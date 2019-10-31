#!/usr/bin/python3
import json

# Test data in jason format
J = '{"name" : "shri", "age" : 35, "place" : "mumbai"}'

Y = json.loads(J)
print(Y["age"])
