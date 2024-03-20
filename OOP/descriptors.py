# _______________________________________Descriptors___________________________________________

# In Python, descriptors are classes that define how attributes are accessed, 
# modified, or deleted within another classes. They are a powerful tool in Python's 
# object-oriented programming, allowing developers to customize attribute access and 
# implement various behaviors such as validation, lazy evaluation, and data transformation.

# Descriptors are typically implemented as classes with one or more of the following special methods:

# __get__(self, instance, owner): 
#                                Invoked when the descriptor's attribute is accessed. 
#                       It receives three arguments: 
#                       self (the descriptor instance), 
#                       instance (the instance of the owner class (where the attribute is accessed).
#                       owner (the owner class itself).

# __set__(self, instance, value): 
#                                 Invoked when the descriptor's attribute is set. 
#                             It receives three arguments: 
#                             self, instance, and value (the value being assigned to the attribute).

# __delete__(self, instance): 
#                         Invoked when the descriptor's attribute is deleted. 
#                           It receives two arguments: 
#                             self and instance.

# Example
# We have to make Descriptor coz, we set the conditons for first input of attribute, 
# But we didn't set the conditon when a user wants to change input. That's why descriptor is used because 
# we cannot implement these conditions in the owner class, 


class Descriptor:
    def __init__(self) -> None:
        self.__fuel_cap = 0

    def __get__(self,instance,owner):
        return self.__fuel_cap
    
    def __set__(self,instance,value):
        if not isinstance(value, int):
            raise TypeError('Fuel capacity must be int')
        if value <= 0:
            raise ValueError('Fuel capacity can never be zero')
        
        self.__fuel_cap = value

    def __delete__(self,instance):
        del self.__fuel_cap


class Car:
    fuel_cap = Descriptor()

    def __init__(self,make,model,fuel_cap) -> None:
        if not isinstance(make, str):
            raise TypeError('Make of the car must be str')
        if not isinstance(model,str):
            raise TypeError('Model of the car must be str')
        
        self.make = make
        self.model = model
        self.fuel_cap = fuel_cap

    # You can also set descriptor conditon by using this magic method

    # def __setattr__(self, name,value) -> None:
    #     if name == 'make' and not isinstance(value, str):
    #         raise TypeError('Make of the car must be str')
    #     super().__setattr__(name,value)


    def __str__(self) -> str:
        return f'{self.make} company car model {self.model} has fuel capacity of {self.fuel_cap} litres'

id1 = Car('Toyota','Prius',44)
id1.make = 11
print(id1)

#NOTE
# You might use a class descriptor if you're implementing a database ORM where you need to lazily 
# load data, perform validation, or trigger cascading updates upon attribute access, setting, or deletion.
# It is used when attributes are not private, if private use property decorator
# Descriptor class has effect on both, first instance attribute input and when user change its value



# ___________________________________Property Decorators_______________________________


# The property decorator in Python is a built-in feature that allows you to define getter, setter, and 
# deleter methods for encapsulated instance attributes and class attributes.
# It provides a way to encapsulate attribute access, enabling you to execute custom logic when getting,
# setting, or deleting attributes.

# class Student:
#     def __init__(self,name) -> None:
#         self.__name = name

#     @property
#     def name(self):                    # Main property method
#         return self.__name
    

#     # Setter method
#     @name.setter                       # This name will always same to the main property method
#     def name_change(self, name):
#         if isinstance(name,str):
#             self.__name = name
#         else:
#             raise TypeError('Name must be str')


#     # Deleter method
#     @name.deleter                    # This name will always same to the main property method
#     def delete_name(self):
#         del self.__name



# When you define a method as a property using the @property decorator, 
# it essentially transforms that method into a descriptor instance. 
# Descriptors provide a way to define how attribute access works on a class, 
# allowing you to customize behavior when accessing, setting, or deleting attributes.
# How to call these methods
# You should call these methods without parenthesis(), with the method name 
# These property decoraters allow us to use Encapsulated attributes like the normal attributes
        

# a = Student('Ali')
# print(a.name)
# a.name_change = 'Mubashir'      
# print(a.name)
# del a.delete_name


# You can also convert normal methods to property Methods

# class Teacher:
#     def __init__(self,name,age) -> None:
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name
    
#     def update_name(self, new_name):
#         self.__name = new_name

#     def delete_name(self):
#         del self.__name

#     # Convert all methods into property methods
#     name = property(get_name, update_name, delete_name)

# obj1 = Teacher('Ambreen',25)
# obj2 = Teacher('Themina',23)

# obj1.name = 'Shumaila'
# print(obj1.name)
# del obj2.name
# print(obj2.name)


#NOTE
# You might use a property decorator if you're implementing a simple data container 
# class where you want to ensure that certain attributes are always accessed or modified 
# through getter and setter methods. It is used when attributes are private. 
# Property decorators has only effect, when user change instance attributes value


#NOTE 2
# for private attributes, using property decorators is a recommended approach, while for simple attributes, 
# directly assigning them or using setattr in the __init__ method is sufficient. 
# Descriptor classes can be useful for more advanced attribute handling scenarios but may introduce 
# complexity that is not always necessary.