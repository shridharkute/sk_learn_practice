#!/usr/bin/python3
import time
mytuple = ("shri", "kavi", "harsha")

myit = iter(mytuple)

print(next(myit))
time.sleep(1)
print(next(myit))
time.sleep(1)
print(next(myit))
time.sleep(1)

mystr = "shridhar"
myitr = iter(mystr)


print(next(myitr))
print(next(myitr))1754/









































print(next(myitr))
print(next(myitr))



for i in mytuple:
    print(i)

for x in mystr:
    print(x)

mystr = "Shridharkaviharsharamshri"

myitr = iter(mystr)

JK = len(mystr)

for i in range(1, len(mystr)):
    print(next(myitr))
    time.sleep(0.1)

