#!/usr/bin/python
import urllib
import time


class Weather :
  
  
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
        self.ts = time.strftime('%H:%M:%S')
        self.updated = True
      except :
        self.updated = False
    
  


