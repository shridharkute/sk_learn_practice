#!/usr/bin/python3
import module
import module as  MD
import platform

'''
This function was created to practice using module
'''
module.mywish("shridhar")
module.mywish("shri")
module.mywish("kavi")
module.mywish("harsha")
MD.mywish("MD shridhar")
MD.mywish("MD shri")
MD.mywish("MD kavi")
MD.mywish("MD harsha")


a_name = module.person1["Name"]
a_age = module.person1["Age"]
a_country = module.person1["Country"]

print("my name is %s"   %a_name)
print("my age is %d"  %a_age)
print("my Country is %s" %  a_country)


X = platform.system()
Y = platform.release()
print(X)
print(Y)

print(dir(platform))

