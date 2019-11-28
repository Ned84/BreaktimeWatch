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


class Functions(object):
    time1 = datetime.now()
    time2 = datetime.now()
    total = 0

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

    def Stop():
        Functions.time2 = Functions.GetTime()
        Functions.CalcDiff()

    def CalcDiff(): 
        diff = Functions.time2 - Functions.time1
        Functions.total = Functions.total + diff.seconds
        print(diff)
        print(Functions.total)
        