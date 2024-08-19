#Loop


#While Loop
#This is a loop that will keep repeating itself until the while condition becomes false.
n = 1
while n < 10:
  n += 1
  print(n)


#For Loop
#For loops give you more control than while loops. You can loop through anything that is iterable. e.g. a range, a list, a dictionary or tuple.
fruits = ["apple","banana", "orange"]
for fruit in fruits:
  print(fruit)  


#_ in a For Loop
#If the value your for loop is iterating through,
#e.g. the number in the range, or the item in the list is not needed, you can replace it with an underscore.
for _ in range(10):
  #Do something 10 times. 
  print(_) 


#break
#This keyword allows you to break free of the loop. You can use it in a for or while loop.
scores = [34, 67, 99, 105]
for s in scores:
      if s > 100:
           print("Invalid")
           break
      print(s)
    
  
#continue
#This keyword allows you to skip this iteration of the loop and go to the next. The loop will still continue, but it will start from the top.
n = 0
while n < 100:
  n += 1
  if n % 2 == 0:
    continue
  print(n) #Prints all the odd numbers  


#Infinite Loops
#Sometimes, the condition you are checking to see if the loop should continue never becomes false. In this case, the loop will continue for eternity (or until your computer stops it). This is more common with while loops.

#    while 5 > 1: 
#      print("I'm a survivor")  
  



# Average Height of the students in the class 
# without using sum() and len()
# split() is used to split the input passed for each spaces
# Also find max height
total_h = 0
num = 0
max = 0
students_h = input("Tell the students height: ").split()
for i in range(0 , len(students_h)):
  students_h[i] = int(students_h[i]) 
  total_h += int(students_h[i])
  num += 1
  if (max < int(students_h[i])): 
    max = int(students_h[i])
print(students_h)

print(f"The average height of the students is {total_h/num}")
print(f"The max height is {max}")


#Create a password 
import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@','#','$','%','^','&','*','(',')','_']

print("Welcome to the Password Generator")
nl = int(input("How many letters would you like in your password? "))
nn = int(input("How many numbers would you like in your password? "))
ns = int(input("How many symbols would you like in your password? "))

password_list = []

for i in range(nl): 
   password_list.append(random.choice(letters))

for i in range(nn): 
   password_list.append(random.choice(numbers))

for i in range(ns): 
   password_list.append(random.choice(symbols))

password = ''.join(password_list)

random.shuffle(password_list)

password = ''.join(password_list)

print(f"Your password is {password}")


