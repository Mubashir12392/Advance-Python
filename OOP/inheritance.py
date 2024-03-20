
# Inheritance is the process by which one class takes on the attributes and methods of another
# Newly formed classes are called CHILD CLASSES, and the classes that you derive child classes
# from are called PARENT CLASSES.


# Simple inheritance

#Base Class
class Parent:                    # Base-Class / Parent-Class / Super-class

    skin_color = 'Brown'
    language = 'urdu'
    
    def __init__(self,name,age,gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        

    def __str__(self) -> str:
        return f'Name:{self.name}, Age:{self.age}, Gender:{self.gender}'
    
    def greet(self):
        return f"hello From Parents"
    
    def each_name(self):
        return f" i am the member of this Family, my name is {self.name}"


# Parent Class instances
Dad = Parent('Yameen',50,'Male')
Dad.skin_color = 'Dark_Brown'

Mom = Parent('Sabahat',48,'Female')
Mom.skin_color = 'White'


# use a user defined function in class

# print(Mom.each_name())
# print(Dad.greet())


# Derived Class
class Child(Parent):             # Derived-class / Child-class / Sub - Class

    #Extend the instance attributes of Base class in Derived class
    def __init__(self, name, age, gender, qualification) -> None:
        super().__init__(name,age,gender)
        self.qualification = qualification


    # Extend str method of Base class in derived class
    def __str__(self) -> str:
        super_parent = super().__str__()
        return f'{super_parent}, Qualification:{self.qualification}'
    
    # Override a method of Base Class
    def greet(self):
        return 'Greet from the children'
    
    # Access Base class method to extend in derived class
    def each_name(self):
        super_method = super().each_name()
        return f'{super_method}, and I  love my parents'

    # Add a new method in Derived class
    def adult_checker(self):
        if self.age < 18:
            return f'{self.name} is not an Adult'
        else:
            return f'{self.name} is an adult'


# Create an instance of Derived class
Mubashir = Child('Mubashir',20,'Male','BSCS')
Konain = Child('Konain',17,'Female',10)


#use user defined method of derived class
# print(Mubashir.adult_checker())
# print(Konain.each_name())


# To check object is the instance of which class
# print(isinstance(ali,Parent))

# # ______________________________Multiple Inheritance___________________


# # Multiple inheritance is a feature in object-oriented programming languages, 
# including Python, that allows a class to inherit attributes and methods 
# from more than one parent class.


# # lets make 2 base classes

# class Base1:
#     def __init__(self,name,house) -> None:
#         self.name = name
#         self.house = house 
#     def __str__(self) -> str:
#         return f'Name: {self.name}, House_no:{self.house}'
    
#     def my__fucn(self):
#         return f'Hello from {self.name}'
    

# class Base2:
#     def __init__(self,area,city) -> None:
#         self.area = area
#         self.city = city

#     def __str__(self) -> str:
#         return f'Area: {self.area}, City: {self.city}'
    
#     def my_method(self):
#         city = self.city
#         return city.upper()

    
# # Make a derived class and inherit from both base classes
    
# class Derived(Base1, Base2):
#     def __init__(self, name,house,area,city) -> None:
#         Base1.__init__(self,name,house)
#         Base2.__init__(self,area,city)
    

#     # call str of both base 1 and base 2
#     def __str__(self) -> str:
#         return f'{Base1.__str__(self)}, {Base2.__str__(self)}'
    
#     # Override the method of Class base 2
#     def my_method(self):
#         city = self.city
#         return city.lower()

# a = Derived('Mubashir','P.379','Samanabad','FAISALABAD')
# print(a.my_method())


# ________________________________Multilevel inheritance________________________

# Multilevel inheritance is a type of inheritance in object-oriented programming 
# where a derived class inherits from a base class, and then another class inherits 
# from this derived class. This creates a hierarchy of classes, forming a chain of inheritance.


# class Ancestor:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return f'Name: {self.name}, Age: {self.age}'

# class Grandparent(Ancestor):
#     def __init__(self, name, age, skincolour) -> None:
#         super().__init__(name, age, )
#         self.skin_colour = skincolour

#     def __str__(self) -> str:
#         return f'{Ancestor.__str__(self)}, Skin: {self.skin_colour}'


# class Parent(Grandparent):
#     def __init__(self, name, age, skincolour,location) -> None:
#         super().__init__(name, age, skincolour)
#         self.location = location

#     def __str__(self) -> str:
#         return f'{Grandparent.__str__(self)}, Location: {self.location}'


# class Child(Parent):
#     def __init__(self, name, age, skincolour, location) -> None:
#         super().__init__(name, age, skincolour, location)

#     def __str__(self) -> str:
#         return super().__str__()
    
# id1 = Child('Mubashir',20,'White','Faisalabad')
# print(id1)

# __________________________________Method Overriding___________________

# Method overriding occurs when a subclass provides a specific implementation of a method 
# that is already defined in its superclass. This allows objects of the subclass to respond
# to the same message or method invocation in a manner specific to the subclass. 
# It is a fundamental aspect of polymorphism in OOP.


# class Hen:
#     def __init__(self,breed,age) -> None:
#         self.breed = breed
#         self.age = age

#     def __str__(self) -> str:
#         return f'Breed: {self.breed}, Age: {self.age}'
    
#     def age_change(self):
#         return self.age* 4
    
# class Chick(Hen):
#     def age_change(self):
#         return self.age - 2
    
# id1 = Chick('Desi',3)
# print(id1.age_change())


# ___________________________________Polymorphism__________________________________

# In Python, polymorphism is a fundamental feature of object-oriented programming (OOP) 
# that allows objects of different derived classes to be treated as objects of a common superclass. 
# This concept is closely tied to inheritance and method overriding.

# Polymorphism in Python can be achieved through two main mechanisms:

# Method overriding

class Cars:
    def car_colour(self):
        print('Black')

class OldCar(Cars):
    def car_colour(self):
        print('Blue')

class NewCar(Cars):
    def car_colour(self):
        print('Red')

# Make objects of derived classes
a = OldCar()
b = NewCar()

# Objects of derived classes treated(not made) as object of base class,This is called polymorphism
animals = [a,b]

# iterate over the list of animals and calling the method car_colour
for animal in animals:
    animal.car_colour()