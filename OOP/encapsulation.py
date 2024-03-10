# ____________________________________Encapsulation___________________

# Encapsulation is one of the fundamental principles of object-oriented programming (OOP) that 
# refers to the bundling of data and methods that operate on the data into a single unit, 
# known as a class. It allows for the implementation details of a class to be hidden from 
# the outside world, and only the necessary interfaces are exposed for interacting with the class.


# class Animals:
#     def __init__(self,name,age) -> None:
#         self.__name = name       # Private instance attribute    
#         self.__age = age         # Private instance attribute

#  # private instance attribute values can only be show by methods whether it is magic or user method
#     def __str__(self) -> str:
#         return f'Name: {self.__name}, Age: {self.__age}'

#  # Private instance attribute values can only be change by methods
#     def set_name(self,name):
#         self.__name = name
    

# id1 = Animals('Lion',10)
# id1.set_name('cheetah')
# # print(id1)

# NOTE you cannnot access  instance attribute value by typing print(instance.attribute)
# print(id1.__name)


# _____________________________________Wrapping up______________________________________

# In Python Object-Oriented Programming (OOP), "wrapping up" typically refers to encapsulating data 
# and behavior within a class. This encapsulation allows for better organization, abstraction,
# and modularity of code. Here are some aspects of "wrapping up" in Python OOP:

# Encapsulation
# Method Wrapping
# Abstraction