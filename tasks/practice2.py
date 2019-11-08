#!/usr/bin/python3

'''
Question 2: Given a range of numbers. Iterate from o^th
number to the end number and print the sum of the current
number and previous number
'''

PRV=0
for i in range(1,10):
    print(f"previous number {PRV}", end = " ")
    print(f"Current number {i}", end = " ")
    print(f"Sum of previous and current : {PRV + i}")
    PRV = i

nums = input("Please type any numbers : ")
arry = list(nums.split(","))


NN = 0

def prn(nums):
    global NN
    for i in arry:
        i = int(i)
        print(f"print Current number {i}", end = " ")
        print(f"print previous number {NN}", end = " ")
        print(f"print P and C sum : {NN + i}")
        NN = i

prn(nums)
print(NN)