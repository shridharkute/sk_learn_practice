#!/usr/bin/python3

'''
Question 5: Given a list of ints, return True if first 
and last number of a list is same


This script will run only with single digit input

'''

# Solution 1 - Which is not working with double  digit
# it will not working as expected with 12,1,2,3,4,5,12 input
X = list(input("Please supply imput list: "))

F = X[0]
L = X[-1]

if X[0] == X[-1]:
    print("the first and last number of list is saame")
    print("result is true")
    print(f"First {F} Last {L}")
else:
    print("result is false")


# Solution 2 - Which is also not working with double  digit
# it will not working as expected with 12,1,2,3,4,5,12 input
Y = list(input("Please supply imput list: "))

def F_and_L(numlist):
    F_NUM = numlist[0]
    L_NUM = numlist[-1]
    if F_NUM == L_NUM:
        return True
    else:
        return False



print("The first and last number of the a list is same")
print("Result is ", F_and_L(Y))


# Solution 3 # it is updated solution1 # it should work with double digit
# it will be working as expected with 12,1,2,3,4,5,12 input
X = list(input("Please supply imput list: ").split(","))

F = X[0]
L = X[-1]

if X[0] == X[-1]:
    print("the first and last number of list is saame")
    print("result is true")
    print(f"First {F} Last {L}")
else:
    print("result is false")
