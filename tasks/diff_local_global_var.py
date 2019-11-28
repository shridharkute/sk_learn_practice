#!/usr/bin/python3

'''
This snippet will show the behaviour of the global and local variable.


'''

# We have two array
kk = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
kk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# sum is globale variale
sum = 0

# Add funcation to add all values in array

def Add1(nums):
    global sum
    for i in nums:
        sum += i
        print(sum, end = " ")
    print("")

def Add2(nums):
    sum = 0
    for i in nums:
        sum += i
        print(sum, end = " ")
    print("")
'''
below execution will give
Add1(kk)
Add1(kk1)

output:
10 30 60 100 150 210 280 360 450 550 
551 553 556 560 565 571 578 586 595 605    # while execution of "Add1(kk1)" previous value of sum will be used,
previous value means 550 + 1, 551 + 2 ..... 

'''
Add1(kk)
Add1(kk1)

#=========================================================================

'''
below execution will give
Add2(kk)
Add2(kk1)

output:
10 30 60 100 150 210 280 360 450 550 
1 3 6 10 15 21 28 36 45 55                # This is expected output

'''
Add2(kk)
Add2(kk1)

