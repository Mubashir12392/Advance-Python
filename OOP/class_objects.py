
# _____________________________________ Syntax_________________________


# class Student:      #class

#     #class Attribute
#     school = 'Royal_Education_Complex'
#     def __init__(self,name,age,course):   # Dunder method (Class initializer)
        
#         # Instance attributes
#         self.name = name
#         self.age = age
#         self.course = course

# # Create an object(Instance) and save it in variable id1
# id1 = Student('Mubashir',20,'BSCS')

# # Use object as you want
# print(id1.school)


# _____________________________________Theory_________________________________

# Class:

# A class is a blueprint for creating objects (instances) that share common attributes and behaviors.
# It defines the structure and behavior of objects by encapsulating data (attributes) 
# and methods (functions).
# Classes are defined using the class keyword followed by the class name and a colon.


# Object (Instance):
# An object (also called an instance) is a concrete realization of a class.
# It represents a specific entity or instance of a particular class.
# Objects have their own identity, state (attributes), 
# and behavior (methods), as defined by their class.
# Objects are created by calling the class constructor using the class_name() syntax.


# __init__ Function:
# The __init__ method (initializer or constructor) is a special method in 
# Python classes that is automatically called when a new instance of the class is created.
# It is used to initialize the attributes of the newly created object.
# The self parameter refers to the instance itself and is used to access 
# instance attributes and methods within the class.


# __str__ Function:
# The __str__ method is a special method in Python classes that is used to define 
# the string representation of an object.
# It returns a string representation of the object, 
# which can be customized to provide meaningful information about the object's state.
# When an object is passed to the print() function or used in 
# string formatting, Python calls its __str__ method to convert it to a string.


# Instance Methods:
# Instance methods are functions defined within a class that 
# operate on instances of the class.
# They are called with the instance itself (i.e., self) as the 
# first argument and can access and modify instance attributes.
# Instance methods are defined using the def keyword within the 
# class definition and can be called on instances of the class.


# Instance Attributes:
# Instance attributes are variables associated with a specific instance of a class.
# They represent the state of individual objects and are unique to each instance.
# Instance attributes are initialized within the __init__ method using the self parameter.


# Class Attributes:
# Class attributes are variables associated with a class rather than instances of the class.
# They are shared among all instances of the class and are accessed using the class name.
# Class attributes are typically defined outside of any method within the class definition.


# self Parameter:
# The self parameter is a reference to the current instance of the class and 
# is passed as the first parameter to instance methods.
# It allows instance methods to access and modify instance attributes and 
# call other instance methods within the class.
# While self is a convention, you can use any name for the first parameter 
# of instance methods, although it's best practice to stick with self for readability.


# _______________________________STR Method__________________

# class Teachers:
#     def __init__(self,name,age,subject) -> None:
#         self.name = name
#         self.age = age
#         self.subject = subject
    
#     def __str__(self) -> str:
#         return f'Name:{self.name}, Age:{self.age}, Subject:{self.subject}'

# id1 = Teachers('Uzma',34,'History')
# print(id1)

# __________________________instance methods_________________________

# class Cars:
#     def __init__(self,name,companyname,modelyear) -> None:
#         self.name = name
#         self.companyname = companyname
#         self.modelyear = modelyear
    
#     def my_func(self):
#         return self.modelyear *2
    
# car1 = Cars('Corolla','Toyota',2018)
# print(car1.my_func())


# _________________________Update object properties______________________

# class Employees:
#     def __init__(self,name,age,designation) -> None:
#         self.name = name
#         self.age = age
#         self.designation = designation
    
#     def __str__(self) -> str:
#         return f'Name:{self.name}, Age:{self.age}, Designation:{self.designation}'
    
#     def age_increase(self):
#         return self.age + 1 
    
# id1 = Employees('Haider',22,'Python Developer')

# # change the value of attribute
# id1.age = 24
# print(id1.age)


# _________________________ Loop in Class__________________________

# Iterating over instance attributes

# class Fruits:
#     def __init__(self,item) -> None:
#         self.item = item

#     def print_items(self):
#         for item in self.item:
#             print(item)
        
# x = Fruits(['Mango','Apple','Pineapple','Banana'])
# # x.print_items()


# _________________Iterate over class intance___________________

# class Student:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age

# # class instance
# student1 = Student('Mubashir',20)
# student2 = Student('Umar',21)

# class Classroom:
#     def __init__(self) -> None:
#         self.student = []

#     def add_student(self,student):
#         self.student.append(student)
    
#     def print_students(self):
#         for student in self.student:
#             print (f'Name: {student.name}, Age: {student.age}')

# classroom = Classroom()
# classroom.add_student(student1)
# classroom.add_student(student2)

# classroom.print_students()


# _________________________Overloading__________________________________________


# Overloading, in the context of object-oriented programming, 
# refers to the ability to define multiple methods or functions with the same name 
# but different parameter types or numbers. Python does not support traditional 
# method overloading as seen in some other languages like C++ or Java, where methods 
# can have different signatures. However, Python does provide a form of overloading 
# through the use of default arguments and variable-length argument lists.

# Overloading by default arguments
# class Student:

#     def method(self, x=None):
#         if x is None:
#             print('no argument provided')
#         else:
#             print(f'Here is your output: {x}')

# a = Student()
# a.method()


# Overloading by variable-length argument
# class Teacher:

#     def method(self,*args):
#         if len(args) == 1:
#             print('method has 1 argument: ',args)
#         elif len(args) == 2:
#             print('method has 2 arguments:',args[0], args[1])
#         else:
#             print('method has more than 2 arguments')

# a = Teacher()
# a.method('hello',34,'maria')


