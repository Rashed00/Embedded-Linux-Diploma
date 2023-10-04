#!/usr/bin/python3

#Write a Python program to count the number of lines in a text file.
f = open("file.txt", 'r')
lst = f.read()
print(len(lst))

