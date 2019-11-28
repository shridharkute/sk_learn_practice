#!/usr/bin/python3

'''
Question 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

'''

# Solution1
KK = int(input("Please type any number under 9 :"))

def nu_prin():
    for i in range(1,KK + 1):
        for j in range(0,i):
            print(f"{i} ", end = " ")
        print("")

nu_prin()

# Solution2
for num in range(10):
    for i in range(num):
        print (num , end=" ") #print number
    # new line after each row to display pattern correctly
    print("")
