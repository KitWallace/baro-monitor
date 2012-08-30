#!/usr/bin/python
""" yacht control  

"""

import sys
import speak
import time

from menu import *
from persistant import *

# the following are application specific so should be in the menu
from switch import *
from barometer import *

def visit(item) :
   action = item.getAttribute('action')
   if action == "" :
      text = item.getAttribute('title')
   else : 
      text = eval(action)
   speak.say(text)
   print text


Switch('barotalk').put() 
Switch('anchortalk').put() 
Switch('clock').put()

print "starting"

name = sys.argv[1]
menu = Menu(name)
print menu
menu.run(visit)  

