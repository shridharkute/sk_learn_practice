#!/usr/bin/python3

'''Question 3: Accept string from the user and display
only those characters which are present at an even index
'''


def kk(x):
    for r in range(0,len(x)):
        if (r % 2) == 0:
            print(f"index [{r}] {x[r]}")

x = str(input("Enter String: "))
print(f"Orginal String is {x}")

kk(x)


def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = input("Enter String ")
print("Orginal String is ", inputStr)

print("Printing only even index chars")
printEveIndexChar(inputStr)