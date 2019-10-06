#!/usr/bin/python3
import time
mydict = {
    "one" : {
    "name" : "shridhar",
    "age" : "35"
    },
    "two" : {
        "name" : "raghu",
        "age" : 30
    },

    "three" : {
        "name" : "Kavi",
        "age" : 5
    }
}


print(mydict)

kk1 = {
    "name" : "kk1",
    "age" : "1",
    "number" : 55
}


kk2 = {
    "name" : "kk2",
    "age" : "2",
    "number" : 56
}


kk3 = {
    "name" : "kk3",
    "age" : "3",
    "numer" : 57
}


my2dic = {
    "kk1" : kk1,
    "kk2" : kk2,
    "kk3" : kk3
}


print(my2dic)



print(len(mydict))

print(len(my2dic))



for i in mydict:
    print(i, end = " ")
    print(mydict[i])
    time.sleep(0.1)


for j in my2dic:
    print(j, end = " ")
    print(my2dic[j])
    time.sleep(0.1)

print(my2dic["kk1"])
print(my2dic["kk2"])
print(my2dic["kk3"])

print(mydict["one"])
print(mydict["two"])
print(mydict["three"])