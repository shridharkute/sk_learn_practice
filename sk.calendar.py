#!/usr/bin/python3


import calendar


print(calendar.__dir__())


print("Monday %d" % calendar.MONDAY)
print("Tuesday %d" % calendar.TUESDAY)
print("Wednesday %d"  % calendar.WEDNESDAY)
print("Thursday %d" % calendar.THURSDAY)
print("Friday %d" % calendar.FRIDAY)
print("Saturday %d" % calendar.SATURDAY)
print("Sunday %d" % calendar.SUNDAY)
#help(calendar.WEDNESDAY)

print(calendar.month(2019, 9))






#help(calendar.calendar)
print(calendar.calendar(2019, c = 12, m = 4))
help(calendar.leapdays(2001, 2020))
#mama = calendar.isleap(year=2016)
mama = calendar.leapdays(2017, 2020)
print(mama)