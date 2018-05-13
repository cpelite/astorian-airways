#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file may be used to populate the database

from aaweb.models import *

#  main():
if __name__ == '__main__':
    data_db.create_tables((Company, PlaneLayout, Country, Plane, Airport, Route, RouteAssignment))

    #############################################
    # GEO DATA (PART I)
    #############################################

    astor = Country.create(
        name = "United States of Astor",
        website = "http://forum.astor.ws",
    )

    stralien = Country.create(
        name = "Republik Stralien",
        website = "http://spinmo.de/stralien",
    )

    livornien = Country.create(
        name = "Königreich beider Archipele Livornien und Melba",
        website = "http://www.livornien.li"
    )


    # COMPANIES
    astorian_airways = Company.create(
        name = "Astorian Airways",
        website = "http://www.astorian-airways.de",
        country = astor,
        ownCompany = True,
    )

    astorian_airways_stralia = Company.create(
        name = "Astorian Airways Stralia",
        website = "http://www.spinmo.de/stralien/forum/index.php/Thread/567-Astorian-Airways-Stralia-Headquarter/",
        country = stralien,
        ownCompany = True,
    )

    astorian_airways_livornien = Company.create(
        name = "Astorian Airways Livornien",
        website = "http://www.livornien.li/forum/viewtopic.php?f=22&t=1041",
        country = livornien,
        ownCompany = True,
    )

    #############################################
    # PLANE LAYOUTS
    #############################################

    b650_std_layout = PlaneLayout.create(
        economy_class = 135,
        business_class = 8,
        flight_attendants = 5,
        picture = "1.png",
    )

    b6310_business = PlaneLayout.create(
        economy_class = 39,
        business_class = 16,
        flight_attendants = 3,
        picture = "2.png",
    )

    a107_std_layout = PlaneLayout.create(
        economy_class = 374,
        business_class = 24,
        first_class = 3,
        flight_attendants = 15,
        picture = "3.png",
    )

    awh_910_std_layout = PlaneLayout.create(
        economy_class = 76,
        business_class = 8,
        flight_attendants = 4,
        picture = "4.png",
    )

    #############################################
    # PLANES
    #############################################

    # A-ARYA
    a_arya = Plane.create(
        aircraft = "B650",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Cradle of Jazz",
        registration = "A-ARYA",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  b650_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # A-TRYN
    a_tryn = Plane.create(
        aircraft = "B650",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Carsten Schmidt",
        registration = "A-TRYN",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  b650_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # A-C3P0
    a_c3p0 = Plane.create(
        aircraft = "B650",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Nicholasburry",
        registration = "A-C3PO",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  b650_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # A-R2D2
    a_r2d2 = Plane.create(
        aircraft = "B650",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Cedar Creek",
        registration = "A-R2D2",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  b650_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # A-L33T
    a_l33t = Plane.create(
        aircraft = "B650",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Francistown",
        registration = "A-L33T",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  b650_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # A-H4XR
    a_h4xr = Plane.create(
        aircraft = "B650",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Walvisoog",
        registration = "A-H4XR",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  b650_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # A-P1NK
    a_p1nk = Plane.create(
        aircraft = "B650",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Michael D. Schaffer",
        registration = "A-P1NK",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  b650_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # A-T35T
    a_t35t = Plane.create(
        aircraft = "B650",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Astoriatown",
        registration = "A-T35T",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  b650_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # S-I5LD
    s_i5ld = Plane.create(
        aircraft = "B650",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Geelong",
        registration = "S-I5LD",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        comment = "Dieses Flugzeug ist aktuell nicht im Einsatz. Es wurde von Rebellen auf der stralischen Insel Geelong entführt. Die Geschäftsführung berichtet, dass zu keinem Zeitpunkt Passagiere von Astorian Airways in Gefahr waren.",
        layout =  b650_std_layout,
        owner = astorian_airways,
        operator = astorian_airways_stralia,
    )

    # A-C4M8
    a_c4m8 = Plane.create(
        aircraft = "B650",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Wallby",
        registration = "A-C4M8",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  b650_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # S-B7U8
    s_b7u8 = Plane.create(
        aircraft = "B650",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Vic",
        registration = "S-B7U8",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  b650_std_layout,
        owner = astorian_airways,
        operator = astorian_airways_stralia,
    )
    
    ########## SPECIALS

    # A-B1S1
    a_b1s1 = Plane.create(
        aircraft = "B310",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Westby County",
        registration = "A-B1S1",
        pilots = 2,
        purpose = "Geschäftsflüge",
        layout = b6310_business,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # L-AS4Y
    l_as4y = Plane.create(
        aircraft = "B310",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Melba",
        registration = "L-AS4Y",
        pilots = 2,
        purpose = "Geschäftsflüge",
        layout = b6310_business,
        owner = astorian_airways,
        operator = astorian_airways_livornien,
    )

    ########## JUMBOS

    # A-0LEJ
    a_0lej = Plane.create(
        aircraft = "A107",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Cinnamon Bun",
        registration = "A-0LEJ",
        pilots = 2,
        purpose = "Lang- und Interkontinentalstrecken",
        layout =  a107_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # A-T4FT
    a_t4ft = Plane.create(
        aircraft = "A107",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Vino Rosario",
        registration = "A-T4FT",
        pilots = 2,
        purpose = "Lang- und Interkontinentalstrecken",
        layout =  a107_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # A-C0TN
    a_c0tn = Plane.create(
        aircraft = "A107",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Port Caroline",
        registration = "A-C0TN",
        pilots = 2,
        purpose = "Lang- und Interkontinentalstrecken",
        layout =  a107_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # L-L4VL
    l_l4vL = Plane.create(
        aircraft = "A107",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Elberg",
        registration = "L-L4VL",
        pilots = 2,
        purpose = "Lang- und Interkontinentalstrecken",
        layout =  a107_std_layout,
        owner = astorian_airways,
        operator = astorian_airways_livornien,
    )

    # A-VDWP
    a_vdwp = Plane.create(
        aircraft = "A107",
        manufacturer = "Tang Industrial Services Aerospace",
        alias = "Blueberry Muffin",
        registration = "A-VDWP",
        pilots = 2,
        purpose = "Lang- und Interkontinentalstrecken",
        layout =  a107_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    ########## EMBRAER

    # L-BLU3
    l_blu3= Plane.create(
        aircraft = "910-LR",
        manufacturer = "Automobil- und Aviatikwerke Haltberg",
        alias = "Lienz",
        registration = "L-BLU3",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  awh_910_std_layout,
        owner = astorian_airways,
        operator = astorian_airways_livornien,
    )

    # L-G33K
    l_g33k= Plane.create(
        aircraft = "910-LR",
        manufacturer = "Automobil- und Aviatikwerke Haltberg",
        alias = "Brisken",
        registration = "L-G33K",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  awh_910_std_layout,
        owner = astorian_airways,
        operator = astorian_airways_livornien,
    )

    # A-GR3N
    a_gr3n = Plane.create(
        aircraft = "910-LR",
        manufacturer = "Automobil- und Aviatikwerke Haltberg",
        alias = "St. Montélimar",
        registration = "A-GR3N",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  awh_910_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # A-BL4K
    a_bl4k = Plane.create(
        aircraft = "910-LR",
        manufacturer = "Automobil- und Aviatikwerke Haltberg",
        alias = "Côte te Morbinaux",
        registration = "A-BL4K",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  awh_910_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # A-R05A
    a_r05a = Plane.create(
        aircraft = "910-LR",
        manufacturer = "Automobil- und Aviatikwerke Haltberg",
        alias = "Port Bologne",
        registration = "A-R05A",
        pilots = 2,
        purpose = "Kurz- und Mittelstrecken",
        layout =  awh_910_std_layout,
        owner = astorian_airways,
        operator = astorian_airways,
    )

    # L-H4PY
    #l_h4py= Plane.create(
    #    aircraft = "910-LR",
    #    manufacturer = "Automobil- und Aviatikwerke Haltberg",
    #    alias = "Altburg",
    #    registration = "L-H4PY",
    #    pilots = 2,
    #    purpose = "Kurz- und Mittelstrecken",
    #    layout =  awh_910_std_layout,
    #    owner = astorian_airways,
    #    operator = astorian_airways_livornien,
    #)

    # L-YL0W
    #l_yl0w= Plane.create(
    #    aircraft = "910-LR",
    #    manufacturer = "Automobil- und Aviatikwerke Haltberg",
    #    alias = "Haltberg",
    #    registration = "L-YL0W",
    #    pilots = 2,
    #    purpose = "Kurz- und Mittelstrecken",
    #    layout =  awh_910_std_layout,
    #    owner = astorian_airways,
    #    operator = astorian_airways_livornien,
    #)

    # L-A5TR
    #l_a5tr= Plane.create(
    #    aircraft = "910-LR",
    #    manufacturer = "Automobil- und Aviatikwerke Haltberg",
    #    alias = "Astor",
    #    registration = "L-A5TR",
    #    pilots = 2,
    #    purpose = "Kurz- und Mittelstrecken",
    #    layout =  awh_910_std_layout,
    #    owner = astorian_airways,
    #    operator = astorian_airways_livornien,
    #)


    #############################################
    # GEO DATA (PART II)
    # NATIONAL AIRPORTS
    #############################################


    # AIRPORTS ASSENTIA
    ham = Airport.create(
        name = "Lakefront Westby National Airport",
        code = "HAM",
        city = "Hambry",
        country = astor,
        state = "Assentia",
        classification = 1,
        x = 460,
        y = 89,
    )

    amb = Airport.create(
        name = "Central Assantian National Airport",
        code = "AMB",
        city = "Ambridge",
        country = astor,
        state = "Assentia",
        classification = 1,
        x = 391,
        y = 113,
    )

    frb = Airport.create(
        name = "Fredericksburg International Airport",
        code = "FRB",
        city = "Fredericksburg",
        country = astor,
        state = "Assentia",
        classification = 1,
        x = 403,
        y = 9,
    )

    # AIRPORTS FREELAND
    gar = Airport.create(
        name = "Freeland Airport",
        code = "GAR",
        city = "Gareth",
        country = astor,
        state = "Freeland",
        classification = 0,
        x = 637,
        y = 155,
    )

    pba = Airport.create(
        name = "International Airport Port Bologne",
        code = "PBA",
        city = "Port Bologne",
        country = astor,
        state = "Freeland",
        classification = 0,
        x = 641,
        y = 110,
    )

    # AIRPORTS ASTORIA STATE
    oji = Airport.create(
        name = "Ole Jann International Airport",
        code = "OJI",
        city = "Astoria City",
        country = astor,
        state = "Astoria State",
        classification = 0,
        x = 561,
        y = 190,
    )

    # AIRPORTS LAURENTINA
    neb = Airport.create(
        name = "Savannah Airport",
        code = "NEB",
        city = "New Beises",
        country = astor,
        state = "Laurentiana",
        classification = 1,
        x = 556,
        y = 288,
    )


    # AIRPORTS NEW ALCANTARA
    con = Airport.create(
        name = "El Conjunto Airport",
        code = "CON",
        city = "El Conjunto",
        country = astor,
        state = "New Alcantara",
        classification = 1,
        x = 372,
        y = 276,
    )

    # AIRPORTS SERENA
    hnm = Airport.create(
        name = "Hong Nam Airport",
        code = "HNM",
        city = "Hong Nam",
        country = astor,
        state = "Serena",
        classification = 1,
        x = 202,
        y = 190,
    )

    jda = Airport.create(
        name = "Jerome Davenport International Airport",
        code = "JDA",
        city = "Freeport City",
        country = astor,
        state = "Serena",
        classification = 0,
        x = 287,
        y = 260,
    )

    scn = Airport.create(
        name = "Sen City National Airport",
        code = "SCN",
        city = "Sen City",
        country = astor,
        state = "Serena",
        classification = 1,
        x = 278,
        y = 217,
    )

    svi = Airport.create(
        name = "St. Vincentius International Airport",
        code = "SVI",
        city = "St. Vincentius",
        country = astor,
        state = "Serena",
        classification = 1,
        x = 162,
        y = 340,
    )

    #############################################
    # GEO DATA (PART III)
    # AIRPORTS STRALIA
    #############################################

    cbp = Airport.create(
        name = "Flughafen Camber-Perf",
        code = "CBP",
        city = "Camber-Perf",
        country = stralien,
        state = "Terridor",
        classification = 0,
        x = 481,
        y = 341,
    )

    gee = Airport.create(
        name = "Ernest Honcho Flughafen",
        code = "GEE",
        city = "Geelong",
        country = stralien,
        state = "Geelong",
        classification = 1,
        x = 407,
        y = 394,
    )

    bsh = Airport.create(
        name = "Flughafen Brishen",
        code = "BSH",
        city = "Brishen",
        country = stralien,
        state = "Hjaarta",
        classification = 1,
        x = 575,
        y = 455,
    )

    #############################################
    # GEO DATA (PART IV)
    # AIRPORTS STRALIA
    #############################################

    alt = Airport.create(
        name = "Altburg Breeda International",
        code = "ALT",
        city = "Altburg",
        country = livornien,
        state = "Herzogtum Born",
        classification = 0,
        x = 865,
        y = 234,
    )

    bri = Airport.create(
        name = "Brisken Airport",
        code = "BRI",
        city = "Brisken",
        country = livornien,
        state = "Königreich Melba",
        classification = 1,
        x = 972,
        y = 263,
    )

    ssn = Airport.create(
        name = "San Sebastian International",
        code = "SSN",
        city = "San Sebastian",
        country = livornien,
        state = "Provinz Livornisch-Garùpano",
        classification = 0,
        x = 878,
        y = 714,
    )

    prc = Airport.create(
        name = "Flugplatz Port au Prince",
        code = "PRC",
        city = "Port au Prince",
        country = livornien,
        state = "Kolonie St. Etienne",
        classification = 1,
        x = 27,
        y = 689,
    )

    hal = Airport.create(
        name = "Flugplatz Haltberg",
        code = "HAL",
        city = "Haltberg",
        country = livornien,
        state = "Markgrafschaft Haltberg",
        classification = 1,
        x = 866,
        y = 263,
    )

    #############################################
    # CURRENT ROUTES
    #############################################

    def create_return_routes(duration, departure, arrival):
        return (
            Route.create( duration = duration, departure = departure, arrival = arrival ),
            Route.create( duration = duration, departure = arrival, arrival = departure )
            )

    ############################
    # NATIONAL ROUTES
    ############################

    # HNM/OJI
    oji_hnm, hnm_oji = create_return_routes(60 * 5 + 30, oji, hnm)

    # CON/OJI
    oji_con, con_oji = create_return_routes(60 * 3 + 25, oji, con)

    # NEB/OJI
    oji_neb, neb_oji = create_return_routes(60 * 1 + 30, oji, neb)

    # GAR/OJI
    oji_gar, gar_oji = create_return_routes(60 * 1 + 10, oji, gar)

    # AMB/OJI
    oji_amb, amb_oji = create_return_routes(60 * 2 + 50, oji, amb)

    # HAM/OJI
    oji_ham, ham_oji = create_return_routes(60 * 2 + 20, oji, ham)

    # SEN/OJI
    oji_scn, scn_oji = create_return_routes(60 * 4 + 30, oji, scn)

    # JDA/OJI
    oji_jda, jda_oji = create_return_routes(60 * 4 + 40, oji, jda)

    # PBA/OJI
    oji_pba, pba_oji = create_return_routes(60 * 1 + 50, oji, pba)

    # FYB/OJI
    oji_frb, frb_oji = create_return_routes(60 * 3 + 45, oji, frb)

    # SVI/OJI
    oji_svi, svi_oji = create_return_routes(60 * 11 + 25, oji, svi)

    #### SCN NATIONAL ROUTES

    # CON/SCN
    scn_con, con_scn = create_return_routes(60 * 1 + 45, scn, con)

    # HNM/SCN
    scn_hnm, hnm_scn = create_return_routes(60 * 1 + 25, scn, hnm)

    # AMB/SCN
    scn_amb, amb_scn = create_return_routes(60 * 2 + 5, scn, amb)

    # SVI/SCN
    scn_svi, svi_scn = create_return_routes(60 * 2 + 15, scn, svi)

    # FRB/SCN
    scn_frb, frb_scn = create_return_routes(60 * 4 + 10, scn, frb)

    ############################
    # INTERNATIONAL ROUTES
    ############################

    # STRALIA
    oji_cbp, cbp_oji = create_return_routes(60 * 3 + 20, oji, cbp)

    # NATIONAL STRALIA
    cbp_gee, gee_cbp = create_return_routes(60 * 1 + 10, cbp, gee)
    cbp_bsh, bsh_cbp = create_return_routes(60 * 3 + 10, cbp, bsh)

    # LIVORNIEN
    oji_alt, alt_oji = create_return_routes(60 *  4 + 30, oji, alt)
    scn_prc, prc_scn = create_return_routes(60 *  9  + 25, scn, prc)
    scn_alt, alt_scn = create_return_routes(60 * 11  + 15, scn, alt)

    # NATIONAL LIVORNIEN
    alt_hal, hal_alt = create_return_routes(60 * 1  +  0, alt, hal)
    alt_bri, bri_alt = create_return_routes(60 * 1  + 40, alt, bri)
    alt_ssn, ssn_alt = create_return_routes(60 * 9  + 10, alt, ssn)

    # ASSIGNMENTS
    from datetime import time

    ############################
    # A-TRYN (Hong Nom Hopper)
    ############################

    _ = RouteAssignment.create(
        plane = a_tryn,
        route = hnm_oji,
        departure = time(8,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True,
    )

    _ = RouteAssignment.create(
        plane = a_tryn,
        route = oji_hnm,
        departure = time(14,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True,
    )

    ############################
    # A-ARYA (Freestate, Hambry)
    ############################

    # MON, WED, FRI, SUN
    _ = RouteAssignment.create(
        plane = a_arya,
        route = oji_ham,
        departure = time(8,0),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )
    _ = RouteAssignment.create(
        plane = a_arya,
        route = ham_oji,
        departure = time(11,0),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )
    _ = RouteAssignment.create(
        plane = a_arya,
        route = oji_gar,
        departure = time(14,30),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )
    _ = RouteAssignment.create(
        plane = a_arya,
        route = gar_oji,
        departure = time(16,30),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )
    _ = RouteAssignment.create(
        plane = a_arya,
        route = oji_neb,
        departure = time(18,30),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )
    _ = RouteAssignment.create(
        plane = a_arya,
        route = neb_oji,
        departure = time(20,30),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )

    # TUE, THU, SAT
    _ = RouteAssignment.create(
        plane = a_arya,
        route = oji_gar,
        departure = time(6,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )
    _ = RouteAssignment.create(
        plane = a_arya,
        route = gar_oji,
        departure = time(8,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )
    _ = RouteAssignment.create(
        plane = a_arya,
        route = oji_neb,
        departure = time(10,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )
    _ = RouteAssignment.create(
        plane = a_arya,
        route = neb_oji,
        departure = time(12,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )
    _ = RouteAssignment.create(
        plane = a_arya,
        route = oji_ham,
        departure = time(14,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )
    _ = RouteAssignment.create(
        plane = a_arya,
        route = ham_oji,
        departure = time(17,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )

    ############################
    # A-C3P0 (North/South Hopper)
    ############################

    # MON, WED, FRI, SUN
    _ = RouteAssignment.create(
        plane = a_c3p0,
        route = oji_con,
        departure = time(6,30),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )
    _ = RouteAssignment.create(
        plane = a_c3p0,
        route = con_oji,
        departure = time(10,30),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )
    _ = RouteAssignment.create(
        plane = a_c3p0,
        route = oji_amb,
        departure = time(14,30),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )
    _ = RouteAssignment.create(
        plane = a_c3p0,
        route = amb_oji,
        departure = time(18,0),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )

    # TUE, THU, SAT
    _ = RouteAssignment.create(
        plane = a_c3p0,
        route = oji_amb,
        departure = time(7,0),
        tuesday = True,
        thursday = True,
        saturday = True,
    )
    _ = RouteAssignment.create(
        plane = a_c3p0,
        route = amb_oji,
        departure = time(10,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )
    _ = RouteAssignment.create(
        plane = a_c3p0,
        route = oji_con,
        departure = time(14,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )
    _ = RouteAssignment.create(
        plane = a_c3p0,
        route = con_oji,
        departure = time(18,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )

    ############################
    # A-R2D2 (Freyburg, Freestate)
    ############################

    # MON, WED, FRI, SUN
    _ = RouteAssignment.create(
        plane = a_r2d2,
        route = oji_frb,
        departure = time(7,0),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )
    _ = RouteAssignment.create(
        plane = a_r2d2,
        route = frb_oji,
        departure = time(11,30),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )

    _ = RouteAssignment.create(
        plane = a_r2d2,
        route = oji_pba,
        departure = time(16,0),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )

    _ = RouteAssignment.create(
        plane = a_r2d2,
        route = pba_oji,
        departure = time(18,30),
        monday = True,
        wednesday = True,
        friday = True,
        sunday = True,
    )

    # TUE, THU, SAT
    _ = RouteAssignment.create(
        plane = a_r2d2,
        route = oji_pba,
        departure = time(8,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )

    _ = RouteAssignment.create(
        plane = a_r2d2,
        route = pba_oji,
        departure = time(11,0),
        tuesday = True,
        thursday = True,
        saturday = True,
    )

    _ = RouteAssignment.create(
        plane = a_r2d2,
        route = oji_frb,
        departure = time(14,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )

    _ = RouteAssignment.create(
        plane = a_r2d2,
        route = frb_oji,
        departure = time(19,0),
        tuesday = True,
        thursday = True,
        saturday = True,
    )

    ############################
    # A-L33T (Sen City Hopper)
    ############################

    _ = RouteAssignment.create(
        plane = a_l33t,
        route = scn_oji,
        departure = time(9,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True,
    )

    _ = RouteAssignment.create(
        plane = a_l33t,
        route = oji_scn,
        departure = time(14,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True,
    )

    ############################
    # A-H4XR (JDA Hopper)
    ############################

    _ = RouteAssignment.create(
        plane = a_h4xr,
        route = jda_oji,
        departure = time(8,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True,
    )

    _ = RouteAssignment.create(
        plane = a_h4xr,
        route = oji_jda,
        departure = time(14,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True,
    )

    ############################
    # A-0LEJ (SVI Island Hopper)
    ############################
    _ = RouteAssignment.create(
        plane = a_0lej,
        route = oji_svi,
        departure = time(8,30),
        monday = True,
        wednesday = True,
        friday = True,
    )

    _ = RouteAssignment.create(
        plane = a_0lej,
        route = svi_oji,
        departure = time(8,30),
        tuesday = True,
        thursday = True,
        saturday = True,
    )

    ############################
    # A-C4M8 (Camber-Perf Return)
    ############################
    _ = RouteAssignment.create(
        plane = a_c4m8,
        route = oji_cbp,
        departure = time(10,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_c4m8,
        route = frb_oji,
        departure = time(14,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # S-B7U8 (Camber-Perf Return)
    ############################
    _ = RouteAssignment.create(
        plane = s_b7u8,
        route = cbp_bsh,
        departure = time(6,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = s_b7u8,
        route = bsh_cbp,
        departure = time(10,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = s_b7u8,
        route = cbp_bsh,
        departure = time(14,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = s_b7u8,
        route = bsh_cbp,
        departure = time(18,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # S-I5LD (Camber-Perf Return)
    ############################
    _ = RouteAssignment.create(
        plane = s_i5ld,
        route = cbp_gee,
        departure = time(10,00),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = s_i5ld,
        route = gee_cbp,
        departure = time(12,00),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = s_i5ld,
        route = cbp_gee,
        departure = time(14,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = s_i5ld,
        route = gee_cbp,
        departure = time(16,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # Altburg - Haltberg
    ############################
    _ = RouteAssignment.create(
        plane = l_blu3,
        route = alt_hal,
        departure = time(7,00),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_blu3,
        route = hal_alt,
        departure = time(8,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_blu3,
        route = alt_hal,
        departure = time(10,00),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_blu3,
        route = hal_alt,
        departure = time(11,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_blu3,
        route = alt_hal,
        departure = time(13,00),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_blu3,
        route = hal_alt,
        departure = time(14,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_blu3,
        route = alt_hal,
        departure = time(16,00),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_blu3,
        route = hal_alt,
        departure = time(17,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_blu3,
        route = alt_hal,
        departure = time(19,00),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_blu3,
        route = hal_alt,
        departure = time(20,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # Altburg - Brisken
    ############################

    _ = RouteAssignment.create(
        plane = l_g33k,
        route = alt_bri,
        departure = time(9,00),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_g33k,
        route = bri_alt,
        departure = time(11,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_g33k,
        route = alt_bri,
        departure = time(15,00),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_g33k,
        route = bri_alt,
        departure = time(17,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # Astoria City - Altburg
    ############################
    _ = RouteAssignment.create(
        plane = a_c0tn,
        route = oji_alt,
        departure = time(8,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_c0tn,
        route = alt_oji,
        departure = time(14,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # Altburg - San Sebastian
    ############################
    _ = RouteAssignment.create(
        plane = l_l4vL,
        route = ssn_alt,
        departure = time(6,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = l_l4vL,
        route = alt_ssn,
        departure = time(15,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # Sen City - Port au Prince
    ############################
    _ = RouteAssignment.create(
        plane = a_t4ft,
        route = scn_prc,
        departure = time(6,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_t4ft,
        route = prc_scn,
        departure = time(15,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # Sen City - Hong Nam/El Conjunto (1st plane)
    ############################
    _ = RouteAssignment.create(
        plane = a_r05a,
        route = scn_hnm,
        departure = time(6,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_r05a,
        route = hnm_scn,
        departure = time(8,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_r05a,
        route = scn_hnm,
        departure = time(9,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_r05a,
        route = hnm_scn,
        departure = time(12,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_r05a,
        route = scn_con,
        departure = time(14,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_r05a,
        route = con_scn,
        departure = time(17,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # Sen City - Hong Nam/El Conjunto (2nd plane)
    ############################
    _ = RouteAssignment.create(
        plane = a_gr3n,
        route = scn_con,
        departure = time(9,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_gr3n,
        route = con_scn,
        departure = time(12,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_gr3n,
        route = scn_hnm,
        departure = time(15,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_gr3n,
        route = hnm_scn,
        departure = time(17,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_gr3n,
        route = scn_hnm,
        departure = time(19,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_gr3n,
        route = hnm_scn,
        departure = time(21,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # Sen City - Ambridge
    ############################
    _ = RouteAssignment.create(
        plane = a_bl4k,
        route = scn_amb,
        departure = time(9,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_bl4k,
        route = amb_scn,
        departure = time(12,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_bl4k,
        route = scn_amb,
        departure = time(15,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_bl4k,
        route = amb_scn,
        departure = time(18,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # Sen City - St. Vincentius
    ############################
    _ = RouteAssignment.create(
        plane = a_p1nk,
        route = scn_svi,
        departure = time(8,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_p1nk,
        route = svi_scn,
        departure = time(11,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_p1nk,
        route = scn_svi,
        departure = time(14,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_p1nk,
        route = svi_scn,
        departure = time(17,30),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # Sen City - Fredericksburg
    ############################
    _ = RouteAssignment.create(
        plane = a_t35t,
        route = scn_frb,
        departure = time(9,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    _ = RouteAssignment.create(
        plane = a_t35t,
        route = frb_scn,
        departure = time(15,0),
        monday = True,
        tuesday = True,
        wednesday = True,
        thursday = True,
        friday = True,
        saturday = True,
        sunday = True
    )

    ############################
    # Sen City - Altburg
    ############################
    _ = RouteAssignment.create(
        plane = a_vdwp,
        route = scn_alt,
        departure = time(8,00),
        monday = True,
        wednesday = True,
        friday = True,
    )

    _ = RouteAssignment.create(
        plane = a_vdwp,
        route = alt_scn,
        departure = time(8,00),
        tuesday = True,
        thursday = True,
        saturday = True,
    )