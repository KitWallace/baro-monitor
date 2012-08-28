#!/usr/bin/python
""" yacht control  

"""

import sys
import speak
import time
import persist

from menu import *

# the following are application specific so  should be in the menu
from switch import *
from barometer import *

persist.save(Switch(),'barotalk') 
persist.save(Switch(),'anchortalk')
            
def visit(item) :
   action = item.getAttribute('action')
   if action == "" :
      text = item.getAttribute('title')
   else : 
      text = eval(action)
   speak.say(text)
   print text

name = sys.argv[1]
menu = Menu(name)
menu.run(visit)  

