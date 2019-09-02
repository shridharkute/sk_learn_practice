#!/usr/bin/python3
import time

list=[8,3,5,2,1,9,4,7,6]

def sort(list):
    for i in range(len(list)):
        min_pos = i
        for j in range(i,len(list)):
            if list[j] < list[min_pos]:
                min_pos = j

            temp = list[i]
            list[i] = list[min_pos]
            list[min_pos] = temp



print("Before sorting old list was\t: %s" % list)
sort(list)
print("After sorting new list is\t: %s" % list)
