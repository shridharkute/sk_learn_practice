#!/usr/bin/python3
'''
This script is created to get the count of the substring in string.

Note: strings are case sensitive.

Eg.
Input:
ABCDCDC
CDC

Output:
2      # AS CDC is appeared twice in string "ABCDCDC"

'''

CNT = 0

def string_match(main_string, sub_string):
    print(main_string, len(main_string))
    print(sub_string, len(sub_string))
    for i in range(0,len(main_string)):
            JK = []
            if len(main_string) >= (i + len(sub_string)):
                global CNT
                for j in range(i, i + len(sub_string)):
                    JK.append(main_string[j])
                STR_SNIPET = "".join(JK)
                if STR_SNIPET == sub_string:
                    CNT += 1
    return CNT

#count = string_match("ABCDCDC", "CDC")
count = string_match("Shridharkutekaivalyakuteharshkute", "kute")
#print(f"Substring kute found {count} times in main string")
print(count)