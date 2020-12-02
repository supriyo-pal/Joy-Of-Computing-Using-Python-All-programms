# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 00:38:57 2020

@author: Supriyo
"""
'''
months before august:
    odd numbered months have 31 days 
    even numbered months have 30 days
months from august:
    odd numbered months have 30 days 
    even numbered months have 31 days
'''

from datetime import datetime as dt
import pytz
import calendar

# print(dt.now())

# tz=pytz.timezone('Singapore')
# print(dt.now(tz))

#print(len(pytz.all_timezones))

def check_for_leap(year):
    if year%100==0:
        if year%400==0:
            return True
        else:
            return False
    else:
        if year%4==0:
            return True
        else:
            return False


def check_valid_date(date,month,year,leap):
    if leap:
        if month==2:
            if date<30:
                return True
            else:
                return False
        else:
            if month<8:
                if month%2==1:
                    if date<32:
                        return True
                    else:
                        return False
                else:
                    if date<31:
                        return True
                    else:
                        return False
            else:
                 if month%2==0:
                    if date<32:
                        return True
                    else:
                        return False
                 else:
                    if date<31:
                        return True
                    else:
                        return False
    else:
        if month==2:
            if date<29:
                return True
            else:
                return False
        else:
            if month<8:
                if month%2==1:
                    if date<32:
                        return True
                    else:
                        return False
                else:
                    if date<31:
                        return True
                    else:
                        return False
            else:
                 if month%2==0:
                    if date<32:
                        return True
                    else:
                        return False
                 else:
                    if date<31:
                        return True
                    else:
                        return False

            

while (1):
    year=int(input("Enter Year :from 1970 "))
    if year<1970:
        print("Enter a valid year")
    else:
        break

while (1):
    month=int(input("Enter month :(1-12) "))
    if month<=12 and month>0:
       break
    else:
        print("Enter a valid Month (1-12)")

leap=check_for_leap(year)

while (1):
    date=int(input("Enter Date : "))
    if date>0 and check_valid_date(date,month,year,leap):
        break
    else:
        print("Enter a valid date")

fg=calendar.weekday(year,month,date)
print("\n The Day Is : ")
if fg==0:
    print("Monday")
elif fg==1:
    print("Tuesday")
elif fg==2:
    print("Wednesday")
elif fg==3:
    print("Thrusday")
elif fg==4:
    print("Friday")
elif fg==5:
    print("Saturday")
elif fg==6:
    print("Sunday")