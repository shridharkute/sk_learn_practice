#!/usr/bin/python3

x = lambda a : a * 10

print(x(5))


y = lambda s,t,u : s + t + u

print(y(2,2,2))

def my_lab(n):
    return lambda r : r * n

D  = my_lab(5)
F  = my_lab(3)

print(D(2))
print(F(2))