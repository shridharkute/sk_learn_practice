#!/usr/bin/python3

'''
Question 10: Given a two list of ints create a third list such that should contain
only odd numbers from the first list and even numbers from the second list
listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

output:
Merged List is
[23, 11, 17, 24, 36, 12]

'''

listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

# Solution1
def get_odd(list):
    ODD = []
    for i in list:
        if (i % 2) != 0:
            ODD.append(i)
    return ODD

def get_even(list):
    EVEN = []
    for i in list:
        if (i % 2) == 0:
            EVEN.append(i)
    return EVEN

ODD_FIST = get_odd(listOne)
EVEN_FIST = get_even(listTwo)

Mrged = ODD_FIST + EVEN_FIST
print(f"Mearged list is\n{Mrged}")



# Solution 2
def get_sorted(listOne, listTwo):
    third_list = []
    for i in listOne:
        if (i % 2) != 0:
            third_list.append(i)

    for j in listTwo:
        if (j % 2) == 0:
            third_list.append(j)
    return third_list

MIRGED = get_sorted(listOne, listTwo)

print(f"Merged List is\n{MIRGED}")

print(f"Merged List is \n{get_sorted(listOne, listTwo)}")