import dialogue
import pokemon
import battle
import map as game_map

while True:

    print("--- POKEMON RPG ---")
    print("\n1- NEW GAME")
    print("2- QUIT\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        dialogue.clear_screen()

        player_name, rival_name = dialogue.intro()

        dialogue.start_journey(player_name, rival_name)

        player_starter = pokemon.choose_starter(player_name)
        rival_starter = pokemon.choose_rival_starter(player_starter, rival_name)

        battle.rival_first_battle(player_name, rival_name, player_starter, rival_starter)

        player_starter.current_hp = player_starter.max_hp

        dialogue.narration(f"\nAfter the battle, {player_name} left Professor Oak's Lab.")
        dialogue.narration("\nWith a POKEMON by your side, your journey was finally about to begin.")
        dialogue.next_dialogue()

        game_map.route_1(player_name)

    elif choice == "2":
        print("\nExiting the game...\n")
        break

    else:
        print("\nInvalid option, please try again...\n")