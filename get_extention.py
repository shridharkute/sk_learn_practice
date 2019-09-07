#!/usr/bin/python3

# accept file name as input and print file extention.

File_name=input("please type file name: ")

File_ext=File_name.split(".")

print("File extenction is : %s" % File_ext[1])