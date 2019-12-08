# -*- coding: utf-8 -*-
"""
BreaktimeWatch | Program for tracking breaktimes (coffee- or smokebreak)
Copyright (C) 2019  Ned84 ned84@protonmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

#from datetime import datetime
import math
import threading
import json
import os
import sys
import datetime


class Functions(object):
    time1 = datetime.datetime.now()
    time2 = datetime.datetime.now()
    totalmin = 0
    totalsec = 0
    diffsec = 0
    selecteddate = ""
    totalworkedhours = 0
    totalworkeddays = 0
    workedhoursatdate = 0.0


    def __init__():
        dt = datetime.datetime.now()
        dtwithoutmill = dt.replace(microsecond=0)
        Functions.total = dtwithoutmill

    def GetTime(self):
        dt = datetime.datetime.now()
        dtwithoutmill = dt.replace(microsecond=0)
        print(dtwithoutmill)
        return dtwithoutmill

    def Start(self):
        Functions.time1 = Functions.GetTime(self)
        daynow = datetime.datetime.now().strftime("%d-%m, %Y")
        Functions.GetTotalFromJson(daynow)


    def Stop(self):
        Functions.time2 = Functions.GetTime(self)
        Functions.CalcDiff()

        daynow = datetime.datetime.now().strftime("%d-%m, %Y")
        Functions.WriteTimeToJson(daynow,Functions.totalsec)

        
    def CalcDiff(): 
        try:
            diff = Functions.time2 - Functions.time1   
            Functions.totalsec = Functions.totalsec + diff.seconds
            Functions.totalmin = Functions.totalsec / 60
            Functions.totalmin = math.floor(Functions.totalmin)
            print()   
            print("diff = {0}".format(diff))
            print("totalsec = {0}".format(Functions.totalsec))
            print("totalmin = {0}".format(Functions.totalmin))
        except Exception as exc: 
            Functions.WriteLog(exc)

    def WriteTimeToJson(date,totalsec):
        try:
            file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\tmedta\\Data.JSON', "r")
            json_array = json.load(file)
            date_list = []

            for item in json_array:
                date_details = {}
                date_details['date'] = item['date']
                date_details['totalbreaktime'] = item['totalbreaktime']
                date_details['totalworkedhours'] = item['totalworkedhours']
                if date_details['date'] == date:
                     date_details['totalbreaktime'] = totalsec

                date_list.append(date_details)
            print("JSON = \n\r       {0}".format(date_list))
            file.close()

            file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\tmedta\\Data.JSON', "w")
            json.dump(date_list, file, indent=1, sort_keys=True)
            file.close()

        except Exception as exc: 
            Functions.WriteLog(exc)

    def GetTotalFromJson(date):
        try:
            file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\tmedta\\Data.JSON')
            json_array = json.load(file)
            date_list = []
            found = False
            daysoftheweek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            totalhoursdate = 0


            for item in json_array:
                date_details = {}
                date_details['date'] = item['date']
                date_details['totalbreaktime'] = item['totalbreaktime']
                date_details['totalworkedhours'] = item['totalworkedhours']
                if date_details['date'] == date:
                    Functions.totalsec = date_details['totalbreaktime']
                    Functions.totalmin = Functions.totalsec / 60
                    Functions.totalmin = math.floor(Functions.totalmin)
                    totalhoursdate = date_details['totalworkedhours']
                    Functions.workedhoursatdate = date_details['totalworkedhours']
                    found = True
                date_list.append(date_details)

            file.close()

            if found == False:
                file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\tmedta\\Data.JSON', "w+")
                date_list.append({"date": date,"totalbreaktime": 0, "totalworkedhours": 0})
                json.dump(date_list,file, indent=1, sort_keys=True)
                file.close()
                Functions.totalsec = 0
                Functions.totalmin = Functions.totalsec / 60
                Functions.totalmin = math.floor(Functions.totalmin)


            totalhoursdate = 0
            weekday = ("{0}".format(Functions.selecteddate))
      
            weekday = weekday[0:3]

            daynumber = 0
            index = 0
            for day in daysoftheweek:
                if day != weekday:
                    index += 1
                else:
                    daynumber = index

            datetime_object = datetime.datetime.strptime(date, '%d-%m, %Y')
            for item in json_array:
                index = 0
                while index <= daynumber:
                    timedeltadays = datetime_object - datetime.timedelta(days=index)
                    timedeltadays = timedeltadays.strftime('%d-%m, %Y')
                    if item['date'] == timedeltadays :
                        totalhoursdate = totalhoursdate + item['totalworkedhours']
                    index += 1

            Functions.totalworkeddays = daynumber + 1
            Functions.totalworkedhours = totalhoursdate
               
        except Exception as exc: 
            Functions.WriteLog(exc)

    paramversion = ""
    paramworkdaysperweek = 0
    paramworkhoursperweek = 0

    def GetSettingsFromJson():
    
        try:
            file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\btwtwparam\\Param.json')
            json_array = json.load(file)
            param_list = []

            for item in json_array:
                param_details = {}
                param_details['workdays_per_week'] = item['workdays_per_week']
                param_details['version'] = item['version']        
                param_details['workhours_per_week'] = item['workhours_per_week']
                param_list.append(param_details)
            file.close()

            Functions.paramversion = param_details['version']
            Functions.paramworkdaysperweek = param_details['workdays_per_week']
            Functions.paramworkhoursperweek = param_details['workhours_per_week']


        except Exception as exc: 
            Functions.WriteLog(exc)



    def WriteSettingsToJson():
        try:
            file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\btwtwparam\\Param.json', "r")
            json_array = json.load(file)
            param_list = []

            for item in json_array:
                param_details = {}
                param_details['workdays_per_week'] = Functions.paramworkdaysperweek
                param_details['version'] = Functions.paramversion       
                param_details['workhours_per_week'] = Functions.paramworkhoursperweek
                param_list.append(param_details)
            file.close()

            file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\btwtwparam\\Param.json', "w")
            json.dump(param_list, file, indent=1, sort_keys=True)
            file.close()

        except Exception as exc: 
            Functions.WriteLog(exc)

    def WriteWorkhoursToJSON(date, totalworkedhours):
        try:
            file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\tmedta\\Data.JSON', "r")
            json_array = json.load(file)
            date_list = []

            for item in json_array:
                date_details = {}
                date_details['date'] = item['date']
                date_details['totalbreaktime'] = item['totalbreaktime']
                date_details['totalworkedhours'] = item['totalworkedhours']
                if date_details['date'] == date:
                     date_details['totalworkedhours'] = totalworkedhours

                date_list.append(date_details)
            print("JSON = \n\r       {0}".format(date_list))
            file.close()

            file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\tmedta\\Data.JSON', "w")
            json.dump(date_list, file, indent=1, sort_keys=True)
            file.close()

        except Exception as exc: 
            Functions.WriteLog(exc)



    def CalcAverageWorktime():
        averageleft = 0
        workeddays = (int)(Functions.paramworkdaysperweek) - Functions.totalworkeddays
        if workeddays < 0:
            workeddays = 0
        if workeddays != 0:
            averageleft = ((float)(Functions.paramworkhoursperweek) - (float)(Functions.totalworkedhours)) / (float)(workeddays)
        averageleft = round(averageleft,2)
        return averageleft
       

    def WriteLog(exc):
        logfile = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\Logfiles\\btwlog.txt',"a")
        dt = datetime.datetime.now()
        dtwithoutmill = dt.replace(microsecond=0)
        logfile.write("{0}".format(dtwithoutmill))
        logfile.write(": ")
        logfile.write("{0}".format(sys.exc_info()[0]))
        logfile.write(" -----> ")
        logfile.write("{0}".format(exc))
        logfile.write("\n\r")
        logfile.close()
        print(sys.exc_info()[0])
        print(exc)
