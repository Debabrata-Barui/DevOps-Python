'''
 Tuple Data Type :- # It is a Heterogeneous datatype. We can store string, tuple, dict,int, float, complex datatypes. It is constant variable. We can't modify the data element inside the tuple.
To modify the data element, we have to typecast into list.
'''
ecpl_it_emp=("Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma")
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



 # To do type custing into tuple datatype
ecpl_it_emp=["Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma"] #It is in list datatype
tuple1=tuple(ecpl_it_emp)
print(tuple1)


# To Add a element at the end of the tuple :--
ecpl_it_emp=("Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma")
list1=list(ecpl_it_emp)
list1.append("Asish")
tuple1=tuple(list1)
print(tuple1)


# To Delete one element from end of the tuple
ecpl_it_emp=("Arbind", "Pumbala Purki", "Saiko Sanath", "Thalavare", "Garishma")
list1=list(ecpl_it_emp)
list1.remove("Thalavare")
tuple1=tuple(list1)
print(tuple1)