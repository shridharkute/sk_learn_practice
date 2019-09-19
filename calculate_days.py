#!/usr/bin/python3
import datetime

#help(datetime)

print(datetime.__dir__())
A = datetime.date(2019, 8, 1)
B = datetime.date(2019, 9, 11)
year = B.year
month = B.month
day = B.day
print("A DATE - %d/%d/%d" %(A.day,A.month,A.year))
print("B DATE - %d/%d/%d" %(B.day,B.month,B.year))


days = B - A
print("by setting direct var - %d" % days.days)


''' This is second part just want to try with variable

 
'''
y, m, d = 2019, 9, 1
y1, m1, d1 = 2019, 11, 1
DT1 = datetime.date(y, m, d)
DT2 = datetime.date(y1, m1, d1)

DT3 = DT2 - DT1

print("using Var - %d" % DT3.days)