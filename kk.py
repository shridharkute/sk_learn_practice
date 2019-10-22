#!/usr/bin/python3
# Temp test
import time

'''
 this is created for tem test
'''
x = 300
def myfun():
    global x
    x = 200 
    def mychild():
        print(x)
    mychild()

myfun()

print(x)