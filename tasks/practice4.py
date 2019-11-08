#!/usr/bin/python3

'''
Question 4: Given a string and an int n, remove characters
from string starting from zero up to n and return a new string

'''

def removeChars(text, num):
    if num > len(text):
        print(f"Number should be less that {len(text)}")
    else:
        print(f"Removing {num} number of chars")
        for i in range(0,num):
            print(text[i], end = "")
    print("\n")

removeChars("shridhar", 4)
