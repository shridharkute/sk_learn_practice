#!/usr/bin/python3

# Global variable x
x = 300
print("Golbal variabe\t\t\t:%d"%x)

# define same in funcaton

def myfunc():
    print("Global used in funtion\t:%d" % x)

myfunc()

# now define x in side funcation
def my2ndfunc():
    x = 200
    print("In side my2ndfunc\t\t:%d" %x)

my2ndfunc()

# Global keyword is used to set global variable from inside of the function
def my3rdfunc():
    global  x
    x = 400
    print("In side my3rdfunc\t\t:%d" %x)


my3rdfunc()

print("Finale x value out side of the funcation: %d" % x)