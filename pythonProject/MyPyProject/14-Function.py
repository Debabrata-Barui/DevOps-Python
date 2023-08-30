def function1(): #Funtion Defination
    print("Function Defination")


function1() #Function Call



def function2(para1, para2): #Funtion Defination and pass the parameter
    print("Parameters :", para1, para2)


function2("Deb", "Barui") #Function Call and pass the arguments


# Use Return Statement
def function3(para1, para2): #Funtion Defination and pass the parameter
    return para1, para2


print ("Retun : ",function3("Deb", "Barui")) #Print Function Call and pass the arguments


# Pass Default Parameter as a Argument
def function4(name = "Debabrata"):
    print("Name ", name)

function4("Tirumala Raju")
function4()
function4("Garishma")
function4("Khaja Babu")


#Keyword Arguments
def function5(name,emp_id, com_name, address, phone, country="India"):

    print("\nName:",name, "Emp_ID :",emp_id, "\nCompany Name :",com_name, "\nAddress :", address, "\nPhone :", phone, "\nCountry :",country)



function5(name = "Saiko Sanath", emp_id = "8288", address="Bengalore", phone="63738738383", com_name="ecpl")



# Arbitrary Argument
def ecpl(*it_emp): #Funtion Defination and pass the parameter
    print(it_emp[1])    # To get single data
    print(it_emp)   # To get all the data of it_emp


ecpl("Deb", "Saiko Automative Sanath", "Thalavare", "Pombala Porki", "Robotic Ashish")


# Arbitrary Keyvalue Argument
def ecpl2(**it_emp): #Funtion Defination and pass the parameter
    print(it_emp["name"])    # To get single data
    print(it_emp)   # To get all the data of it_emp


ecpl2(name = "Saiko Sanath", emp_id = "8288", address="Bengalore", phone="63738738383", com_name="ecpl")


# Make a function without any statement
def funFunction():
    pass

funFunction()




