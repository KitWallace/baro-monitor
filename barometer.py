#!/usr/bin/python

import time
import sys
import speak
import persist
from weather import *
from history import *
import conv
from switch import *

class Barometer :
    def __init__(self,name,smooth_secs,history_secs) :
        self.name = name
        self.smooth = History(smooth_secs) 
        self.history = History(history_secs)
        
        """ dummy up the pressure by reading from a weather station"""
        self.station = Weather("horfield","http://www.martynhicks.co.uk/weather/clientraw.txt")
     
    def reload(self) :
        logname = "log/" + self.name + ".dat"
        logfile =  open(logname,"r")
        self.history.load(logfile)
        logfile.close()
        if self.history :
            last = self.history.latest()
            self.baro = last[0]
            self.ts = last[1]
            self.update_trend()
        else :
            self.baro = None
            self.ts = None

    def monitor(self,interval) :
        self.interval = interval
        self.running = True
        logname = "log/" + self.name + ".dat"
        logfile =  open(logname,"a")
        while self.running : 
            self.station.refresh()
            baro_now = self.station.baro
            if self.station.updated :
                self.smooth.add(baro_now)
                if self.smooth.full():
                    (self.baro,self.ts) = self.smooth.average()
                    self.history.add_timed(self.baro,self.ts,logfile)
                    self.smooth.clear()
                    self.update_trend()
                    barotalk = persist.load(self.name+"talk")
                    if barotalk.on :
                        speak.say(self.baro_text())
                        
                    persist.save(self,self.name)
                
                time.sleep(self.interval)
            else :
                time.sleep(10) # refresh failed - try again in 10 seconds 
      
    def update_trend(self) :
        aged_baro = self.history.limit_value()
        if aged_baro is None :
            self.trend = None
            self.tendancy = ""
        else  :
            self.trend = round(self.baro - aged_baro ,1)
            self.tendancy = conv.trend_to_tendancy(self.trend)
              
                  


    def baro_text(self) :
        return "Barometer is " + str(int(self.baro)) + " " + self.tendancy


    def __getstate__(self) :
        odict = self.__dict__.copy()
        del odict['smooth']
        del odict['history']
        return odict
