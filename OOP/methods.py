
# _________________________________________Class methods and Static methods___________________

# Class Method:

# A class method is a method that is bound to the class rather than the object instance. 
# This means it can be called on the class itself or on any instance of the class.
# Class methods are defined using the @classmethod decorator.
# The first parameter of a class method is conventionally named cls, which refers to the class itself. 
# This parameter allows the method to access and modify class-level variables and call other class methods.
# Class methods are commonly used for factory methods or methods that need to operate on class-level data.

# class Student:
#     students_school = 'Royal'

#     @classmethod
#     def school(cls):
#         if cls.students_school == 'Royal':
#             print(f'Every student,s school name is: {cls.students_school}')

# id1 = Student()
# Student.school()
# # id1.school()


# Static Method:

# A static method is a method that is not bound to either the class or the object instance. 
# It behaves like a regular function but is defined within the scope of a class for organizational purposes.
# Static methods are defined using the @staticmethod decorator.
# Unlike instance methods or class methods, static methods do not have access to 
# instance variables (self) or class variables (cls). They operate only on the arguments passed to them.
# Static methods are commonly used when the functionality of a method does not depend 
# on the state of the object or class and does not need access to instance or class variables.

# class Fruits:
#     def __init__(self,name,colour) -> None:
#         self.name = name
#         self.colour = colour

 # We cannot use instance attribute or class attribute in static method
#     @staticmethod
#     def fruits_name(*args):
#         for element in args:
#             print(element,)

# id1 = Fruits('Mango','Yellow')
# id1.fruits_name('Banana','Pineapple','Mango')



# ________________________________________Magic Methods______________________________________


# Magic methods, also known as dunder methods (short for "double underscore"), 
# are special methods in Python that allow objects to perform various operations 
# with built-in functions or operators. These methods are identified by their names 
# surrounded by double underscores, such as __init__() or __str__(). They enable the 
# implementation of operator overloading, customization of behavior, and enable the 
# creation of user-defined classes that emulate built-in types

# Here's a brief overview of some commonly used magic methods:

# __init__(self, ...): 
# This method is called when an object is initialized. 
# It's used to initialize instance variables or perform any setup necessary for the object.

# __repr__(self): 
# This method returns a string representation of the object. 
# It's typically used for debugging or logging purposes. 
# When possible, eval(repr(obj)) == obj should be true.

# __str__(self): 
# This method returns a string representation of the object. 
# It's meant to be readable and is typically used for displaying information to end-users.

# __len__(self): 
# This method returns the length of the object when the len() function is called on it.

# __getitem__(self, key): 
# This method allows the object to support indexing. It's invoked when an item 
# is accessed using square brackets ([]).

# __setitem__(self, key, value): 
# This method allows the object to support item assignment. 
# It's invoked when an item is assigned a value using square brackets ([]).

# __delitem__(self, key): 
# This method allows the object to support item deletion. 
# It's invoked when an item is deleted using the del statement.

# __iter__(self): 
# This method returns an iterator object that can be used to iterate over the elements of the object.

# __next__(self): 
# This method is used in conjunction with __iter__() to iterate over the elements of the object. 
# It returns the next item in the iteration.

# __contains__(self, item): 
# This method allows the object to support the in operator. 
# It's invoked when the in operator is used to check for membership.

# __eq__(self, other): 
# This method defines the behavior of the equality operator (==) for objects of the class.

# __lt__(self, other), __le__(self, other), __gt__(self, other), __ge__(self, other): 
# These methods define the behavior of comparison operators (<, <=, >, >=) for objects of the class.

# __add__(self, other), __sub__(self, other), __mul__(self, other), __truediv__(self, other): 
# These methods define the behavior of arithmetic operators (+, -, *, /) for objects of the class.