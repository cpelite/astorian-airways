# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='aaweb',
      version='0.1',
      description='Astorian Airways App for Astor',
      author='Arjan van de Westplate',
      author_email='arjan@astorian-airways.de',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask>=0.10.1', 'peewee>=0.2.5', 'pillow>=2.8.1', 'qrcode>=5.1', 'arrow>=0.5.0'],
     )
