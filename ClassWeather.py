#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Gruik coded by GuiguiAbloc
# http://blog.guiguiabloc.fr
# http://api.domogeek.fr
#

import urllib,urllib2
import json

class weather:

  def nowopenweathermap(self, lat, lng, request, apikey):
        url = "http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (urllib.quote(str(lat)), urllib.quote(str(lng)), urllib.quote(apikey))
        # print "now " + url
        try:
          data = urllib.urlopen(url).read()
          dataopenweathermap = json.loads(data)
          temp = dataopenweathermap['main']['temp']
          try:
            pressure =  dataopenweathermap['main']['pressure']
          except:
            pressure = 0
          try:
            humidity = dataopenweathermap['main']['humidity']
          except:
            humidity = 0
          try:
            weather = dataopenweathermap['weather'][0]['main']
          except:
            weather =''
          try:
            windspeed = dataopenweathermap['wind']['speed']
          except:
            windspeed = 0
          try:
            windgust = dataopenweathermap['wind']['gust']
          except:
            windgust = 0
          try: 
            rain = dataopenweathermap['rain']['1h']
          except: 
            rain = 0
          try:
            snow = dataopenweathermap['snow']['1h']
          except:
            snow = 0
          if request == "temperature":
            return temp
          if request == "pressure" :
            return pressure
          if request == "humidity" :
            return humidity
          if request == "weather" :
            return weather
          if request == "windspeed":
            return windspeed
          if request == "windgust":
            return windgust
          if request == "rain":
            return rain
          if request == "snow":
            return snow
          if request == "all":
            print dataopenweathermap
            try:
              alldata = {}
              alldata['main']=dataopenweathermap['main']
              alldata['wind']=dataopenweathermap['wind']
              try:
                alldata['rain']=dataopenweathermap['rain']
              except:
                alldata['rain']={}
              try:
                alldata['snow']=dataopenweathermap['snow']
              except:
                alldata['snow']={}
              alldata['weather']=dataopenweathermap['weather'][0]              
              return alldata
            except:
              print e
          else:
            return None
        except:
          return "no data"

  def forecastopenweathermap(self, lat, lng, day, request, apikey):
        url = "http://api.openweathermap.org/data/2.5/onecall?exclude=minutely,hourly&lat=%s&lon=%s&appid=%s&units=metric&cnt=2" % (urllib.quote(str(lat)), urllib.quote(str(lng)), urllib.quote(apikey))
        print day + " " + request + " forecast " + url
        if day == "today" :
            num=0
        else: 
            num=1
            
        try:
          data = urllib.urlopen(url).read()
          dataopenweathermap = json.loads(data)
          temp = dataopenweathermap['daily'][num]['temp']['day']
          pressure =  dataopenweathermap['daily'][num]['pressure']
          humidity = dataopenweathermap['daily'][num]['humidity']
          weather = dataopenweathermap['daily'][num]['weather'][0]['main']
          dataopenweathermap['daily'][num]['speed']=dataopenweathermap['daily'][num]['wind_speed']
          del dataopenweathermap['daily'][num]['wind_speed']
          windspeed = dataopenweathermap['daily'][num]['speed']
          dataopenweathermap['daily'][num]['gust']=dataopenweathermap['daily'][num]['wind_gust']
          del dataopenweathermap['daily'][num]['wind_gust']
          windgust = dataopenweathermap['daily'][num]['gust']
          try:
            rain = dataopenweathermap['daily'][num]['rain']
          except:
            rain = 0
            dataopenweathermap['daily'][num]['rain']=0
          try:
            snow = dataopenweathermap['daily'][num]['snow']
          except:
            snow = 0
            dataopenweathermap['daily'][num]['snow'] = 0
          if request == "temperature":
            return temp
          if request == "pressure" :
            return pressure
          if request == "humidity" :
            return humidity
          if request == "weather" :
            return weather
          if request == "rain":
            return rain
          if request == "snow":
            return snow
          if request == "windspeed":
            return windspeed
          if request == "all":
            return dataopenweathermap['daily'][num] 
          else:
            return None
        except:
          return "no data"
      
def getrain(self, lat, lng, apikey, date):
        url = "http://api.worldweatheronline.com/free/v1//weather.ashx?q=%s,%s&key=%s&format=json&date=%s&includeLocation=no" % (urllib.quote(str(lat)), urllib.quote(str(lng)), urllib.quote(apikey), urllib.quote(date))
        print "rain " + url
        try:  
          data = urllib.urlopen(url).read()
          dataopenweathermap = json.loads(data)
          rain = dataopenweathermap['data']['weather'][0]['precipMM']
          return rain 
        except:
          return "no data"

