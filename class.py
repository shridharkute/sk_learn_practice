#!/usr/bin/python3

import time
class mycls():
    x = 5
    y = 3
    z = 2

s = mycls.x
print(s)
print(mycls.x)
print(mycls.z)
print(mycls.x)

class myclass():
    def __init__(self, name, age):
        self.name  = name
        self.age = age

S = myclass("shridhar", 35)
R = myclass("Kaivalya", 4)
H = myclass("harsh", 5)

for j in (S, R, H):
    print(j.name, j.age)



class person:
    def __init__(kaka, name , age):
        kaka.name = name
        kaka.age = age

    def my_func(mama):
        print("This is my name " + mama.name,"and age is ", mama.age)


P1 = person("john", 20)
P1.my_func()
del P1
print(P1)