x=10
y=20
print(x+y) # Addition
print(x-20) # Subtraction
print(y/5) # Multiplication
print(y%2) # Modulus
print(20**2) # Exponential/ 20^2
print(19//2) #The floor division // rounds the result down to the nearest whole number 
print(x>5 and y<50)
print(x<5 or y>20)

print("------------------------------------------------------------------------")
x = ["Kiran", "Debabrata", "Ashish"]
y = ["Kiran", "Debabrata", "Ashish"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
