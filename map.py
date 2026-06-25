import random
import dialogue
import pokemon
import battle

GRASS_ENCOUNTER_CHANCE = 85

def pokemon_center(player_pokemon):
    dialogue.clear_screen()

    dialogue.narration("\nWelcome to the POKEMON CENTER!")

    player_pokemon.current_hp = player_pokemon.max_hp
    
    dialogue.narration("\nYour POKEMON were fully healed!")

    dialogue.next_dialogue()

def route_1(player_name, player_pokemon):

    steps = 0

    dialogue.clear_screen()

    while True:

        print("\n--- ROUTE 1 ---")
        print(f"Progress: {steps}/5\n")

        print("1 - WALK")
        print("2 - WALK ON THE GRASS")
        print("3 - MENU")

        choice = input("\nChoose: ")

        if choice == "1":
            dialogue.clear_screen()

            steps += 1

            dialogue.narration(f"\n{player_name} walked through Route 1... ({steps}/5)")
            dialogue.next_dialogue()

            if steps >= 5:
                dialogue.narration(f"\n{player_name} arrived in Viridian City!")
                dialogue.next_dialogue()
                
                viridian_city(player_name, player_pokemon)
                break

        elif choice == "2":
            dialogue.clear_screen()

            dialogue.narration(f"\n{player_name} walked through the tall grass...")

            wild_pokemon_encounter = random.randint(1, 100)

            wild_pokemon_level = random.randint(2, 4)

            if wild_pokemon_encounter <= GRASS_ENCOUNTER_CHANCE:
                wild_name = random.choice(["RATTATA", "PIDGEY"])

                wild_pokemon = pokemon.Pokemon(wild_name, wild_pokemon_level)

                battle_result = battle.wild_battle(player_name, player_pokemon, wild_pokemon)

                if battle_result == "LOSE":
                    player_pokemon.current_hp = player_pokemon.max_hp
                    steps = 0

                    dialogue.narration(f"\n{player_name} returned home to rest...")
                    dialogue.narration(f"\n{player_name}'s POKEMON recovered!")
                    dialogue.next_dialogue()
                    
                    continue

            else:
                dialogue.narration("\nNothing appeared.")
                dialogue.next_dialogue()

        elif choice == "3":
            dialogue.clear_screen()

            print("\nMenu is not available yet.")
            dialogue.next_dialogue()

        else:
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()
            
def viridian_city(player_name, player_pokemon):

    dialogue.clear_screen()

    while True:

        print("\n--- VIRIDIAN CITY ---")

        print("1 - GO NORTH TO ROUTE 2")
        print("2 - RETURN TO ROUTE 1")
        print("3 - POKEMON CENTER")
        print("4 - MENU")

        choice = input("\nChoose: ")

        if choice == "1":
            dialogue.clear_screen()

            dialogue.narration("\nRoute 2 is not available yet.")
            dialogue.next_dialogue()

        elif choice == "2":
            dialogue.clear_screen()
            
            dialogue.narration(f"\n{player_name} returned to Route 1.")
            dialogue.next_dialogue()

            route_1(player_name, player_pokemon)

            break

        elif choice == "3":
            pokemon_center(player_pokemon)

        elif choice == "4":
            dialogue.clear_screen()

            print("\nMenu is not available yet.")
            dialogue.next_dialogue()

        else:
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()