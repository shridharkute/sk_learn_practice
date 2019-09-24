#!/usr/bin/python3
import time

a =  "Hello World"

print(a)
print(a.split(" "))
print(a.split(" ")[0])
print(a.split(" ")[1])

F = open("/tmp/syslog")


help(F.readline)

for i in range(1,14):
    print(i, F.readline(-i))
    time.sleep(0.1)



F.close()


