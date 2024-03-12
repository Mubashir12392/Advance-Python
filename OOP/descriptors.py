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
        if not isinstance(fuel_cap, int):
            raise TypeError('Fuel capacity of the car must be int')
        if fuel_cap <= 0:
            raise ValueError('Fuel Capacity can never be zero')
        
        self.make = make
        self.model = model
        self.fuel_cap = fuel_cap


    def __str__(self) -> str:
        return f'{self.make} company car model {self.model} has fuel capacity of {self.fuel_cap} litres'

id1 = Car('Toyota','Prius',44)
id1.make = 11
print(id1)

#NOTE
# You might use a class descriptor if you're implementing a database ORM where you need to lazily 
# load data, perform validation, or trigger cascading updates upon attribute access, setting, or deletion.
# It is used when attributes are not private, if private use property decorator