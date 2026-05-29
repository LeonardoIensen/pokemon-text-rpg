import os
import dialogue
import pokemon
import battle

while True:

    print("--- POKEMON RPG ---")
    print("\n1- NEW GAME")
    print("2- QUIT\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        os.system("cls")

        player_name, rival_name = dialogue.intro()

        dialogue.start_journey(player_name, rival_name)

        player_starter = pokemon.choose_starter(player_name)
        rival_starter = pokemon.choose_rival_starter(player_starter, rival_name)

        battle.rival_first_battle(player_name, player_starter, rival_name, rival_starter)

        dialogue.next_dialogue()

    elif choice == "2":
        print("\nExiting the game...\n")
        break

    else:
        print("\nInvalid option, please try again...\n")