#Name:Santiago Salais
#Class: 5th Hour
#Assignment: HW6

print("hello world")

#1. Create a list with 9 different numbers inside.
ListVar1 = [1,2,3,4,5,6,7,8,9]
#2. Sort the list from highest to lowest.
ListVar1.sort(reverse=True)
#3. Create an empty list.
ListVar2 = []
#4. Remove the median number from the first list and add it to the second list.
taco=ListVar1.pop(4)
ListVar2.append(taco)
#5. Remove the first number from the first list and add it to the second list.
happy=ListVar1.pop(0)
ListVar2.append(happy)
#6. Print both lists.
print(ListVar1)
print(ListVar2)
#7. Add the two numbers in the second list together and print the result.
sumListVar2 = ListVar2[0] + ListVar2[1]
print(sumListVar2)
#8. Add the sum from #7 to the first list.
ListVar1.append(sumListVar2)
#9. Sort the first list from lowest to highest and print it.
ListVar1.sort()
print(ListVar1)