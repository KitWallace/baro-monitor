#!/usr/bin/python
import time
import speak

from persistant import *
from switch import *

Switch("clock").put()

while True :
   sw = get("clock")
   if sw.on :
      message = "The time on Aremiti is " + \
          speak.escape_XML(speak.ssml_break(500)) + \
          str(int(time.strftime('%I'))) + \
          ' ' + time.strftime('%M %p')
      speak.say(message)
   time.sleep(60)

