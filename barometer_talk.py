#!/usr/bin/python

import speak

from persistant import *
from barometer import *
from switch import *

while True :
    baro = get("baro")
    sw = get("barotalk")
    if sw.on :
       msg = baro.talk_text()
       speak.say(msg)
    time.sleep (300)
    
 
