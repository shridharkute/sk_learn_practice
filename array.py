#!/usr/bin/python3
import time

car_co = ["maruti", "honda", "tata", "bajaj", "hero"]


def my_arr(list):
    for i in list:
        print(i)
        time.sleep(1)

my_arr(car_co)

x = car_co[0]

print("Total number of elements in array %d" %(len(car_co)))


car_co.append("volvo")
print(car_co)
car_co.pop(1)
print (car_co)
car_co.remove("volvo")
print(car_co)

print(car_co.index("bajaj"))