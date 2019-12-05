#!/usr/bin/python3
import random

'''
Testing something

'''

USR_INPUT = int(input("Please type any fev number between 1-6 :"))



#print(random.__doc__)
#X = dir(random)
#print(X)

def jk():
    KK = random.randrange(1,7, step=1)
    if USR_INPUT == KK:
            print(f"Ye..... . Same to same user:{USR_INPUT} rand{KK}")
    else:
            print(f"Better luck next time user:{USR_INPUT} rand {KK}")



jk()


#help(random.randrange)

