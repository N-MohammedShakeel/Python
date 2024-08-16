# Basics

#Comments
#Adding a # symbol in font of text , lets you make comments on a line of code.
#The computer will ignore your comments.

#Print
#Prints a string into the console.

print("Hello World")
print("('What to print')")
print("Hello \n Hello \n Hello")


#String Concatenation
#You can add strings to string to create
#a new string. This is called concatenation.
#It results in a new string.

#becomes "Helloms"

print("Hello" + "ms")
print(str(1) + str(0))

#Input
#Prints a string into the console,and asks the user for a string input.

print("Hello " + input("What is your name: "))

#Variables
#A variable give a name to a piece of data.
#Like a box with a label, it tells you what's inside the box.

a = input("Give your name: \n")
print("Your name is " + a)

#Converting Data Types
#You can convert a variable from one data type to another.
#Converting to float:
#float()

#Converting to int:
#int()

#Converting to string:
#str()


print( "Length of your name is: " + str(len(input("What is your name: ") )) ) 

#Swapping 

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: "+ str(a))
print("b: "+ str(b))


# Brand generator

print(" Brand Generator ")
a = input("Give your name: \n")
print("Your name is " + a)
b = input("Give your Nick name: \n")
print("Your nickname is: " + b)
print("Your Brand Name is: " + a + " " + b)