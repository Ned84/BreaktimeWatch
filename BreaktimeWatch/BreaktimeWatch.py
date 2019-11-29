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


class Functions(object):
    time1 = datetime.now()
    time2 = datetime.now()
    totalmin = 0
    totalsec = 0
    processrunning = 0


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
        Functions.processrunning = 1

    def Stop():
        Functions.time2 = Functions.GetTime()
        if Functions.processrunning == 1:
            Functions.CalcDiff()
            Functions.processrunning = 0
        
    def CalcDiff(): 
        
        diff = Functions.time2 - Functions.time1       
        Functions.totalsec = Functions.totalsec + diff.seconds
        Functions.totalmin = Functions.totalsec / 60
        Functions.totalmin = math.floor(Functions.totalmin)
        print()
        print(diff)
        print(Functions.totalsec)
        print(Functions.totalmin)




















  

        