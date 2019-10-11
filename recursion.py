#!/usr/bin/python3

'''
This is recursion example.
recursion is method to call itself while running.
Below is the example which will create addition till we get 1.
Eg.
If we below funcation as "tri_resolution(6)" the result will be

Rcursion example result
1 1
2 3
3 6
4 10
5 15
6 21

But in the background it will execute below code.

>>> 6 + 5 + 4 + 3 + 2 + 1
21
>>> 5 + 4 + 3 + 2 + 1
15
>>> 4 + 3 + 2 + 1
10
>>> 3 + 2 + 1
6
>>> 2 + 1
3
>>> 1
1
>>> 



'''
def tri_resolution(k):
    if (k>0):
        result = k+tri_resolution(k-1)
        print(k, result)
    else:
        result = 0
    return result


print("\n\nRcursion example result")

tri_resolution(6)



