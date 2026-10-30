#santi salais

import random
def meteor2():
    print("You see a cave, a building, and a tree. which do you hide in/under. 1/2/3 (if 2 enter twice if 3 enter three times")
    if int(input("").lower()) == 1:
        print("You hide in the cave..... Good Choice! you wait out the meteor shower in the cave. YOU WIN!")
    elif int(input("").lower()) == 2:
        print("the building shakes and you get hit by debris and die! oh no!... RESTART GAME")
    elif int(input("").lower()) == 3:
        print("BAD CHOICE! you hid under the tree and a meteor hit it!. You get flattened by the tree. you die.."
              "RESTART  GAME")

def meteor3():
    print("What do you do? Go look for food?, Go hunting?, wait the night out 1/2/3 (type 2 twice, 3 three times) ")
    if int(input("").lower()) == 1:
        print("You find blueberrys! they were poisonous. RESTART GAME")
    elif int(input("").lower()) == 2:
        print("You manage to kill a deer for food! you survive the night. YOU WIN!")
    elif int(input("").lower()) == 3:
        print("You die to starvation... RESTART GAME")

def meteor4():
    print("You see an open field, a tree and a wood hut 1/2/3 (if 2 enter twice if 3 enter three times")
    if int(input("").lower()) == 1:
        print("You almost get struck, but survive... YOU WIN!")
    elif int(input("").lower()) == 2:
        print("The tree gets struck! you die from the inital strike... RESTART GAME")
    elif int(input("").lower()) == 3:
        print("The wooden hut gets struck, it catches on fire! you die to the fire... RESTART GAME")

def meteor5():
    print("YOU WIN")

def meteor6():
    print("RESTART GAME")

def meteor7():
    print("You see a building, a forest, and a hole 1/2/3 (if 2 enter twice if 3 enter three times")
    if int(input("").lower()) == 1:
        print("The building had a basement, you survive!.... YOU WIN!")
    elif int(input("").lower()) == 2:
        print("The trees topple down and u get flattened... RESTART GAME")
    elif int(input("").lower()) == 3:
        print("The tornado sucks you out of the hole and throws you!... RESTART GAME")







print("Welcome to SANDBOX!, here you are going to play a game full of disasters.. WOW! enter 1 if you'd like to play.. 2 if you want to leave.")

if int(input("").lower()) == 1:
    print("disaster time!")
elif int(input("").lower()) == 2:
    print("Too bad")
else:
    print("THATS NOT AN OPTION!... RESTART GAME")





print("DAY 1, you land in a forest when suddenly A DISASTER STRIKES!")


disaster1 = random.randint(1,6)
if disaster1 == 1:
    print("WATCH OUT! METEOR SHOWER!")

    meteor2()
elif disaster1 == 2:
    print("Oh no! you're out of food!")
    meteor3()
elif disaster1 == 3:
    print("Thunderstorm! look out for lightning!")
    meteor4()
elif disaster1 == 4:
    print("You're safe!.. for now...")
    meteor5()
elif disaster1 == 5:
    print("You died from breathing air. tough luck.")
    meteor6()
elif disaster1 == 6:
    print("TORNADO!")
    meteor7()












