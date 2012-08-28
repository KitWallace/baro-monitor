#!/usr/bin/python
import sys
import tty

def read_key() :
    """ decode single keypresses from either the presenter or the keyboard

    """
    last = 0
    tty.setcbreak(sys.stdin)

    while True :
        code = ord(sys.stdin.read(1)) 
        if (code== 53 and last==91 or code==68) : 
            key = "left"
        elif (code==98 or code==66) :
            key = "down"
        elif (code==54 or code==67) :
            key = "right"
        elif (code==49 or code==65) :
            key = "up"
        else :
            key = None
        last=code
        if not(key is None) :
            yield key


