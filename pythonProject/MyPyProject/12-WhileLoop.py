'''
Indentation :  Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
Other programming languages often use curly-brackets for this purpose.
'''
# While Loop

ecpl_it_emp=["Sanath", "Jaya Kumar", "Kiran", "Dinesh Thalabare", "Kousal"]
x=0
length=len(ecpl_it_emp)
while x <= length:
 print(ecpl_it_emp[x])
 x += 1

del x
x=0
while x <= 50:
 x +=1
 if x==10 :
  continue
 elif x==50:
  break
 else:
  print(x)
 
 