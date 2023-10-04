#!/usr/bin/python3


# ls = [1.5, 1, "Rashed", [1.2,5],{1,2}]
# for i in ls:
#     print(type(i))
    
# tup = (1,"rashed",3.2)
# print(tup[0])
# print(type(tup))
# print(tup[0])

# x = int(input("please enter value:  "))
# print(x + 5)

# ls = ["Rashed",10,20,30,40,50]
# print(10>9)
# print(ls)

# thisdict = {
#     "Brand": "Ford",
#     "Electrical": False,
#     "Year": 2014,
#     "Color": ["Red","Blue","Black"],
#     "Email": "Prashed25594@gmail.com",  
#     "Email": "a.s.rashed03@gmail.com"   #this line overrite the previous key value
#                                         #otherwise on C++ it takes first key value and ignore the 2nd
# }

# print(type(thisdict))
# print(thisdict)
# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict["Brand"])
# print(len(thisdict))


# thisset = {"Rashed",3,8,1.9,3}
# print(type(thisset))
# print(thisset)
# print(list(range(1,10,2)))
# import time

# #Creating a list of numbers
# thislist = list(range(1,1000001))

# #Creating a set of numbers
# thisset = set(range(1,1000001))

# #Calculate time taken to find number in list
# Start_time = time.time()
# print(1000000 in thislist)
# End_time = time.time()
# print("Time taken to search in list:",End_time - Start_time, "Seconds")

# #Calculate time taken to find number in set
# Start_time = time.time()
# print(1000000 in thisset)
# End_time = time.time()
# print("Time taken to search in set:",End_time - Start_time, "Seconds")

# name = "Rashed"
# thislist = list(name)
# print(thislist)
# print(name)

# helloworld = '#include <iostream>\nint main()\n{\nstd::cout<<"Hello World!"<<std::endl;\nreturn 0;\n}'

# namecpp = input("Enter file name: ")
# fd = open(namecpp, "w+")
# fd.write(helloworld)
# fd.close()

# number = int(input("Please enter value:"))
# print(f"you enetered {number}")
# print("you enetered %d"%number)
# print("you enetered {}".format(number))


# x = 10
# if x == 10:
#     print("x = 10")
#     print("Don't do this again")
#     x = 1
# elif x == 1:
#     print("test")
# print("Space matters")

# i = 1 
# while i in range(0,5):
#     print(i)
#     i+=1


# for i in [1,3,4.3,"Rashed"]:
#     print(i)
#     print(type(i))

#Reverse String in python [C_Style]
# name = input("Please enter ur name: ")
# for i in range(len(name)):
#     i += 1
#     print(name[len(name) - i],end="")

#Reverse String in python [Python_Style]
# name = input("Enter your name: ")
# print(type(name))
# txt = name[::-1]
# print(txt)
    
# import datetime
# print(datetime.datetime.now())

# import pyfiglet
# result = pyfiglet.figlet_format("Rashed Elsayed")
# print(result)

# f = "RasHeD Elsayed"
# print(f.split())

# # f = "              RaSheD            ElSayEd            "
# print(f)

#Function
#Functions in python is defined using 'def' keyword

# def func(fname):
#     print("Hello "+str(fname))

# func("Rashed")

# def mul_fun(value = 0):
#     return 5*value

# print(mul_fun())


# def function(child1, child2, child3):
#     print("the kid name is "+str(child3))

# function(child2 = "Ahmed", child3 = "Mohamed", child1="Khaled")

# def print_country(country = "Egypt"):
#     print(country)

# print_country("USA")

# def function(*var):
#     print(var[0][3])
#     print(type(var))
# function([1,2,3,"Rashed"])


# import numpy as np
# import cv2
# import pyautogui
# import imutils
  
# take screenshot using pyautogui
# image = pyautogui.screenshot()
   
# since the pyautogui takes as a 
# PIL(pillow) and in RGB we need to 
# convert it to numpy array and BGR 
# so we can write it to the disk
# image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
   
# writing it to the disk using opencv
# cv2.imwrite("image.png", image)

# # # this time take a screenshot directly to disk
# # pyautogui.screenshot("straight_to_disk.png")
# # # we can then load our screenshot from disk in OpenCV format
# # image = cv2.imread("straight_to_disk.png")
# # cv2.imshow("Screenshot", imutils.resize(image, width=600))
# # cv2.waitKey(0)


# import subprocess

# subprocess.Popen(['gnome-screenshot','-w'])

import os
import subprocess

subprocess.run(['gnome-screenshot','-w'])
# os.system("gnome-screenshot -w")