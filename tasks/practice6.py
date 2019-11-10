#!/usr/bin/python3
'''
Question 6: Given a list of numbers, Iterate it and
print only those numbers which are divisible of 5
'''

# Solution 1
LST = input("Please type input:")
X = LST.split(",")

def DEV_5(list):
    print("Below numbers are dv=ivisible by \"5\"")
    for i in list:
        J = int(i)
        if (J % 5) == 0 :
            print(f"shridhar {J}")



DEV_5(X)
