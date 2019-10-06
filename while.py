#!/usr/bin/python3
import time
a = 1
while a < 101 :
    time.sleep(0.1)
    if a == 12:
        a += 1
        continue
    print(a)
    a += 1

a = 0
while a <  101:
    print(a)
    a += 1
    if  a == 51:
        break
    time.sleep(0.2)