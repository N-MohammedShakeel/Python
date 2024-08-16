# Data Types

#PEMDASLR 
# ()      |  first
# **      |  Precedence
# * /     |  Precedence
# + -     |  last
#        \ /
#Integers
#Integers are whole numbers.

my_number = 354

#Floating Point Numbers
#Floats are numbers with decimal places.
#When you do a calculation that results in
#a fraction e.g. 4 ÷ 3 the result will always be
#a floating point number.

my_float = 3.14159

#Strings
#A string is just a string of characters.
#It should be surrounded by double quotes.

my_string = "Hello"

#Boolean

a = True
b = False

#Escaping a String
#Because the double quote is special, it
#denotes a string, if you want to use it in
#a string, you need to escape it with a "\"

speech = "She said: \"Hi\"" #prints: She said: "Hi"
print(speech)


#Checking Data Types
#You can use the type() function to check what is the data type of a particular variable.
n = "ms"
print(type(n)) #result str

n = 1
print(type(n)) #result int

n = 3.14159
print(type(n)) #result float

n = True
print(type(n)) #result bool


#Floor Division 
print(8 // 3)

#Round of to n decimal
print(round(2.666666,2))   #Rounds of to 2 decimal


#Operators

x = 1
y = 2

x += y
x -= y
x *= y
x /= y


#F-Strings
#You can insert a variable into a string using f-strings.
#The syntax is simple, just insert the variable in-between a set of curly braces {}.

days = 365
print(f"There are {days} in a year")




#Living Calculator
age = int(input("Enter your age: "))
years = 90 - age
print(f"You have {years * 365} Days , {years*12} Months , {years*52} Weeks and {years} Years to live ")


#BMI Calculator

h = float(input("Enter your height: "))
w = float(input("Enter your weight: "))
bmi = (w/(h*h)) # height should be in meters
print("Your BMI is: " + str(bmi))


# Adding Numbers

two_digit  = input("Enter a two digit number: ")
ans  = two_digit[0] + two_digit[1]
print("The Added value is: " + ans)
 


# Bill Splitter

print("Restaurent Bill Splitter")
bill = float(input("What is your Bill: "))
tip = float(input("Choose how much you going to tip 10,15,20: "))
Total = bill + tip
print("Your total bill is: " + str(Total))
splits = int(input("How many people to split the bill ? : "))
print("Each person should pay : " + str((Total)/splits))


