#!/usr/bin/env python

"""
DESCRIPTION:
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
"""

def make_readable(seconds):
    # Do something
    timestamp = ""
    
    if seconds < 60:
        timestamp = "00:00:{:02d}".format(seconds)
        
    if seconds <= 3599:        
        minutes  = seconds//60
        spillage = seconds%60
        
        timestamp = "00:{:02d}:{:02d}".format(minutes,spillage)

    # 359999
    else:
        hours   = seconds//3600
        # print('hours: ',hours)
        minutes = (seconds-(hours*3600))//60
        # print('minutes: ',minutes)
        spillage = seconds - (hours*3600) - (minutes*60)
        timestamp = "{:02d}:{:02d}:{:02d}".format(hours,minutes,spillage)

    return timestamp
        
print(make_readable(1))
print(make_readable(610))
print(make_readable(6100))

"""
Optimal Solution:

def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
"""