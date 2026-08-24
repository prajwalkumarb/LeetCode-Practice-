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

def my_decorator(func):
    def wrapper_func():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper_func

def greet():
    print("Hello!")

def hello():
    print("Hi!")

greet = my_decorator(hello)  # manually wrapping
greet()