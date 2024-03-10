

# ______________________________________Theory__________________________

# Abstraction in Python object-oriented programming (OOP) is the concept of hiding 
# the complex implementation details of a class and exposing only the essential features 
# or functionalities to the outside world. It focuses on providing a clear, high-level 
# interface for interacting with objects while hiding the internal complexities.


# Achieving Abstraction in Python:
# In Python, abstraction can be achieved by having/using abstract classes and methods in our programs.


# Understanding Abstract Methods and Classes:
#  An abstract method is a method that is declared, but does not contain implementation. 
# An abstract method in a base class identifies the functionality that should be implemented 
# by all its subclasses. However, since the implementation of an abstract method would differ 
# from one subclass to another, often the method body comprises just a pass statement. 
# Every subclass of the base class will ride this method with its implementation. 
# A class containing abstract methods is called abstract class.Python provides the 
# abc module to use the abstraction in the Python program,


# ______________________________Code______________________________

from abc import ABCMeta, abstractmethod

class Shape():
    __metaclass__ = ABCMeta

    def __init__(self,shapetype) -> None:
        self.shapetype = shapetype

    @abstractmethod
    def area (self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    
    def __init__(self, length,breath) -> None:
        Shape.__init__(self,'Rectangle')
        self.length = length
        self.breath = breath

    def area(self):
        return self.length * self.breath
    
    def perimeter(self):
        return 2 * (self.length + self.breath)
    
id1 = Rectangle(44,22)
# print(id1.perimeter())
    
class Circle(Shape):

    pi = 3.14
    def __init__(self, radius) -> None:
        Shape.__init__(self,'Circle')
        self.radius = radius
    
    
    def area(self):
        return  (self.radius * self.radius) * Circle.pi
    
    def perimeter(self):
        return (2 * Circle.pi) * self.radius

id2 = Circle(15)
# print(id2.perimeter())


# _____________________________________Another example__________________________

class Bank:

    __metaclass__ = ABCMeta

    def __init__(self,bankname) -> None:
        self.bankname = bankname

    @abstractmethod
    def customer_detail(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deposit_amout(self):
        pass

    @abstractmethod
    def withdraw_amount(self):
        pass


class Bank_customer(Bank):


    def __init__(self, bankname,branchname,customername,accountno,accounttype,balance) -> None:
        super().__init__(bankname)
        self.__branchname = branchname
        self.__customername = customername
        self.__accountno = accountno
        self.__accounttype = accounttype
        self.__balance = balance

    def customer_detail(self,):
            return f'BanK:{self.bankname}, Branch:{self.__branchname}, Name:{self.__customername}, AccountNo:{self.__accountno}, Account_type:{self.__accounttype}, Balance:{self.__balance}'
    
    def check_balance(self,accountno):
        if accountno == self.__accountno:
            return f'Your Balance is {self.__balance}'

    def deposit_amout(self,amount):
        self.__balance += amount
        return 'Your Money has been succesfully deposited'
    
    def withdraw_amount(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f'Your {amount} has been succesfully withdraw '
        else:
            return 'You have insufficient Funds'

id1 = Bank_customer('Meezan_Bank','Samanabad','Mubashir',4123344574,'Current',324)
id2 = Bank_customer('Meezan','People-colony','Ali-Raza',1234636378,'Saving',456)
print(id1.check_balance(4123344574))
print(id1.deposit_amout(1000))
print(id1.check_balance(4123344574))
print(id1.withdraw_amount(500))
print(id1.check_balance(4123344574))
print(id1.customer_detail())



# _____________________________________________Abstract Base Class_________________________

# An Abstract Base Class (ABC) in Python is a way of defining a class that cannot be instantiated 
# directly but serves as a blueprint for other classes. It defines a set of abstract methods and 
# properties that must be implemented by its subclasses. The purpose of an ABC is to provide a 
# common interface or behavior that can be shared among multiple classes.

# In the 2nd Example, class Bank is a Abstract Base class (ABC)