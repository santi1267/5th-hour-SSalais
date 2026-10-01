#Name:Santiago Salais
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.
The_Null = {
    'null_soldier' : {
        'Damage' : 3,
        'Speed' : 5,
        'Hp' : 32,

    },
    'null_soldier2' : {
        'Damage' : 7,
        'Speed' : 6,
        'Hp' : 56,
    },
    'null_commander' : {
        'Damage' : 10,
        'Speed' : 9,
        'Hp' : 75,
    },
    'Wraith' : {
        'Damage' : 34,
        'Speed' : 24,
        'Hp' : 112,
    },
    'Spokeishere' : {
        'Damage' : 85,
        'Speed' : 47,
        'Hp' : 537,
    }
}
print(The_Null)


The_Null['null_soldier'].update({'Damage' : int(input('Damage: '))})
The_Null['null_soldier2'].update({'Damage' : int(input('Damage: '))})
The_Null['null_commander'].update({'Damage' : int(input('Damage: '))})
The_Null['Wraith'].update({'Damage' : int(input('Damage: '))})
The_Null['Spokeishere'].update({'Damage' : int(input('Damage: '))})

print(The_Null)


#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.