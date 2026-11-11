#Name:Santi Salais
#Class: 5th Hour
#Assignment: HW16

import time
#1. import the "random" library
import random


#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
sumvar1 = (a + b) / c
print(sumvar1)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
roundvar = round(sumvar1)
if roundvar % 2 == 0:
    print("Even")
else:
    print("Odd")
#6. Create a list of five different random integers between 1 and 10.
list1 = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
print(list1)
#7. Print the 4th number in the list.
print(list1[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
appendvar = random.randint(1, 10)
list1.append(appendvar)
print(list1)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
list1.sort()
print(list1)
print(list1[3])

#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
x = 0
while x < 100:
    x += 1
    print(x)
    if x > 100:
        break
#11. Create a list containing the names of five other students in the classroom.
list2 = ["Anthony", "Jake", "oliver", "wyatt", "Ethan"]
#12. Create a for loop that individually prints out the names of each student in the list.
for x in list2:
    print(x)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for x in range(1, 100,):
    print(x)
    time.sleep(0.2)
    if x % 10 == 0:
        break
#14. Free space. Do something creative. :)
print("welcome to 67 calculator enter 2 numbers.")
input("What do you want to do, add, sub, multiply, divide?")
calc = int(input("First number: "))
calc67 = int(input("2nd number: "))

print(67)

