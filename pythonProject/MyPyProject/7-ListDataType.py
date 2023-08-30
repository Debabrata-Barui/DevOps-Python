# List Data Type: It is a Heterogeneous datatype. We can store string, tuple, dict,int, float, complex datatypes. We can add and remove the element in the list. List is a dynamic variable.
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
print(ecpl_it_emp)
print(ecpl_it_emp[1])
print(ecpl_it_emp[1:5])
print(ecpl_it_emp[-1])

# To Delete the variable
del ecpl_it_emp 

# Print data by for loop
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]

for x in ecpl_it_emp:
  print(x)


# Print data by while loop
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
x=0
length= len(ecpl_it_emp)

while x <= length:
  print(ecpl_it_emp[x])



# Print data by while loop
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
x=0
while x <= 100:
  if ecpl_it_emp[x] == ecpl_it_emp[-1]:
    break

  print(ecpl_it_emp[x])
 
del ecpl_it_emp

 # To do type custing into list datatype
ecpl_it_emp=("Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma") #It is in tuple datatype
list1=list(ecpl_it_emp)
print(list1)

# To Add a element at the end of the list :--
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
ecpl_it_emp.append("Asish")
print(ecpl_it_emp)

# To Add a element by the index number of the list :--
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
ecpl_it_emp.insert(1,"Debabrata")
print(ecpl_it_emp)



# To Add multiple element into the list :--
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
multipleEle=("Bharath", "Koushal", "Shadab")
ecpl_it_emp.extend(multipleEle)
print(ecpl_it_emp)

del ecpl_it_emp


# To Delete one element from List
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
ecpl_it_emp.remove("Thalavare")
print(ecpl_it_emp)



# To Delete one element from List by Element Name
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
ecpl_it_emp.remove("Thalavare")
print(ecpl_it_emp)


# To Delete one element from end of the List
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
ecpl_it_emp.pop()
print(ecpl_it_emp)

# To Delete one element of the List by index number
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
ecpl_it_emp.pop(2)
print(ecpl_it_emp)

# To Delete one element by index number from the List
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
del ecpl_it_emp[1]
print(ecpl_it_emp)



# To clear the whole List
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
ecpl_it_emp.clear()
print(ecpl_it_emp)

# To Delete the list datatype
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"]
del ecpl_it_emp
print(ecpl_it_emp)



