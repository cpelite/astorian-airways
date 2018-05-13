# -*- coding: utf-8 -*-

import os
from datetime import date, timedelta, time
from hashlib import sha1 as hash_function
from base64 import b64encode

import arrow
from peewee import *
from aaweb import app, default_timezone

data_db = SqliteDatabase('aaweb.db')

@app.before_request
def _db_connect():
    data_db.connect()

@app.teardown_request
def _db_close(exc):
    if not data_db.is_closed():
        data_db.close()


class Country(Model):
    """ Model of countries """

    name = CharField(max_length=255)
    website = CharField(max_length=255)

    class Meta:
        database = data_db

class Company(Model):
    """ Model of company """

    name = CharField(max_length=100)
    website = CharField(max_length=100)
    ownCompany = BooleanField(default=True)
    percentOwned = IntegerField(default=100)
    country = ForeignKeyField(Country)

    class Meta:
        database = data_db

class PlaneLayout(Model):
    """ Model of plane layouts """

    economy_class = IntegerField(default=0)
    business_class = IntegerField(default=0)
    first_class = IntegerField(default=0)
    flight_attendants = IntegerField()
    picture = CharField()

    class Meta:
        database = data_db

class Airport(Model):
    """ Model of aiports """

    name = CharField(max_length=255)
    code = CharField(unique=True, max_length=3)
    city = CharField(max_length=255)
    country = ForeignKeyField(Country, related_name="airports")
    state = CharField(max_length=255)
    classification = IntegerField() # 0 Primary, 1 Non-Primary, 2 General
    x = IntegerField()
    y = IntegerField()

    class Meta:
        database = data_db

class Route(Model):
    """ Model of abstract routes """

    duration = IntegerField() # in minutes
    departure = ForeignKeyField(Airport, related_name="departures")
    arrival = ForeignKeyField(Airport, related_name="arrivals")
    active = BooleanField(default=True)

    class Meta:
        database = data_db

    def get_coordinates(self):
        """ Returns x and y coordinates of airports as tuples of kind (<departure x+y>,<arrival x+y>) """

        return ((self.departure.x, self.departure.y), (self.arrival.x, self.arrival.y))

    def interpolate(self, percentage):
        """ Interpolates x and y coordinates of departure and arrival airport based on given percentage between 1.0 and 0.0 """
        
        if percentage < 0.0:
            percentage = percentage * -1

        if percentage > 1.0 or percentage < 0.0:
            raise Exception("Percentage value must be between 0.0 and 1.0 but was %f" % percentage)

        x = int(self.departure.x + (self.arrival.x - self.departure.x) * percentage)
        y = int(self.departure.y + (self.arrival.y - self.departure.y) * percentage)
        return x,y

class Plane(Model):
    """ Model of planes """

    aircraft = CharField(max_length=20)
    manufacturer = CharField(max_length=255)
    alias = CharField(unique=True, max_length=100)
    registration = CharField(unique=True, max_length=6)
    pilots = IntegerField()
    purpose = CharField(max_length=255)
    comment = TextField(null=True)
    layout =  ForeignKeyField(PlaneLayout, related_name="layout")
    owner = ForeignKeyField(Company, related_name="owned_planes")
    operator = ForeignKeyField(Company, related_name="leased_planes")

    def get_amount_of_active_routes(self):
        """ Returns the amount of active routes of the current plane """

        return len([1 for i in self.assignments if i.active])

    def current_position(self, relative_datetime=arrow.now(default_timezone)):
        """ Returns a tuple (<Bool:in-air>, (<lat>,<lon>), <flight|airport code>) of the plane """

        ground_list = []

        #app.logger.info("%s" % relative_datetime)

        # check all active route assignments of the current day (assuming that no flights are performed over midnight!)
        for ra in self.assignments.where(RouteAssignment.active == True and getattr(RouteAssignment, relative_datetime.strftime("%A").lower()) == True):
            departure, arrival = ra.calculate_concrete_datetimes(relative_datetime.date())

            # (relative) delta
            delta = ra.route.duration - (int(arrival.format('H')) - int(relative_datetime.format('H'))) * 60 + (int(arrival.format('M')) - int(relative_datetime.format('M')))
            percent_flight = 1.0 * (delta / ra.route.duration) # float casting because of RedHat/Debian difference (RedHat always has percent of 0.0 otherwise :P)
            #print(percent_flight, delta, ra.route.duration)


            if departure < relative_datetime and relative_datetime < arrival: # flying
                return(True, ra.route.interpolate(percent_flight), ra.get_flight_number(with_spaces=False))
            else: # on ground
                ground_list.append( (delta, ra) )

        # 2nd case: somewhere at an airport (cheat and take next flight as indicator :p)
        if len(ground_list) > 0:
            delta, nearest_fight = min( ground_list, key=lambda x: abs(x[0]) )

            if delta >= 0:
                return(False, (ra.route.departure.x, ra.route.departure.y), ra.route.departure.code)
            return(False, (ra.route.arrival.x, ra.route.arrival.y), ra.route.arrival.code)

        # 3rd case: unknown (if no flight is scheduled today): define as stationed @ main hub
        main_hub = Airport.get(code = RouteAssignment.main_hub)
        return(False, (main_hub.x, main_hub.y), main_hub.code)

    class Meta:
        database = data_db

