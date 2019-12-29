#!/usr/bin/python3

'''
This script is created to find 2st runner up from the list of the results
2 9 5 3 8 9 7
'''


if __name__ == '__main__':
    #n = int(input())
    n = 5
    arr = map(int, input().split())
    sk = list(arr)
    kk = max(sk)
    NEW = []
    for i in range(len(sk)):
        if sk[i] != kk:
            NEW.append(sk[i])

    print(f"{max(NEW)} is the runner up")

