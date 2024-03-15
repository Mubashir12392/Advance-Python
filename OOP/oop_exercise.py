
# Create a class Car with attributes make, model, and year. 
# Include a method display_info() that prints out the car's information.


# class Car:
#     def __init__(self,make,model,year) -> None:
#         self.make = make
#         self.model = model
#         self.year = year

#     def __setattr__(self, name, value) -> None:
#         if name == 'make' and not isinstance(value,str):
#             raise TypeError('Make of the car must be str')
#         if name == 'model' and not isinstance(value,str):
#             raise TypeError('Model of the car must be str')
#         if name == 'year' and not isinstance(value, int):
#             raise TypeError('Year of the car must be Integer')
#         super().__setattr__(name,value)
    
#     def display_info(self):
#         print(f'Make: {self.make}, Model: {self.model}, Year: {self.year}')


# id1 = Car('Toyota','Corolla',2017)
# id1.display_info()

# ___________________________________________________________________________

# Implement a class BankAccount with attributes account_number, account_holder, and balance. 
# Include methods deposit(amount) and withdraw(amount) to modify the balance.

# class BankAccount:
    
#     def __init__(self,account_holder,account_number,balance) -> None:
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.balance = balance

#     def deposit_amount(self, amount):
#         if isinstance(amount, int):
#             self.balance += amount
#             print('Your amount has been succesfully deposited')
#         else:
#             raise TypeError('Amount must be integer')
        
#     def withdraw_amount(self,amount):
#         if isinstance(amount, int):
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print('Your amount has been successfuly withdraw')
#             else:
#                 print('Insufficient amount')
#         else:
#             raise TypeError('Amount must be integer')
        
        
# id1 = BankAccount('MuhammadYameen',345262782,18000)
# id1.deposit_amount(10000)
# id1.withdraw_amount(50800)

# _______________________________________________________________________

# Create a class Employee with attributes name, salary, and employment_year. 
# Implement a method calculate_bonus() that returns a bonus amount based on the years of employment.

# class Employee:

#     def __init__(self,name,salary,employment_year) -> None:
#         self.name = name
#         self.salary = salary
#         self.employment_year = employment_year
        

#     def calculate_bonus(self):
#         bonus_percentages = {1:0.05,
#                              2:0.10,
#                              3:0.15,
#                              4:0.20}
#         if self.employment_year in bonus_percentages:
#             bonus_percent = bonus_percentages[self.employment_year]
#             bonus_amount = self.salary * bonus_percent
#             print(f'{self.name} your Bonus amount is {bonus_amount}')
#         else:
#             print('You are not eligible for bonus')

# id1 = Employee('Mubashir',25000,2)
# id1.calculate_bonus()

# ___________________________________________________________________

# Define a class Animal with a method make_sound(). 
# Create subclasses Dog and Cat that override the make_sound() method to print different sounds.

# from abc import ABCMeta,abstractmethod
# class Animal:
#     __metaclass__ = ABCMeta
#     def __init__(self,breed,age) -> None:
#         self.breed = breed
#         self.age = age

#     @abstractmethod
#     def sound(self,speak):
#         pass

# class Dog(Animal):
#     def sound(self,speak):
#         return f'Dog speaks {speak}'
    
# id1 = Dog('GermanShepherd',2)
# print(id1.sound('Whow'))
    
# class Cat(Animal):
#     def sound(self, speak):
#         return f'cat speaks {speak}'
    
# id2 = Cat('Persion', 3)
# print(id2.sound('Meow'))


# ___________________________________________________________________________

# Implement a class Triangle with attributes side1, side2, and side3. 
# Include a method is_valid() that returns True if the triangle is valid and False otherwise.

# class Triangle:
#     def __init__(self,side1,side2,side3) -> None:
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3

#     def is_valid(self):
#         one_side    = self.side1 + self.side2
#         second_side = self.side1 + self.side3
#         third_side = self.side2 + self.side3

#         if one_side > self.side3 and second_side > self.side2 and third_side > self.side1:
#             return True
       
#         else:
#             return False
        
# id1 = Triangle(10,20,15)
# print(id1.is_valid())

# same solution with professional approach

# class Triangle:
#     def __init__(self,side1,side2,side3) -> None:
#         self.sides = [side1,side2,side3]
#         self.sides.sort()     #sort the list of sides in Ascending order

#     def is_valid(self):
#         # checks if two shortest sides sum is greater than the one biggest side
#         # this condition satisfies the valid triangle
#         return sum(self.sides[:2]) > self.sides[2]

# a = Triangle(20,50,37)
# print(a.is_valid())


# ____________________________________________________________________________________