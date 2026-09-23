#Name:Santiago Salais
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library
import random
#2. print "Hello World!"
print("hello world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
hi = random.randint(1,10)
taco = random.randint(1,10)
burger = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(hi, taco, burger)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
hiplus2 = hi + 2
tacominus4 = taco - 4
burgermultiply = burger * 1.5
#6. Print each result from #5 on the same line.
print(hiplus2, tacominus4, burgermultiply)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
List1 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#8. Sort the list in #7 and print it.
List1.sort()
print(List1)
#9. Add together the highest three numbers in the list from #7 and print the result.
sum1 = List1[1] + List1[2] + List1[3]
print(sum1)
#10. Create a list with 5 names of other students in this class and print the list.
List2 = ["anthony", "Jake", "wyatt", "oliver","max"]
print(List2)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(List2)
print(List2)
#12. Print a random choice from the list of names from #10.
print(random.choice(List2))