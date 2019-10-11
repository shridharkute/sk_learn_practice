#!/usr/bin/python3


def my_fun(name = "kaliya"):
    print(name + " kute")


my_fun("ram")
my_fun("shidhar")
my_fun("anil")
my_fun()


def my_country(country = "India"):
    print("%s is my country" % country )


my_country("india")
my_country("mumbai")


def my_fev(food):
    for i in food:
        print("%s is my frevrate fruits" % i, end = " -> ")
        kk = "{} is my frevrate fruits"  # We can also print like this
        print(kk.format(i))


fruits = [ "mango", "apple", "banana", "cherry"]
food =  fruits

my_fev(food)


# How to get number of arguments passed in funcation

def my_funck(*kids):
    KK = len(kids) - 1
    print("The youngest child is " + kids[KK])
    print(my_funck.__name__)


my_funck("one", "two", "three", "four", "five")

import sys

def whoami():
    return sys._getframe(1).f_code.co_name

def func1():
    print(whoami())

func1()

exit(10) # We can set exit code using exit() method
