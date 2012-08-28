import time
from barometer import *

baro = Barometer("baro",20,100)
baro.reload()
baro.monitor(5)
