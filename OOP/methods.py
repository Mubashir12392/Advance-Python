
# _________________________________________Class methods and Static methods___________________

# Class Method:

# A class method is a method that is bound to the class rather than the object instance. 
# This means it can be called on the class itself or on any instance of the class.
# Class methods are defined using the @classmethod decorator.
# The first parameter of a class method is conventionally named cls, which refers to the class itself. 
# This parameter allows the method to access and modify class-level variables and call other class methods.
# Class methods are commonly used for factory methods or methods that need to operate on class-level data.

class Student:
    students_school = 'Royal'

    @classmethod
    def school(cls):
        if cls.students_school == 'Royal':
            print(f'Every student,s school name is: {cls.students_school}')

id1 = Student()
Student.school()
# id1.school()


# Static Method:

# A static method is a method that is not bound to either the class or the object instance. 
# It behaves like a regular function but is defined within the scope of a class for organizational purposes.
# Static methods are defined using the @staticmethod decorator.
# Unlike instance methods or class methods, static methods do not have access to 
# instance variables (self) or class variables (cls). They operate only on the arguments passed to them.
# Static methods are commonly used when the functionality of a method does not depend 
# on the state of the object or class and does not need access to instance or class variables.

# class Fruits:
#     def __init__(self,name,colour) -> None:
#         self.name = name
#         self.colour = colour

 # We cannot use instance attribute or class attribute in static method
#     @staticmethod
#     def fruits_name(*args):
#         for element in args:
#             print(element,)

# id1 = Fruits('Mango','Yellow')
# id1.fruits_name('Banana','Pineapple','Mango')