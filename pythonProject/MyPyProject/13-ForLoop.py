'''
Indentation :  Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
Other programming languages often use curly-brackets for this purpose.
'''
# For Loop
ecpl_it_emp=["Sanath", "Jaya Kumar", "Kiran", "Dinesh Thalabare", "Kousal"]
print("Length :", len(ecpl_it_emp))
for emp in ecpl_it_emp:
    print(emp)

for x in range(1, 50):
 if x==10:
  continue 
 elif x==50:
  break
 else:
  print(x)
 
 
for x in range(1, 50, 5):
 print(x)
 