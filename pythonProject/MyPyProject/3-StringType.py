str1="Debabrata Barui"
# Slicing String
print(str1[3])
print(str1[2:5])
print(str1[:9])
print(str1[10:])

# Concatination
str2="Parinita"
print(str1 + str2)


# Format String
age = 17
name = "Debabrata"
com="ECPL"
ctc = 600000.9098
str3= "My name is {}. My age is {}. I am working on {}.My CTC is {}"
print(str3.format(name, age, com, ctc))


# Escape Characters
print("A quick brown\ fox jumps over the \n lazy :\" \' dog ")
print("A quick brown \n fox jumps over the lazy dog") # New Line
print("A quick brown \r fox jumps over the lazy dog") # Carrige Return
print("A quick brown fox \t jumps over the lazy dog") # Tab

# String convertion
string1="debabrata barui.a uick brown fox jumps over the lazy dog."
strUpper=string1.upper(); # Upper Case
print(strUpper)

strLower=strUpper.lower() # Lower Case
print(strLower)

strCapitalize= strLower.capitalize() # Capitalize
print(strCapitalize)

strTitle = strLower.title() # Title Case
print(strTitle)

print("------------------------------------------------------------------------------------")



# String Alignment
str101="A quick brown fox and dog jumps over the lazy dog"
center=str101.center(200) # To make a center alignment
print(center)

print(center.count("dog"))# we can count the number of word in a centence

name="Debabrata Barui"

print(name.encode()) # Encode the string

# Period or Punctuation Symbol
str102="A quick brown fox jumps over the lazy dog."
print(str102.endswith("."))

# Find the word
print(str102.find("fox")) #It will return the index number

# Format is used put the different value in long string
no_of_fox=100
no_of_dog=10.675
str103="A quick {} fox jumps over the {} dog"
putText = str103.format(no_of_fox, no_of_dog)
print(putText)

# String validation
phone="8637550219"
print(phone.isdigit())  # for checking whether this is number or not
print(phone.isnumeric())

# Length of the string
print("The phone number is :", len(phone))

# Data Striping/Remove the extra whitespace frome the string
str501="        Debabrata Barui              "
strip=str501.strip()
print("This is ", strip, ". Who is very multi telented boy ")

str502="            Debabrata"
leftstrip= str502.lstrip()
print("This is ", leftstrip, ". Who is very multi telented boy ")


str503="Debabrata         "
rightstrip= str503.rstrip()
print("This is ", rightstrip, ". Who is very multi telented boy ")

# Replace the substring
mystr="A quick brown fox jumps over the lazy dog"
replace=mystr.replace("dog", "shadab")
print(mystr)
print(replace)

# Return the index number accoring the sub string
str1=" A quick brown fox jumps over the lszy dog"
print("The index number of fox is : ", str1.index("dog"))


# In Keyword for chrcking the sub-scring exsits ot not.
str2="Arbind is a bad boy. He is working in the ECPL."
substr= "ECPL"
print(substr in str2)
print("eCPL" in str2)

