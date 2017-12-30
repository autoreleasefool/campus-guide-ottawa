"""Campus Guide - University of Ottawa script setup."""

from setuptools import setup

setup(name='cguo',
      version='0.1.0',
      packages=['cguo'],
      entry_points={
          'console_scripts': [
              'cguo = cguo.__main__:main'
          ]
      })