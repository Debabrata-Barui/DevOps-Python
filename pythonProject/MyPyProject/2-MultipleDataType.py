# print the hello world!!
print('Hello, World!')
print("Hello World!")
#print "Hello World";
""" 
print 'Multi Line Command';

"""
# Object Reference :- Python is the highly object-oriented programming language; that's why every data item belongs to a specific type of class.

# Variable in Python
a=10
print(a)
print(type(a)) # Interger Class

b=10.567
print(b)
print(type(b)) # Float Class

c=10.45j
print(c)
print(type(c))# Complex Class


d="A quick bron fox jumps over the lazy dog"
print(d)
print(type(d)) # String Class


String=str(123.3434) # This is String Class
Float=float(123.343) # This is float calss
Integer=int(103.3454) # This is integer class
Complex=complex(23.56j) # This is complex class


print("String:",String,"type=",type(String))

print("Float :",Float,"type=", type(Float))

print("Integer : ",Integer,"type", type(Integer))

print("Complex : ", Complex," type", type(Complex))


# Multi value Variable
x="Debabrata", "Bharath", "Sanath" # Tuple class
print("The Multi valued variable(x) :", x, "Type of x", type(x))

m=n=o=" ECPL " # String Class
print("Conticatenation :- ", " m=> " + m + ",Type => ",  type(m),  ":  n=> " + n + ",Type => ",  type(n),  ":  o => " + o + ",Type => ",  type(o))

# List Variable :- It is a Hetrogeneous datatype
ecpl_it_mem=["Dev", "Sanath", "Bharath", "Ashish", "James", "Arbindh", "Jai", "Jero" "Dinesh", 100, ["Simra", "Nanduka", 723145], ("tuple-value1", "tuple-value-2"), {"dict-key1": "value1", "dict-key2":"value2"}] # List Class
print(ecpl_it_mem, ": Type->", type(ecpl_it_mem))

print(ecpl_it_mem[2], ecpl_it_mem[3+1])
print(ecpl_it_mem[2:7])

# According to the index
ecpl_dep=["IT", "HR" ,"ADMIN", 100]
p,q,r,n=ecpl_dep
print(p,q,r,n)
print("P type:",type(p),", Q type:", type(q), ", R type:", type(r), ", N type:", type(n))


tuple=("Debabrata", "XYZ", "CCCC", 3434, ("tuple1", "tuple2", 5366), ["listVal1", "ListVal2"], {"key1" : "value1", "key2" : "value"})

print("Tuple =>",tuple,type(tuple))
print(tuple[1:4])
print("Type[3] :", type(tuple[3]))

# Dictionary Type
it_emp={
        "Name" : "Debabrata",
        "Designation" :
        "L1 Engeneer",
        "Age": 23,
        "Salary" : 25000.6700,
        "Address" : ["Simra", "Nanduka", "Purulia", 723145, {"Dict-key1":"value1", "Dict-key2" : "Value2"}],
        "hr_emp" : ("tuple-1", "tuple-2"),
        "Dict" : {"Key-1" : "Value1"}

}

print(it_emp)
print("it_emp Type : ", type(it_emp))
print(it_emp["Name"])
print("Name Type :",type(it_emp["Name"]))
print("Age Type :", type(it_emp["Age"]))
print("Salary Type :", type(it_emp["Salary"]))
print("Address Type :", type(it_emp["Address"]))
print("hr_emp Type :", type(it_emp["hr_emp"]))

# For Random Number
import random
print(random.randrange(100001,999999))


# None value:- It is like Nul value.
var1= None
print("The value of var1 :", var1)
print("The type of var1 is :", type(var1)) # <class 'NoneType'>

'''
Datatype Function :-
Integer => int()
Float => float()
Complex => complex()
String => str()
List => list()
Tuple => tuple()
Dictionary => dict()
Set => set()
Range => range()
Length => len()
Input => input()
Type => type()

'''
