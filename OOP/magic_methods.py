

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

# __str__(self): 
# This method returns a string representation of the object. 
# It's meant to be readable and is typically used for displaying information to end-users.


# _____________________________________Repr()_________________________________________

# class Book:
#     def __init__(self,booktitle,author) -> None:
#         self.booktitle = booktitle
#         self.author = author

#     def __repr__(self) -> str:
#         return f'Book({self.booktitle}, {self.author})'
    
   
    
# book1 = Book('Iqbal','Allama-Iqbal')
# print(book1)

# Repr function allow us to recreate book object using eval()

# mybook = repr(book1)
# new_book = eval(mybook)
# print(new_book == book1)

# __________________________len()______________________________


# class Students_data:
#     def __init__(self,data) -> None:
#         self.data = data

#     def __len__(self):
#         return len(self.data)
    

# id1 = Students_data([23,445,66,4,2,36,3])
# print(len(id1))

#_______________________getitem()____________________

# class Student_data:
#     def __init__(self,data) -> None:
#         self.data = data

#     def __getitem__(self,index):
#         return self.data[index]
    

# id1 = Student_data([23,56,78,35,783,267])
# id2 = Student_data({'Name':'Mubashir',
#                     'Age': 20,
#                     'class':'BSCS'})
# print(id1[5])
# print(id2['Name'])

# ________________________setitem()_______________________

# class Student_data:
#     def __init__(self,data) -> None:
#         self.data = data

#     def __setitem__(self,index,value):
#         self.data[index] = value

#     def print_items(self):
#         if isinstance(self.data, list):
#             for item in self.data:
#                 print(item)
#         if isinstance(self.data, dict):
#             for key, value in self.data.items():
#                 print(value)


# id1 = Student_data([23,56,78,35,783,267])
# id2 = Student_data({'Name':'Mubashir',
#                     'Age': 20,
#                     'class':'BSCS'})

# id1[2] = 98
# id2['Age'] = 23
# id1.print_items()
# id2.print_dict_values()

# ______________________________delitem()____________________

# class Student_data:
#     def __init__(self,data) -> None:
#         self.data = data

#     def __delitem__(self,index):
#         del self.data[index]

#     def print_items(self):
#         for item in self.data:
#             print(item)

# id1 = Student_data([23,56,78,35,783,267])
# id2 = Student_data({'Name':'Mubashir',
#                     'Age': 20,
#                     'class':'BSCS'})

# del id1[2]
# id1.print_items()


# ____________________________________iter()_______________________________


# class Student_data:
#     def __init__(self,data) -> None:
#         self.data = data

#     def __iter__(self):
#         if isinstance(self.data,list):
#             return iter(self.data)
#         if isinstance(self.data, dict):
#             return iter(self.data.items())
    
    
    
# id1 = Student_data([23,56,78,35,783,267])
# id2 = Student_data({'Name':'Mubashir',
#                     'Age': 20,
#                     'class':'BSCS'})
 
# # for key, value in id2:
# #     print(value)

# # for items in id1:
# #     print(items)

# # we can also use iter() like that by using next () to print the next element of list 
# iterator = iter(id1)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# ___________________________________next()__________________________

# The __next__() magic method in Python is used to define the behavior of an iterator 
# when it yields the next element in a sequence

# class Iterator:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.index = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index < len(self.data):
#             value = self.data[self.index]
#             self.index += 1
#             return value
#         else:
#             raise StopIteration()
        

# a = Iterator([23,45,76,56,32,77])
# for item in a:
#     print(item)

# By implementing the __next__() method, you can create custom iterator objects that can be used 
# in loops or with the next() function to iterate over sequences of data.
    
# ______________________________________contains()_______________________
    
# class Student:
#     def __init__(self,data) -> None:
#         self.data = data
  
#     def __contains__(self, value):
#         return value in self.data
    
# id1 = Student([2,3,4,656,77,32,54])
# print(3 in id1)

# ________________________________eq()_________________________________________

# The __eq__() magic method in Python is used to define the behavior of the equality 
# comparison operator (==) when applied to objects of a user-defined class. 
# It allows you to customize how instances of your class are compared for equality.
# Basically it use to check whether instances of class are equal or not

# class Coordinates:
#     def __init__(self,x,y) -> None:
#         self.x = x
#         self.y = y

#     def __eq__(self, value: object) -> bool:
#         if isinstance(value, Coordinates):
#             return self.x == value.x and self.y == value.y
#         else:
#             return False
        
# id1 = Coordinates(34,36)
# id2 = Coordinates(34,36)

# print(id1 == id2)

# ___________________________Comparison operator magic methods______________

# The magic methods __lt__, __le__, __gt__, and __ge__ in Python are used to define the 
# behavior of comparison operators <, <=, >, and >=, respectively, 
# when applied to objects of a user-defined class. These methods allow you to 
# customize how instances of your class are compared with each other.

# class Rectangle:
#     def __init__(self,length,width) -> None:
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def __lt__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() < other.area()
        
#     def __le__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() <= other.area()
        
#     def __gt__(self,other):
#         if isinstance(other, Rectangle):
#             return self.area() > other.area()
        
#     def __ge__(self,other):
#         if isinstance(other, Rectangle):
#             return self.area() >= other.area()
        
# id1 = Rectangle(23,15)
# id2 = Rectangle(26,18)

# print(id1 > id2)
# print(id1 < id2)
# print(id1 >= id2)
# print(id1 <= id2)


# ______________________________ Arithemetic operators magic methods_____________________

# In Python, arithmetic operations like addition, subtraction, multiplication, division, etc., 
# can be performed using special methods called magic methods or dunder methods. 
# These methods allow you to define custom behavior for arithmetic operations 
# on objects of your custom classes.

# class Data:
#     def __init__(self,x,y) -> None:
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if isinstance(other, Data):
#             return self.x + other.x, self.y + other.y
        
#     def __sub__(self,other):
#         if isinstance(other, Data):
#             return self.x - other.x, self.y - other.y
        
#     def __mul__(self, other):
#         if isinstance(other, Data):
#             return self.x * other.x, self.y * other.y
        
#     def __truediv__(self,other):
#         if isinstance(other, Data):
#             return self.x // other.x, self.y // other.y
        
# id1 = Data(16,49)
# id2 = Data(4,7)
# print(id1 / id2)
