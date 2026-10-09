#Name:Santiago Salais
#Class: 5th Hour
#Assignment: HW12
from operator import truediv

#1. Print Hello World!
print("hello world")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = False
admin = True
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
varint = 0
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == True:
    if login == True:
        if admin == True:
            print("Login Successful")
            varint += 1
        else :
            print("Login failed, admin missing")
    else:
        print("Login failed, login missing")
else:
    print("Login failed, wifi missing")