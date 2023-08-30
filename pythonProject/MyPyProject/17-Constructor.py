#**************************************************************************
'''
** Python Constructor :-
The constructor is used to initialise the object or instance of a class.
In Python, the method the __init__() simulates the constructor of the class. This method is called when the class is instantiated. It accepts the self-keyword as a first argument which allows accessing the attributes or method of the class.

We can pass any number of arguments at the time of creating the class object, depending upon the __init__() definition. It is mostly used to initialize the class attributes. Every class must have a constructor, even if it simply relies on the default constructor.

Self Variable :- This works like a this keyword. It initialises the Attributes or Property of Class. Here Self keyword makes the loca variable to global variable
'''
print("******************************Default Constructor***************************************")
class Ecpl:
    name="Debabrata"
    id="9559"

    def __fun__(self):
        print(self.name, self.id)

obj=Ecpl()
obj.__fun__()


print("******************************Non-Parameterised Constructor***************************************")
# Non-Parameterised Constructor
class Ecpl1:
    def __init__(self):
        print("This is a Non-Parameterised constructor")

obj1=Ecpl1()

print("*************************Parameterised Constructor")
# Parameterised Constructor
class Ecpl2():
    def __init__(self,name,emp_id):
        self.lable="Leble-1"
        self.name=name
        self .emp_id=emp_id

    def __output__(self):
        print("EMP Name:", self.name)
        print("EMP_ID :",self.emp_id)
        print("Designation :", self.lable)



obj2=Ecpl2("Debabrata", "9559")
obj2.__output__()


