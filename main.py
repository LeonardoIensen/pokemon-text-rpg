import os
import dialogue

while True:
    print("\n--- POKEMON RPG ---")
    print("\n1- NEW GAME")
    print("2- QUIT\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        os.system("cls")
        player_name = dialogue.intro()
    elif choice == "2":
        print("\nExiting the game...\n")
        break
    else:
        print("\nInvalid option, please try again...\n")