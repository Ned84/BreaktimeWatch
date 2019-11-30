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

from datetime import datetime
import math
import _thread
import json
import os
import sys


class Functions(object):
    time1 = datetime.now()
    time2 = datetime.now()
    totalmin = 0
    totalsec = 0
    diffsec = 0
    selecteddate = datetime.now()


    def __init__():
        dt = datetime.now()
        dtwithoutmill = dt.replace(microsecond=0)
        Functions.total = dtwithoutmill

    def GetTime():
        dt = datetime.now()
        dtwithoutmill = dt.replace(microsecond=0)
        print(dtwithoutmill)
        return dtwithoutmill

    def Start():
        Functions.time1 = Functions.GetTime()
        daynow = datetime.now().strftime("%d-%m, %Y")
        Functions.GetTotalFromJson(daynow)


    def Stop():
        Functions.time2 = Functions.GetTime()
        Functions.CalcDiff()

        daynow = datetime.now().strftime("%d-%m, %Y")
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
            file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\TimeData\\Data.JSON', "r")
            json_array = json.load(file)
            date_list = []

            for item in json_array:
                date_details = {}
                date_details['date'] = item['date']
                date_details['totaltime'] = item['totaltime']
                if date_details['date'] == date:
                     date_details['totaltime'] = totalsec

                date_list.append(date_details)
            print("JSON = \n\r       {0}".format(date_list))
            file.close()

            file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\TimeData\\Data.JSON', "w")
            json.dump(date_list, file, indent=1, sort_keys=True)
            file.close()

        except Exception as exc: 
            Functions.WriteLog(exc)

    def GetTotalFromJson(date):
        try:
            file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\TimeData\\Data.JSON')
            json_array = json.load(file)
            date_list = []
            found = False

            for item in json_array:
                date_details = {}
                date_details['date'] = item['date']
                date_details['totaltime'] = item['totaltime']
                if date_details['date'] == date:
                    Functions.totalsec = date_details['totaltime']
                    Functions.totalmin = Functions.totalsec / 60
                    Functions.totalmin = math.floor(Functions.totalmin)
                    found = True
                date_list.append(date_details)
            file.close()

            if found == False:
                file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\TimeData\\Data.JSON', "w+")
                date_list.append({"date": date,"totaltime": 0})
                json.dump(date_list,file, indent=1, sort_keys=True)
                file.close()
                Functions.totalsec = 0
                Functions.totalmin = Functions.totalsec / 60
                Functions.totalmin = math.floor(Functions.totalmin)

        except Exception as exc: 
            Functions.WriteLog(exc)

    

    def WriteLog(exc):
        logfile = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\Logfiles\\btwlog.txt',"a")
        dt = datetime.now()
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