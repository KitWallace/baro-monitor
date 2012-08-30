#!/usr/bin/python
import urllib
import time


class Weather :
    """ cut down version just for the barometer mock """
                                       
    def __init__(self,id,url) :
        self.url = url
        self.id = id 
        self.refresh()

    def refresh(self) :
        try:
            page = urllib.urlopen(self.url)
            report = page.readline()
            data = report.split(" ")
            self.baro = float(data[6])
            self.ts = time.time()
            self.updated = True
        except Exception :
            self.updated = False
