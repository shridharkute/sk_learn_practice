#!/usr/bin/python3
import time

#list = [5,1,6,2,7,4,9,8,3]
list = [35,4,7,1,9,8,21,62,255,75,4,9,8,33]

def sort(list):
    for i in range(len(list)):
        #print(list[i])
        min_pos = i
        for j in range(i,len(list)):
            if list[j] < list[min_pos]:
                min_pos = j

        temp = list[i]
        list[i] = list[min_pos]
        list[min_pos] = temp


sort(list)
print(list)