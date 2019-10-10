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

exit(10) # We can set exit code using exit() method
