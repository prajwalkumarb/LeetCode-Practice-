# x = 256
# y = 256
# print(x is y)  # True (Shared memory address)

# a = 259
# b = 259
# print(a is b)  # False (Different memory addresses)

# print(id(a) == id(b))
# print(id(a), id(b))

# ############################################################################################################################

# # Shallow Copy vs Deep Copy
# import copy

# original = [[1, 2], [3, 4]]

# shallow = copy.copy(original)       # New list, but inner lists are shared
# deep    = copy.deepcopy(original)   # Fully independent copy

# shallow[0].append(99)
# print(original)   # [[1, 2, 99], [3, 4]] ← affected!

# deep[0].append(99)
# print(original)   # [[1, 2, 99], [3, 4]] ← NOT affected

# #########################################################################################################################



# Class inetialization and constructor example
# class MyClass:
#     def __init__(self, age,name):
#         print("Constructor called")
#         self.age = age
#         self.name = name
#         print("Object created with age:", self.age, "and name:", self.name)

# if __name__ == "__main__":
#     obj1 = MyClass(25, "Prajwal")
#     print("Age in obj1:", obj1.age)
#     print("Name in obj1:", obj1.name)
    
    

# 1. What is a Decorator?
# A decorator is just a function that wraps another function to add behavior before/after it — without modifying the original function.
# The key insight: functions are first-class objects in Python — they can be passed around, assigned to variables, and returned from other functions.

# def my_decorator(func):
#     def wrapper_func():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper_func

# def greet():
#     print("Hello!")

# def hello():
#     print("Hi!")

# greet = my_decorator(hello)  # manually wrapping
# greet()

# _____________________________________________________________

# for i, name in enumerate(["ann","bob"],start=1):
#     print(i,name)
    
# for name, age in zip(["ann","bob"],[25,35]):
#     print(name,age)
    
    
# def process_command(command):
#     match command.split():
#         case ["quit",exiting]:
#             print(f"Goodbye! {exiting}")
#         case ["go", direction]:
#             print(f"Moving towards the {direction}")
#         case ["teleport", x, y]:
#             print(f"Blinking to coordinates: {x}, {y}")
#         case _:
#             print("Command not recognized.")

# process_command("quit immediately")
# process_command("go east")
# process_command("teleport 100 200")

# _____________________________________________________________

# function and Arguments

# def demo(a,b,*args,**kwargs,):
#     print(a,b)
#     print(args)
#     print(kwargs)

# demo(1,2,3,4,5,x=6,y=7,z=8,c=9)

# def add(x,y,z):
#     return x + y + z

# print(add(1,2,3))
# num1 = (1,2,3)
# print(add(*num1))
# num2 = [1,2,3]
# print(add(*num2))
# num2 = {"x":1,"y":2,"z":3}
# print(add(**num2))


# lambda

# number = [1,2,3,4]
# soll = list(filter(lambda x: x + 1 == 5,number))
# print(soll)

# square = list(map(lambda x: x * x , number))
# print(square)

# people = [("ann",30),("bob",10),("charlie",50)]
# people.sort(key=lambda person: person[1])
# print(people)

# from functools import reduce
# reduce_data = reduce(lambda a,b :a * b, number)
# print(reduce_data)

# -----------------------------------------------------------------------------------



# Class and Object
# class Person:
    
#     def __init__(self,name,age):
#         self.name = "Prajwal"
#         self.age = 23
    
#     def get_name(self,name):
#         print(f"Name is {self.name}")
    
#     def get_age(self,age):
#         print(f"Age is {self.age}")
    
# class_data = Person("charan",23)
# get_name = class_data.get_name("Prajwal")
# get_age = class_data.get_age(25)

# class Student:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def get_name(self):
#         print(f"Student name is {self.name}")
    
#     def get_age(self):
#         print(f"Student age is {self.age}")
    
# class_data = Student("Prajwal",23)
# get_name = class_data.get_name()    
# get_age = class_data.get_age()
# ---------------------------------------------------------------------



# # Instance, class, static method

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     @classmethod
#     def from_birth_year(cls,name,year):
#         return cls(name,2026 - year)

#     @staticmethod
#     def is_adult(age):
#         return age > 18

# data = person.from_birth_year("Prajwal",2002)
# print(data.name,data.age)

# print(person.is_adult(data.age))


# import json

# class jsonmixin:
#     def to_json(self):
#         return json.dumps(self.__dict__)
    
# class User(jsonmixin):
#     def __init__(self,name):
#         self.name = name

# print(User("Prajwal").to_json())


# class PDFReport:
#     def render(self): return "PDF"

# class HTMLReport: 
#     def render(self): return "HTML"

# for report in [PDFReport(),HTMLReport()]:
#     print(report.render())
    


# Generator

# def count_up_to(number):
#     count=1
#     while count <= number:
#         yield count
#         print(">>>>>>",count)
#         count += 1

# for i in count_up_to(5):
#     print(i)
    
# def number():
#     yield from range(1,6)

# def squares(seq):
#     for n in seq:
#         yield n * n

# data = squares(number())
# print(list(data))

# def fun(m):
#     for i in range(m):
#         yield i

# for n in fun(3):
#     print(n, end=" ")
    
    
# closures

# def make_multiplier(n):
#     def multiplier(x):
#         return x * n
#     return multiplier

# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(5))
# print(triple(5))


# def sample_text(text):
#     def print_world(world):
#         return f"{text} {world}"
#     return print_world

# print(sample_text("Hello")("World"))


# Decorators

# import functools
# def log_calls(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print(f"Function , {func.__name__} with argument {args}, {kwargs}")
#         result = func(*args,**kwargs)
#         print("<><><><> Result",result)
#         return result
#     return wrapper

# @log_calls
# def add( a, b, i = 90):
#     return a + b

# add(10,20)
# print(add.__name__)

# Docoratory with argument

# def count(length = 6):
#     def decorator(funct):
#         def countdown(*args,**kwargs):
#             print("<><><><>",args,kwargs)
#             for i in range(length):
#                 print(i)
#             funct()
#         return countdown
#     return decorator

# @count(length=10)
# def count_down():
#     print("Verifyed")
    

# count_down()



# -----------------------------------------------------------------------
# Shallow copy and deep copy

import copy
original = [[1,2],[3,4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

print("\noriginal",original)
print("shallow",shallow)
print("deep",deep)

shallow[0].append(99)

print("\noriginal",original)
print("shallow",shallow)
print("deep",deep)

shallow.append([5,6])
print("\noriginal",original)
print("shallow",shallow)
print("deep",deep)