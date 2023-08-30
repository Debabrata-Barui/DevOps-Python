ecpl_it_emp=["Kiran", "Debabrata", "Raju Rashtokhi", "Asish", "Sadhab", "Arbindh", 20000.6488, 22]
print(ecpl_it_emp)
print(ecpl_it_emp[1])
print(ecpl_it_emp[2:5])
print(ecpl_it_emp[:5])
print(ecpl_it_emp[3:])

print("Type of ecpl_it_emp[-1]:", type(ecpl_it_emp[-1]))

print("Type of ecpl_it_emp[1]:", type(ecpl_it_emp[1]))

print(len(ecpl_it_emp))#To fins the total value of list


ecpl_it_emp[1]="Sanath" # To change the list element 
print(ecpl_it_emp)

ecpl_it_emp[1:3]=["Debabrata","Bharath", "Kousal"]
print(ecpl_it_emp)

#Insert the list elelement
ecpl_it_emp.insert(3,'{"Name" : "value"}')
print(ecpl_it_emp)

# Append/add the element at the end of the list
ecpl_it_emp.append("Imran")
print(ecpl_it_emp)

print("-------------------------------------------------------------------")

# Extend the List
list1=["Debabrata", "Shadab", "Bharath", "Sanath"] # List
list2=['Jaya Kumar', 'Yunesh', 'Kiran'] # List
list1.extend(list2)
print(list1)

list3=("Imran", "Snadhya") # Tuple

list1.extend(list3)

print(list1)