
# ___________________________________Property Decorators_______________________________


# The property decorator in Python is a built-in feature that allows you to define getter, setter, and 
# deleter methods for encapsulated instance attributes and class attributes.
# It provides a way to encapsulate attribute access, enabling you to execute custom logic when getting,
# setting, or deleting attributes.

# # Getter method
# class Student:
#     def __init__(self,name) -> None:
#         self.__name = name

#     @property
#     def name(self):                    # Main property method
#         return self.__name
    

#     # Setter method
#     @name.setter                       # This name will always same to the main property method
#     def name_change(self, name):
#         self.__name = name


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
# through getter and setter methods. It is used when attributes are private