#Condition Statements



#comparison operators
#These mathematical comparison operators allow you to refine your conditional checks.
#> Greater than
#< Lesser than
#>= Greater than or equal to
#<= Lesser than or equal to
#== Is equal to
#!= Is not equal to


#if
#This is the basic syntax to test if a condition is true. If so, the indented code will be executed, if not it will be skipped.

#else
#This is a way to specify some code that will be executed if a condition is false.

age = int( input("What is your age: "))

if age > 18:
    print("You can drive")
else:
    print("You can't drive")



#elif 
#In addition to the initial If statement condition, you can add extra conditions to test if the first condition is false.
#Once an elif condition is true, the rest of the elif conditions are no longer checked and are skipped.

n = int(input("Enter a number: "))

if n == 0:
    print("You given zero")
elif n > 0:
    print("You given Positive integer")
else:
    print("You given Negative integer")



# Multiple if condition

n = int(input("What is your Bill"))

if n > 1500: 
    print("You got a free cake")
if n <= 1000:
    print("You got a free water Bottle")
if n <= 500:
    print("You got free toothpicks")        



#Nested if-else

age = int( input("What is your age: "))
weight= int( input("What is your weight: "))

if age > 18 :
    if weight < 50:
        print("Pay 40 dollor")    
    else: 
        print("Pay 50 dollor")
else:
    print("Pay 20 dollor")     

#and
#This expects both conditions either side of the and to be true.
s = 58
if s < 60 and s > 50:
  print("Your grade is C")

#or
#This expects either of the conditions either side of the or to be true. Basically, both conditions cannot be false.
age = 12
if age < 16 or age > 200:
  print("Can't drive")  
    

#not
#This will flip the original result of the
#condition. e.g. if it was true then it's now false.
if not 3 == 1:
 print("something")  



#Finding even numbers 

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is even")
else: 
    print("Number is odd")   


#Leap Year

y = int(input("Enter the year: "))

if y%4 == 0 :
    if y % 100 == 0:
        if y%400 == 0:
            print("It is leap year")
        else: 
            print("It is not a leap year") 
    else:
         print("It is leap year")    
else: 
     print("It is not a leap year")         


# Pizza Bill generator

size = input("What size do you want S , M and L: ")
pepparoni = input("Do you need pepparoni Y and N: ")
cheese = input("Do you need cheese Y and N: ")   
bill = 0

if size == "S" or size == "s":
    bill += 100
    if pepparoni == "Y" or pepparoni == "y" : 
        bill += 20
        if cheese == "Y" or cheese == "y" : 
            bill += 20
        else:
            bill += 0     
    else: 
        bill += 0    
elif size == "M" or size == "m":
    bill += 150
    if pepparoni == "Y" or pepparoni == "y" : 
        bill += 20
        if cheese == "Y" or cheese == "y" : 
            bill += 20
        else:
            bill += 0     
    else: 
        bill += 0    
else: 
    bill += 200
    if pepparoni == "Y" or pepparoni == "y" : 
        bill += 20
        if cheese == "Y" or cheese == "y" : 
            bill += 20
        else:
            bill += 0     
    else: 
        bill += 0    

print(f"Your total bill is {bill} ")        


# Using 
# count() - used to count the sub string in the string 
# lower() - convert the entire string to lower case letters and vice versa for upper()

# Love Calculator

name1 = input("What is your name: ")
name2 = input("what is your crush name: ")

n = name1.lower() + name2.lower()

t = n.count("t")
r = n.count("r")
u = n.count("u")
e = n.count("e")

true = t+r+u+e

l = n.count("l")
o = n.count("o")
v = n.count("v")
e = n.count("e")

love = l+o+v+e

percentage = str(true) + str(love)

if int(percentage) > 80: 
    print(f"{percentage}% lovers")
elif int(percentage) > 50:
    print(f"{percentage}% Crush")
else: 
    print(f"{percentage}% Try ")        