# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:46:28 2020

@author: Supriyo
"""

from datetime import datetime as dt
import pytz

time_zones=pytz.all_timezones

for i in range(len(time_zones)):
    zone=time_zones[i]
    tz=pytz.timezone(zone)
    print("Current time at",zone," is ",dt.now(tz),"\n")
