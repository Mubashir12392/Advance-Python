

# In Python object-oriented programming (OOP), metaclasses provide a means to customize 
# the creation and behavior of classes themselves. Metaclasses are essentially classes of classes.
# They define how classes behave, their instantiation, and their relationships with other classes.

class Meta(type):
    def __new__(cls,name,bases,dict):

        print(f'New Class created: {name}')

        # customize class creation here
        # you can modify attributes, methods or the class itself
        # The __new__ method is called as the new class is created

        return super().__new__(cls,name,bases,dict)
    
class MyClass(metaclass=Meta):
    def __init__(self) -> None:
        pass



# Example
# This will convert every new class instance attribute value to 'b' if it starts with 'a'
    
class Meta(type):
    def __new__(cls,name,bases,dict):


        meta_instance = super().__new__(cls,name,bases,dict)

        original_setattr = meta_instance.__setattr__

        def modifiedattr(self,name,value):
            if isinstance(value, str) and value.startswith('a'):
                value = 'b' + value[1:]
            original_setattr(self,name,value)
        
        meta_instance.__setattr__ = modifiedattr

        return meta_instance

class NewClass(metaclass=Meta):
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f'{self.name}, {self.age}'


id1 = NewClass('ali',23)
print(id1)




