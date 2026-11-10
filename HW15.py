#Name:Santiago Salais
#Class: 5th Hour
#Assignment: HW15

import time

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
a = 5
for a in range(5, 0, -1):
    time.sleep(0.4)
    print(a)
else:
    print("Hello World!")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
b = 1
for b in range(1, 31):
    if b % 2 == 0:
        print(b)
    else:
        continue
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
c = 1
for c in range(1, 30):
    if c % 3 == 0:
        continue
    else:
        print(c)
#4. Create a for loop that prints 5 different animals from a list.
for x in ["cat", "dog", "rat", "fish", "hampter"]:
    print(x)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
word= input("Give me a word")
backwardsword = word[::-1]
for x in backwardsword:
    print(x)
#6. Create a list containing 10 integers of your choice and print the list.
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = []
oddNumbers = []
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for number in list1:
    if number % 2 == 0:
        evenNumbers.append(number)

    else :
        oddNumbers.append(number)


print(evenNumbers)
print(oddNumbers)

#9. Create a variable that asks the user for an integer and an empty integer variable.
var0var = int(input("Give me an integer"))
emptyinteger = 1
var1 = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)

for var in range(1, var0var+ 1):
    emptyinteger= emptyinteger * var
    print(emptyinteger)