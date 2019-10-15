#!/usr/bin/python3

class myparents:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printname(self):
        print(self.name, self.age)

X = myparents("shridhar", 35)

X.printname()
