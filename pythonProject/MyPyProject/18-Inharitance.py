'''
Inheritance In Python :-
Inheritance is an important aspect of the object-oriented paradigm. Inheritance provides code reusability to the program because we can use an existing class to create a new class instead of creating it from scratch.

In inheritance, the child class acquires the properties and can access all the data members/attribute and functions/methods defined in the parent class. A child class can also provide its specific implementation to the functions of the parent class. In this section of the tutorial, we will discuss inheritance in detail.

In python, a derived class can inherit base class by just mentioning the base in the bracket after the derived class name. Consider the following syntax to inherit a base class into the derived class.

Parent Class :- Base Class or Super Class
Child Class :- Derive Class or Sub Class

Python Supports Multiple and Multilevel Inheritance.

Multiple Inheritance :- One child class can access the properties of multiple parent class.
Multi-Level Inheritance :- For example - Clsss-1 is inherited by Class-2 and Class-2 is inherited by Class-3

Function/Method Overloading :- When a class has multiple same name method or function with different number of parameter/Signature, that is called funtion over loading
Function Overriding :- When multiple classes has same name function with same number of parameter or signature.It will make new content of function in the child class. It does not append function's content.
'''

# Example of Inheritance
class Ecpl:
    def __fun__(self):
        self.emp_name="Debabrata"
        self.emp_id="9559"


class it_team(Ecpl):
    def __output__(self):
        self.desi="L1 System Administrator"
        print("Employee Name : ", self.emp_name)
        print("Employee Id : ", self.emp_id)
        print("Employee Designation : ",self.desi)



obj1=it_team()
obj1.__fun__()
obj1.__output__()

