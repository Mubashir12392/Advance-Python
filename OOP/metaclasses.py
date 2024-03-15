

# In Python object-oriented programming (OOP), metaclasses provide a means to customize 
# the creation and behavior of classes themselves. Metaclasses are essentially classes of classes.
# They define how classes behave, their instantiation, and their relationships with other classes.

# class Meta(type):
#     def __new__(cls,name,bases,dict):

#         print(f'New Class created: {name}')

#         # customize class creation here
#         # you can modify attributes, methods or the class itself
#         # The __new__ method is called as the new class is created

#         return super().__new__(cls,name,bases,dict)
    
# class MyClass(metaclass=Meta):
#     def __init__(self) -> None:
#         pass



# __________________________________Modify attributes in metaclass________________________


# class Meta(type):
#     def __new__(cls,name,bases,dct):

#         # add attribute in each creating class
#         dct['newattribute'] = 55

#         # modify existing  class attribute
#         if 'name' in dct:
#             dct['name'] = 'Mubashir'
        
#         # modify existing class instance attribute

#         meta_instance = super().__new__(cls,name,bases,dct)
#         original_isntance = meta_instance.__setattr__
#         def modifiedattr(self,name,value):
#             if name == 'name' and isinstance(value,str):
#                 value = 'Mubashir'
#             original_isntance(self,name,value)

#         meta_instance.__setattr__ = modifiedattr
#         return meta_instance
    
#     # add new instance attribute to class
#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         obj = super().__call__(*args, **kwds)
#         setattr(obj,'school','Royal')
#         return obj
    

# class Myclass(metaclass=Meta):
#     car = 'toyota'
#     name = 'John'

#     def __init__(self,name) -> None:
#         self.name = name

# id1 = Myclass('Ali')
# print(id1.school)

# class NewClass(Myclass):
#     pass

# a = NewClass('Haider')
# print(a.school)


# _______________________________________add/modify methods in metaclasses___________________

# class Meta(type):
#     def __new__(cls,name,bases,dct):

#         # add new method in class
#         dct['new_method'] = cls.new_method

#         # modify existing method
#         dct['list_checker'] = cls.modified_method
#         return super().__new__(cls,name,bases,dct)
    
#     def new_method(cls):
#         print('this is new method')

#     def modified_method(cls):
#         print('This is modified method')

# class MyClass(metaclass=Meta):
#     def __init__(self,name) -> None:
#         self.name = name
    
#     def list_checker(self):
#         print('This is the original method')

# id1 = MyClass('Mubashir')
# id1.new_method()

