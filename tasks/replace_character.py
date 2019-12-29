#!/usr/bin/python3
'''
This script is created to change specific character in string
eg.

to change 5th character in string "shridhar" we can run this script

OUTPUT:
Please type string : shridhar
Specify the character position that you want to change and character "," seprated : 5,c
shridcar



'''
def mutate_string(string, position, character):
    JK= []
    L = list(string)
    for i in range(0,len(L)):
        if i == position:
            L[i] = character
        JK.append(L[i])
    #return JK
    return "".join(JK)

if __name__ == '__main__':
    s = input("Please type string : ")
    i, c = input("Specify the character possion that you waant to change and character \",\" seprated : ").split(",")
    s_new = mutate_string(s, int(i), c)
    print(s_new)


