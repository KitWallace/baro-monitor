points = ["N","NNE","NE","ENE","E","ESE","SE" ,"SSE" ,"S", "SSW","SW","WSW","W", "WNW","NW","NNW","N"]


tendency_table = \
  (   
    (6.05,"rising very rapidly"),
    (3.55 , "rising quickly"),
    (1.55 , "rising"),
    (0.1 , "rising slowly"),
    (-0.1 , "steady"),
    (-1.55 , "falling slowly"),
    (-3.55, "falling"),
    (-6.05 , "falling quickly"),
    (-99 , "falling very rapidly")
  )

forecast1_table = \
  (
    (1022, ( (-0.1 , "Continued fair"),
             (-1.55 , "Fair") ,
             (-3.55 , "Cloudy, Warmer")
           )
    ),
    (1009, ( (-0.1 , "Same as present"), 
             (-1.55 , "Little change"), 
             (-3.55 , "Precipitation likely")
           ) 
    ),
    (980 , ( (-0.1 , "Clearing, cooler"),
             (-1.55 , "Precipitation"), 
             (-3.55 , "Storm")
           ) 
    )
)
def find(table,myval) :
    for threshold,value in table :
        if myval >= threshold :
           return value

def deg_to_dms(dd,latlong) :

   if (latlong == "lat"):
      if (dd< 0) :
         dir = "West"
      else :
         dir = "East"
   else :
      if (dd< 0) :
         dir = "South"
      else :
         dir = "North"

   dd = abs(dd)
   deg = int(dd)
   min = (dd - deg ) * 60
   dmin = int(min)
   sec = int((min - dmin) * 60)
   return "".join([str(deg)," degrees ", str(dmin), "minutes ",str(sec) , " seconds ", dir])

def degree_to_compass_point(deg) :
   dp = deg + 11.25
   dp = dp % 360 
   dp = int(dp // 22.5)
   return points[dp]

def trend_to_tendency(trend) :
    if trend is not None :
        return find(tendency_table,trend)

def forecast1 (baro, trend) :
    if baro is not None and trend is not None :
        return find(find(forecast1_table,baro),trend)



