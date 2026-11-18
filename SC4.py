#Name:santi salais
#Class: 5th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

playercount = int(input("How many players"))
total = 0
for i in range(1, playercount):
    rate = int(input("What would you like to rate them?"))
    while not 5 > rate > 0:
        print("Please enter a number between 1 and 5 Rate again")
        rate = int(input("What would you like to rate them?"))
    else:
        total+=rate
print(total / (playercount - 1))