#!/usr/bin/python3
import time
thisdic = {
    "name" : "shridhar",
    "age" : "35",
    "year" : "1984"
}


print(thisdic)

x = thisdic["year"]
print(x)

y = thisdic.get("age")
print(y)

J = thisdic["year"] = 1715

print(J)

for j in thisdic:
    print(j, thisdic[j])
    time.sleep(1)

print(thisdic)

for x , y in thisdic.items():
    print("-> %s %s" %(x, y))

