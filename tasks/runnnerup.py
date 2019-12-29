#!/usr/bin/python3

'''
This script is created to find 2st runner up from the list of the results
2 9 5 3 8 9 7
'''

# solution1
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


# solution2

if __name__ == '__main__':
    #n = int(input())
    n = 5
    arr = map(int, input().split())
    sk = list(arr)
    for i in range(0,len(sk)):
        max_pos = i
        for k in range(i,len(sk)):
            if sk[max_pos] < sk[k]:
                max_pos = k

        temp = sk[i]
        sk[i] = sk[max_pos]
        sk[max_pos] = temp

for j in range(len(sk)):
    if max(sk) != sk[j]:
        print(sk[j])
        break
