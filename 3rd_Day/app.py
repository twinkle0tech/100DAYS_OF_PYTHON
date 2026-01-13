print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print(" Welcome to Treasure Island!")
print("Your mission is to find the hidden treasure.\n")

choice_1 = input(
    "You're standing at a lonely crossroad in the jungle.\n"
    "Do you want to go LEFT towards the dark forest or RIGHT towards the mountains?\n"
    "Type 'left' or 'right':\n"
).lower()

if choice_1 == "left":
    print("\n You walk into the dark forest. The trees whisper as the wind blows.")
    
    choice_2 = input(
        "After walking for hours, you reach a wide lake.\n"
        "In the middle of the lake, you see a small island.\n"
        "Do you WAIT for a boat or SWIM across?\n"
        "Type 'wait' or 'swim':\n"
    ).lower()

    if choice_2 == "wait":
        print("\n You patiently wait. A wooden boat slowly arrives and takes you to the island safely.")

        choice_3 = input(
            " You arrive at an ancient house with 3 mysterious doors.\n"
            "One RED, one YELLOW, and one BLUE.\n"
            "Which door do you choose?\n"
            "Type 'red', 'yellow', or 'blue':\n"
        ).lower()

        if choice_3 == "red":
            print("\n The room bursts into flames.")
            print("Game Over ")

        elif choice_3 == "blue":
            print("\n A nest of poisonous snakes attacks you.")
            print("Game Over ")

        elif choice_3 == "yellow":
            print("\n You enter a golden hall filled with light.")

            choice_4 = input(
                "In the hall, you see a glowing chest and a dark tunnel.\n"
                "Do you OPEN the chest or ENTER the tunnel?\n"
                "Type 'open' or 'enter':\n"
            ).lower()

            if choice_4 == "open":
                print("\n The chest opens and reveals the legendary treasure!")
                print(" YOU WIN! ")

            elif choice_4 == "enter":
                print("\n The tunnel collapses behind you.")
                print("Game Over ")

            else:
                print("\n Invalid choice. The island traps you forever.")
                print("Game Over ")

        else:
            print("\n Invalid choice. The doors vanish.")
            print("Game Over ")

    else:
        print("\n You try to swim, but a dangerous creature drags you underwater.")
        print("Game Over ")

elif choice_1 == "right":
    print("\n You walk toward the mountains.")
    print("A sudden landslide blocks your path.")
    print("Game Over ")

else:
    print("\n Invalid choice. You are lost forever.")
    print("Game Over ")
