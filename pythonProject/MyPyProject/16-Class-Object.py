class BlankClass:
    pass

BlnkObj=BlankClass()

class Ecpl1:
    name="Debabrata"
    age=22
    address="West Bengal, " + "Kolkata"


obj1=Ecpl1()
print("\nName :", obj1.name,"\nAge : ", obj1.age,"\nAddress :",obj1.address)
print("Type of obj1 : ", type(obj1))

class Ecpl2:
    name="Debabrata"
    age=22
    address="West Bengal, " + "Kolkata"
    def it_team(x): # Here x is a
        print("\nName :", x.name,"\nAge : ",x.age,"\nAddress :",x.address)

obj2=Ecpl2()
obj2.it_team()
print("Type of obj1 : ", type(obj2))


class Ecpl3:
    def fun(x):
        name="Debabrata"
        com="Ecpl"
        return name, com  # It will return in tuple format
obj3=Ecpl3()
print(obj3.fun())


class Ecpl4:
    def fun(x, name, com):
        print(name, com)
obj4=Ecpl4()
obj4.fun("Debabrata", "ECPL")

class Ecpl5:
    nam="Debabrata"
    cmp="ECPL"
    def __init__(x):
        print(x.nam,x.cmp)
        
obj5=Ecpl5()
obj5.__init__()

del obj5