class RouteAssignment(Model):
    """ Assignments to definied routes """

    route = ForeignKeyField(Route)
    plane = ForeignKeyField(Plane, related_name="assignments")
    departure = TimeField(formats=('%H:%M',))
    active = BooleanField(default=True)

    # weekdays to apply route on
    monday = BooleanField(default=False)
    tuesday = BooleanField(default=False)
    wednesday = BooleanField(default=False)
    thursday = BooleanField(default=False)
    friday = BooleanField(default=False)
    saturday = BooleanField(default=False)
    sunday = BooleanField(default=False)

    # FALLBACK AIRPORT
    main_hub = "OJI"

    def calculate_concrete_datetimes(self, relative_date=arrow.now(default_timezone).date()):
        """ Returns a tuple of departure and arrival datetime objects. Calculation is relative to given date instance!"""

        relative_datetime = arrow.Arrow.fromdate(relative_date, tzinfo=default_timezone)
        arrival_t = self.calculate_arrival_time()
        departure_t = self.calculate_departure_time()

        departure_dt = relative_datetime + timedelta( minutes = departure_t.minute + (60 * departure_t.hour) )
        arrival_dt = relative_datetime + timedelta( minutes = arrival_t.minute + (60 * arrival_t.hour) )

        # flight over midnight
        if arrival_t < departure_t:
            arrival_dt = arrival_dt + timedelta(days=1)

        return (departure_dt, arrival_dt)

    def get_flight_number(self, with_spaces=True):
        """ Returns the alphanumerical ID of the route assignment """
        base = u"AA %i" if with_spaces else u"AA%i"
        return base % ( (5000 if self.route.departure.code.upper() == self.main_hub else 100) + self.id)

    @staticmethod
    def get_by_flight_number(flight_number):
        """ Returns the RouteAssignment object bound at given flight number """

        flight_number = int(''.join(i for i in flight_number if i.isdigit()))
        ra = RouteAssignment.get(RouteAssignment.id == flight_number - (100 if flight_number < 5000 else 5000))

        if ra.route.departure.code.upper() == RouteAssignment.main_hub and flight_number > 5000:
            return ra
        elif ra.route.departure.code.upper() != RouteAssignment.main_hub and flight_number < 5000:
            return ra
        raise RouteAssignment.DoesNotExist("No such flight number found")

    def calculate_duration_time(self):
        """ Returns datetime.time object of duration """

        return time( hour = self.route.duration // 60, minute = self.route.duration % 60 )


    def calculate_depature_datetime(self, date=arrow.now(default_timezone).date()):
        """ Returns the datetime of a departure """

        dt_split = self.departure.split(":");
        departure_td = timedelta(hours=int(dt_split[0]), minutes=int(dt_split[1]), seconds=int(dt_split[2]))

        return arrow.Arrow.fromdate(date, tzinfo=default_timezone) + departure_td

    def calculate_departure_time(self, date=arrow.now(default_timezone).date()):
        """ Returns datetime.time object of departure """

        return self.calculate_depature_datetime(date).time()

    def calculate_arrival_datetime(self, date=arrow.now(default_timezone).date()):
        """ Returns datetime of arrival """

        dt = self.calculate_duration_time()
        return self.calculate_depature_datetime(date) + timedelta(minutes=dt.minute + (60 * dt.hour))

    def calculate_arrival_time(self, date=arrow.now(default_timezone).date()):
        """ Returns datetime.time object of arrival """

        return self.calculate_arrival_datetime(date).time()

    class Meta:
        database = data_db


class Account(Model):
    """ Model of user account """

    ADMINISTRATOR = 0
    CUSTOMER = 1
    ROLES = (CUSTOMER, ADMINISTRATOR)

    aid = PrimaryKeyField()
    number = CharField(unique=True, max_length=9)
    email = CharField(max_length=100)
    password = CharField(max_length=40) # sha1, change when using other hashing methods
    salt = CharField(max_length=24)
    is_active = BooleanField(default=False)
    role = IntegerField() # 0: Admin, 1: Customer

    @staticmethod
    def create_and_salt(**kwargs):
        kwargs['password'], kwargs['salt'] = Account.create_salted_password(kwargs['password'])
        return Account.create(**kwargs)

    @staticmethod
    def create_salted_password(password):
        """ Creates a salted password and returns (password, salt) """

        salt = b64encode(os.urandom(24)).decode('utf-8')
        return hash_function((password + salt).encode()).hexdigest(), salt

    def check_password(self, password):
        """ Returns whether given password is correct or not """

        return (self.password == hash_function((password + self.salt).encode()).hexdigest())

    class Meta:
        database = data_db

data_db.connect()
