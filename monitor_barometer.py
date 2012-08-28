#!/usr/bin/python

from barometer import *

baro = Barometer("baro",300,3600)
baro.reload()
baro.monitor(60)

