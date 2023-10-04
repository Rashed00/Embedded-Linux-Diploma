#!/usr/bin/python3
################ String methods ####################
# age = 24
# txt = "My name is Rashed, and I am {}"  
# print(txt.format(age))


# ls = ["Hey","I","am","Rashed"]
# print(" ".join(ls))

# a = "hey"
# print(a * 5)

# x = 10 
# print("Welcome num: "+str(x)+" hello")
# print(f"Welcome num: {x} hello")

################# Functions ######################
#in python functions are defined using def keyword
# def function(name):
#     print("Hello from function,"+str(name))
    
# function("Gumball")

# def function(x):
#     return x * 5
# print(function(8))


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

################ Quick Task ######################
#Find the largest item from a given list using loop
# list1 = [9,92,48,1,201,3]
# list1.sort()
# print("Largest value = ",list1[-1])
# print("Largest value = ",max(list1))


#Write code to find automatically bitcoin rate
# import requests

# url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# if url.status_code == 200:
#     print(url.json()['bpi']['USD'])

############## Lab ######################
# Add keyboard shortcuts
# import keyboard
# import  subprocess

# def on_triggered():
#     subprocess.run(['nautilus','/home/rashed/Documents/Python'])
    
# def listen_to_shortcut():
#     shortcut = "ctrl + alt + s"
#     keyboard.add_hotkey(shortcut, on_triggered)
#     keyboard.wait()

# listen_to_shortcut()


# file containing a set of functions you want to include in your application.
# import util
# print(util.mult(3,8))


#modules inside folder
# import mylib.greeting
# mylib.greeting.hey()

# import importlib
# print("Location of python as module source: ")
# print(importlib.import_module('os'))

# ls = ['rashed', 5 , 'ahmed', 8 , 9.1, [0,'cat'],101010]
# ls.insert(0,"I am")
# print(ls)

