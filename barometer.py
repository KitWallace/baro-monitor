#!/usr/bin/python

import time
import sys
from persistant import *
from history import *
from weather import *
from moving_sequence import *

import conv

def baroReader(interval_secs) :
    station = Weather("horfield","http://www.martynhicks.co.uk/weather/clientraw.txt")
    while True :
       station.refresh()
       if station.baro is None :
          time.sleep(10)
       else :
          yield(station.baro)
          time.sleep(interval_secs)

def baroSmoother(interval_secs,smooth_secs) :
    baro = baroReader(interval_secs)
    max = int(smooth_secs / interval_secs)
    while True:
       total_baro = 0
       for i in range(max) :
          reading = baro.next()
          total_baro += reading
       average_baro = round(total_baro / max, 2)
       yield(average_baro)
       

class Barometer(Persistant) :
    def __init__(self,name,interval_secs, smooth_secs, trend_secs) :
        self.name = name
        self.baro = None
        self.interval_secs = interval_secs
        self.smooth_secs = smooth_secs
        self.trend_secs = trend_secs 
        self.trend_length = int(trend_secs /smooth_secs)
        self.history = Moving_Sequence(self.trend_length)
        self.trend = 0
        self.tendency = ""
        self.forecast = ""

    def monitor(self) :
        reader = baroSmoother(self.interval_secs,self.smooth_secs)
        for self.baro in reader :
            self.history.add(self.baro)
            self.updateTrend()
            self.put()
            print time.strftime("%a %H:%M",time.localtime(self.ts)),self.baro,self.trend,self.tendency,self.forecast
 
    def updateTrend(self) :
        if self.history.get(-1) is not None :
            self.trend = self.history.get(0) - self.history.get(-1)
            self.tendency = conv.trend_to_tendency(self.trend)
            self.forecast = conv.forecast1(self.baro,self.trend)

    def talk_text(self) :
        return "Barometer is " + str(int(round(self.baro,0))) +  " " + self.tendency + " " + self.forecast
        
    def __getstate__(self) :
        odict = self.__dict__.copy()
        del odict['history']
        return odict
    
