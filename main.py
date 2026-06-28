import dialogue
import pokemon
import battle
import map as game_map

while True:
    dialogue.clear_screen()

    print("\n--- POKEMON RPG ---")
    print("\n1 - NEW GAME")
    print("2 - QUIT\n")

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

        game_result = game_map.route_1(player_name, player_starter)

        if game_result == "TITLE":
            continue

    elif choice == "2":
        dialogue.clear_screen()
        dialogue.narration("\nExiting the game...\n")
        dialogue.next_dialogue()
        break

    else:
        dialogue.clear_screen()
        dialogue.narration("\n[Invalid option! Please select again.]")
        dialogue.next_dialogue()