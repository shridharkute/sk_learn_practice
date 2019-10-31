#!/usr/bin/python3

import datetime
x = datetime.__dir__()

SS =  datetime.datetime.now()


print("Date : %d , Month : %d , Year : %d" %(SS.day, SS.month, SS.year))

print(SS.strftime("%A"))

y = datetime.datetime(2019, 10, 29)
print(y.day, end = "/")
print(y.month, end = "/")
print(y.year)