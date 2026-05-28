import os
import dialogue
import pokemon

while True:
    print("--- POKEMON RPG ---")
    print("\n1- NEW GAME")
    print("2- QUIT\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        os.system("cls")
        player_name, rival_name = dialogue.intro()
        dialogue.start_journey(player_name, rival_name)
        starter = pokemon.choose_starter()
        starter.show_stats()
        dialogue.next_dialogue()
    elif choice == "2":
        print("\nExiting the game...\n")
        break
    else:
        print("\nInvalid option, please try again...\n")