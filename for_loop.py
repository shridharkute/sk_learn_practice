#!/usr/bin/python3  
import time

def f_loop(nu):
    for i in range(0,nu):
        print(f"This is for shri {i}")
        time.sleep(2)

f_loop(10)

f_loop(5)

