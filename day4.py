# Builtin function 
#range
#Randamization
#round
#abs

#Randomisation
#The random functions come from the random module which needs to be imported.
#In this case, the start and end are both included
#start <= randint <= end
import random
# randint(start, end)

#n can be 2, 3, 4 or 5.
n = random.randint(2,5)
print(n)


#Round
#This does a mathematical round.
#So 3.1 becomes 3, 4.5 becomes 5 and 5.8 becomes 6.
ans = round(4.6) # result 5

#abs
#This returns the absolute value.
#Basically removing any -ve signs. 
ans = abs(-4.6) # result 4.6


#Modules

#Aliasing
#You can use the as keyword to give your module a different name.
import random as r
n = r.randint(1, 5)

#Importing
#Some modules are pre-installed with python
#e.g. random/datetime
#Other modules need to be installed from pypi.org
import random
n = random.randint(3, 10)

#Importing from modules
#You can import a specific thing from a module. e.g. a function/class/constant
#You do this with the from keyword.
#It can save you from having to type the same thing many times.
from random import randint
n = randint(1, 5)

#Importing Everything
#You can use the wildcard (*) to import everything from a module. Beware, this usually reduces code readability.
from random import *
list = [1, 2, 3]
choice(list)
# More readable/understood
random.choice(list)



import Module1_day4
#The Module1_day4 python file is used as a module file 

print(f"My name is {Module1_day4.name} and I am {Module1_day4.age} years old")



# List
l = [1,2,3,"hello","world"]

#List Methods

#Adding Lists Together
#You can extend a list with another list by using the extend keyword, or the + symbol.
list1 = [1, 2, 3]
list2 = [9, 8, 7]
new_list = list1 + list2
print(new_list)
list1 += list2
print(list1)



#Adding an Item to a List
#If you just want to add a single item to a list, you need to use the .append() method.
all_fruits = ["apple","banana", "orange"]
all_fruits.append("pear")

#List Index
#To get hold of a particular item from a list you can use its index number.
#This number can also be negative, if you want to start counting from the end of the list.

letters = ["a", "b", "c"]
letters[0]
#Result:"a"
letters[-1]
#Result: "c"


#List Slicing
#Using the list index and the colon symbol you can slice up a list to get only the portion you want.
#Start is included, but end is not.
#list[start:end]

letters = ["a","b","c","d"]
letters[1:3]
#Result: ["b", "c"]



#Toss
n = random.randint(1,10)

if(n%2 == 0):
    print("Tails")
else:
    print("Heads")    
