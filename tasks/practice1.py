#!/usr/bin/python3
'''
Question 1: Accept two int values from the user and
return their product. If the product is greater than 1000,
then return their sum

'''
x = int(input("Enter first number "))
y = int(input("Enter second number "))

PD = x * y

if PD > 1000:
    print(x+y)

