#!/usr/bin/python3
import json

# Test data in jason format
J = '{"name" : "shri", "age" : 35, "place" : "mumbai"}'

# below part is dictionary
K = {"name" : "shri", "age" : 35, "place" : "mumbai"}

Y = json.loads(J)
print(Y["name"])
print(Y["age"])
print(Y["place"])

# how to use dictionary data
print(K["name"])

print(json.__dir__())
print(help(json.loads))

globals()