#!/usr/bin/python3
import time

'''
Question 7: Return the number of times that the string
“Emma” appears anywhere in the given string
'''

# Solution1
statement = str ("Emma is a good developer. Emma is also a writer")
K = statement.split(" ")
def str_count(stat):
    COUNT = 0
    for i in stat:
        #print(f"i- {i}")
        time.sleep(0.1)
        if i == "Emma":
            COUNT += 1
    print(f"Emma appeared {COUNT} times")


str_count(K)


# Solution2
def count_jhon(statement):
  count = 0
  for i in range(len(statement)-1):
    count += statement[i:i+4] == 'Emma'
  return count

count = count_jhon("Emma is good developer. Emma is aslo a writer")
print("Emma appeared ", count, "times")
