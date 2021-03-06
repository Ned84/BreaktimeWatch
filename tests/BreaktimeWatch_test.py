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

class InitClass(object):
    def testInit():
        dt = datetime.now()
        dtwithoutmill = dt.replace(microsecond=0)
        TestFunctions.total = dtwithoutmill


class TestFunctions(object):
    time1 = datetime.now()
    time2 = datetime.now()
    totalmin = 0
    totalsec = 0
    diffsec = 0
    selecteddate = ""
    totalworkedhours = 0
    totalworkeddays = 0
    workedhoursatdate = 0.0

    def test_GetTime(self):
        dt = datetime.now()
        dtwithoutmill = dt.replace(microsecond=0)
        print(dtwithoutmill)
        return dtwithoutmill

    def test_Start(self):
        InitClass.testInit()
        TestFunctions.time1 = TestFunctions.test_GetTime(self)
        daynow = datetime.now().strftime("%d-%m, %Y")
        TestFunctions.test_GetTotalFromJson(daynow)


    def test_Stop(self):
        TestFunctions.time2 = TestFunctions.test_GetTime(self)
        TestFunctions.test_CalcDiff(self)

        date = datetime.now().strftime("%d-%m, %Y")
        TestFunctions.test_WriteTimeToJson(self)

        
    def test_CalcDiff(self): 
        try:
            diff = TestFunctions.time2 - TestFunctions.time1   
            TestFunctions.totalsec = TestFunctions.totalsec + diff.seconds
            TestFunctions.totalmin = TestFunctions.totalsec / 60
            TestFunctions.totalmin = math.floor(TestFunctions.totalmin)
            print()   
            print("diff = {0}".format(diff))
            print("totalsec = {0}".format(TestFunctions.totalsec))
            print("totalmin = {0}".format(TestFunctions.totalmin))
        except Exception as exc: 
            TestFunctions.test_WriteLog(exc)

    def test_WriteTimeToJson(self):
        try:
            date = 0
            totalsec = 0
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
            TestFunctions.test_WriteLog(exc)

    def test_GetTotalFromJson(date):
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
                    TestFunctions.totalsec = date_details['totaltime']
                    TestFunctions.totalmin = TestFunctions.totalsec / 60
                    TestFunctions.totalmin = math.floor(TestFunctions.totalmin)
                    found = True
                date_list.append(date_details)
            file.close()

            if found == False:
                file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\TimeData\\Data.JSON', "w+")
                date_list.append({"date": date,"totaltime": 0})
                json.dump(date_list,file, indent=1, sort_keys=True)
                file.close()
                TestFunctions.totalsec = 0
                TestFunctions.totalmin = TestFunctions.totalsec / 60
                TestFunctions.totalmin = math.floor(TestFunctions.totalmin)

        except Exception as exc: 
            TestFunctions.test_WriteLog(exc)

    paramversion = ""
    paramworkdaysperweek = 0
    paramworkhoursperweek = 0

    def test_GetSettingsFromJson(self):
    
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
            TestFunctions.test_WriteLog(exc)



    def test_WriteSettingsToJson(self):
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
            TestFunctions.test_WriteLog(exc)

    def test_WriteWorkhoursToJSON(self):
        try:
            date = 0
            totalworkedhours = 0
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
            TestFunctions.test_WriteLog(exc)



    def test_CalcAverageWorktime(self):
        averageleft = 0
        workeddays = (int)(TestFunctions.paramworkdaysperweek) - TestFunctions.totalworkeddays
        if workeddays < 0:
            workeddays = 0
        if workeddays != 0:
            averageleft = ((float)(TestFunctions.paramworkhoursperweek) - (float)(TestFunctions.totalworkedhours)) / (float)(workeddays)
        averageleft = round(averageleft,2)
        if averageleft < 0:
            averageleft = 0
        return averageleft

    

    def test_WriteLog(exc):
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