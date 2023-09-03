'''
Polymorphism:-   Polymorphism in Java is a concept by which we can perform a single action in different ways. Polymorphism is derived from 2 Greek words: poly and morphs. The word "poly" means many and "morphs" means forms. So polymorphism means many forms.

There are two types of polymorphism in Java: compile-time polymorphism and runtime polymorphism. We can perform polymorphism in java by method overloading and method overriding.
Runtime Polymorphism :- Method overriding(Error is detected at runtime time)
Compiletime Polymorphism :- Method Overloading(Error is detected at compile time )
* Constructor Overriding is possible but Constructor Overloading is not possible.
'''

#Compiletime Polymorphism or Method Overloading :-
class Ecpl:
    def __add__(self, a,b):
        print("1st Addition is :", a+b)
    
    def __add__(self, a,b,c):
        print("2nd Addition is :", a+b+c)

    # def __add__(self, x,y):
    #     print("3rd Addition is :", x*y)
    
obj=Ecpl()
obj.__add__(10,20,30)
#obj.__add__(10,20,30)

'''
Note :- Python doesn't support traditional method overloading like some other languages(C++, JAVA).
The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method.
'''

