#Name:Santiago Salais
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!
print("Hello World")
#1. Create a list with 5 strings containing 5 different names in it.
ListVar1 = ["Santi", "Wyatt", "anthony", "jake", "oliver"]
print(ListVar1[3])
#2. Append a new name onto the Name List.
ListVar1.append(input("insert person name: "))
#3. Print out the 4th name on the list.
print(ListVar1)
#4. Create a list with 4 different integers in it.
ListVar2 = [1, 2, 3, 4]
#5. Insert a new integer into the 2nd spot and print the new list.
ListVar2.insert(1,6)
print(ListVar2)
#6. Sort the list from lowest to highest and print the sorted list.
ListVar2.sort()
print(ListVar2)
#7. Add the 1st three numbers on the sorted list together and print the sum.
ListVar3 =ListVar2[0] + ListVar2[1] + ListVar2[2]
print(ListVar3)
#8. Create a list with two strings, two integers, and two boolean values.
ListVar4 =["hi", "cool", 6, 7, True, False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(ListVar4[int(input("input number: "))])
print(ListVar4)