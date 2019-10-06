#/usr/bin/python3

a = int(input("Please type number :"))
b = int(input("Please type number :"))

if a < b:
    print("%d is smaller than %d" % (a,b))
elif a < b:
    print("%d is grater than %d" % (a,b))
else:
    print("%d is equal to %d" %(a,b))


if a < b or a == b:
    print("%d is smaller or equal to %d" %(a,b))
elif b < a or a == b:
    print("%d is smaller or equal to %d " %(b,a))
else:
    print("unknwon %d %d" %(a ,b))