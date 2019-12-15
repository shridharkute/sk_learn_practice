#!/usr/bin/python3
'''
This cript s created to find "Fibonacci number"
first 5 Fibonacci number means
= ( 0 + 1 ) = 1
= ( 1 + 1 ) = 2
= ( 2 + 1 ) = 3
= ( 3 + 2) = 5
= ( 5 + 3 ) = 8

0  1 1 2 3 5 8 13 21 34 55 89 etc..
'''

def fibonacci(n):
    TTL = 0
    PV = 0
    J = []
    for i in range(0,n+1):
        if i == 0:
            TTL = PV + TTL
            PV = 0
            J.append(TTL)
        elif i == 1:
            TTL = PV + i
            PV = 0
            J.append(TTL)
        else:
            TTL = PV + TTL
            PV = TTL - PV
            J.append(TTL)
    return J

S = fibonacci(5)

print(S)

for k in S:
    print(k**3, end= " ")