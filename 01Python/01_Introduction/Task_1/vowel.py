#!/usr/bin/python3

vowels = "AEOUIaeoui"
var = input("Please Enter a letter: ")
for i in range(0,10):
    if var == vowels[i]:
        print("Vowel")
        break
    elif i == 9:
        print("Consonant")        
