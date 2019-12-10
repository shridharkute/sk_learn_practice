#!/usr/bin/python3
'''
This script is created to learn dictionary
how to use full dictionary
how to use one part of the it
how to use one key value from one element

'''
myd = {
    "kid1" : {
        "name" : "shri",
        "age" : 35
    },
    "kid2" : {
        "name" : "Kavi",
        "age" : 5
    }
}

# use below code to use full dictionary
print(myd)

# use below code to use only kid2 key and values
print(myd["kid2"])

# use below code to use only one element from kid2 like we are using name from kid2
JK = myd["kid2"]

print(JK["name"])
