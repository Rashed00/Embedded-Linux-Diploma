#!/usr/bin/python3
# dic = {
#     "vendor": "Mercedes",
#     "model": 2023,
#     "company": "valeo"
# }
# print(dic.get("model"))

############### Pass by value #############
# def fun(x):
#     x = 5
#     print(f"x inside function = {x}")  
#     print(id(x))  

# x = 10
# print(f"x outside function = {x}")
# print(id(x))  

# fun(x)

# print(f"x outside function = {x}")
# print(id(x)) 


############### Pass by ref ##############
# def fun(x):
#     x[0] = 5
#     print(f"x inside function = {x}")  
#     print(id(x))  


# x = [10]
# print(f"x outside function = {x}")
# print(id(x))

# fun(x)

# print(f"x outside function = {x}")
# print(id(x)) 


# class Person:
#     name = ""
#     def __init__(self,name):
#         print("Constructor is called")
#         print(self)
#         self.name = name
#         print(self.name)
        
#     def greeting(self):
#         print(f"hello {self.name}")
        
        
#     def __del__(self):
#         print("Destructor is called")
        
# ############ Inheritance #################
# class rashed(Person):
#     def __init__(self):
#         print("Hello from rashed class")
#         super().__init__("rashed")
        
#     def python(self):
#         print("You're shit")
    
#     def __del__(self):
#         print("end of rashed class")   
#         super().__del__()     
        
# rashed = rashed()
# rashed.greeting()
# rashed.python()


################# Operator overloading ############
# class Point():
#     def __init__(self,xCoord = 0,yCoord = 0 ):
#         self.xCoord = xCoord
#         self.yCoord = yCoord
        
        
#     #overload operator
#     def __add__(self, point_ov):
#         return Point(self.xCoord +  point_ov.xCoord , self.yCoord + point_ov.yCoord)
    
    
# point1 = Point(2,4)
# point2 = Point(3,8)
# point3 = point1 + point2

# print(point3.xCoord)
import os
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("it doesn't exist")
# f = open("file.txt",)
# print(f.read(5)) #return the first 5 characters in file


        
        
        