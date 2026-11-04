#Name:Santiago Salais1
#Class: 5th Hour
#Assignment: HW14
import random
import time
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    time.sleep(0.2)
    i -= 1
else:
    print("Hello World!")

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
j = 1
while j < 30:
    j += 1
    if j % 2 == 0:
        print(j)
    time.sleep(0.2)

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
x = 1
while x <30:
     x +=1
     if x % 3 == 0:
        continue
     time.sleep(0.2)
     print(x)

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
while True:
    z = random.randint(1, 6)
    print(z)
    if z == 1:
        break



#5. Create a while loop that asks for a number input until the user inputs the number 0.
while True:
    print("enter a number")
    intinput = input()
    if intinput == "0":
        break