import random
import dialogue
import pokemon
import battle
import menu

GRASS_ENCOUNTER_CHANCE = 85

def pokemon_center(player_pokemon):
    dialogue.clear_screen()
    dialogue.narration("\nWelcome to the POKEMON CENTER!")

    player_pokemon.current_hp = player_pokemon.max_hp
    
    dialogue.narration("\nYour POKEMON were fully healed!")
    dialogue.next_dialogue()

def wild_encounter(player_name, player_pokemon, pokemon_names, min_level, max_level, weights=None):
    dialogue.clear_screen()
    dialogue.narration(f"\n{player_name} walked through the tall grass...")

    encounter_roll = random.randint(1, 100)

    if encounter_roll <= GRASS_ENCOUNTER_CHANCE:
        if weights is not None:
            wild_name = random.choices(pokemon_names, weights=weights, k=1)[0]

        else:
            wild_name = random.choice(pokemon_names)

        wild_level = random.randint(min_level, max_level)

        wild_pokemon = pokemon.Pokemon(wild_name, wild_level)

        battle_result = battle.wild_battle(player_name, player_pokemon, wild_pokemon)

        return battle_result
    
    else:
        dialogue.narration("\nNothing appeared.")
        dialogue.next_dialogue()

        return None
    
def handle_viridian_defeat(player_name, player_pokemon):
    dialogue.narration(f"\n{player_name} returned to Viridian City...")
    dialogue.next_dialogue()

    pokemon_center(player_pokemon)

    city_result = viridian_city(player_name, player_pokemon)

    if city_result == "TITLE":
        return "TITLE"

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
                
                city_result = viridian_city(player_name, player_pokemon)

                if city_result == "TITLE":
                    return "TITLE"

                break

        elif choice == "2":
            battle_result = wild_encounter(player_name, player_pokemon, ["RATTATA", "PIDGEY"], 2, 5)

            if battle_result == "LOSE":
                player_pokemon.current_hp = player_pokemon.max_hp
                steps = 0

                dialogue.narration(f"\n{player_name} returned home to rest...")
                dialogue.narration(f"\n{player_name}'s POKEMON recovered!")
                dialogue.next_dialogue()
                    
                continue

        elif choice == "3":
            menu_result = menu.player_menu(player_pokemon)

            if menu_result == "TITLE":
                return "TITLE"

        else:
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()
            
def viridian_city(player_name, player_pokemon):

    dialogue.clear_screen()

    while True:

        print("\n--- VIRIDIAN CITY ---\n")

        print("1 - GO NORTH TO ROUTE 2")
        print("2 - RETURN TO ROUTE 1")
        print("3 - POKEMON CENTER")
        print("4 - MENU")

        choice = input("\nChoose: ")

        if choice == "1":
            dialogue.clear_screen()
            dialogue.narration(f"\n{player_name} arrived in Route 2!")
            dialogue.next_dialogue()
                
            route_result = route_2(player_name, player_pokemon)

            if route_result == "TITLE":
                return "TITLE"

            break

        elif choice == "2":
            dialogue.clear_screen()
            dialogue.narration(f"\n{player_name} returned to Route 1.")
            dialogue.next_dialogue()

            route_result = route_1(player_name, player_pokemon)

            if route_result == "TITLE":
                return "TITLE"

            break

        elif choice == "3":
            pokemon_center(player_pokemon)

        elif choice == "4":
            menu_result = menu.player_menu(player_pokemon)

            if menu_result == "TITLE":
                return "TITLE"

        else:
            dialogue.clear_screen()
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()

def route_2(player_name, player_pokemon):

    steps = 0

    dialogue.clear_screen()

    while True:

        print("\n--- ROUTE 2 ---")
        print(f"Progress: {steps}/8\n")

        print("1 - WALK")
        print("2 - WALK ON THE GRASS")
        print("3 - RETURN TO VIRIDIAN CITY")
        print("4 - MENU")

        choice = input("\nChoose: ")

        if choice == "1":
            dialogue.clear_screen()

            steps += 1

            dialogue.narration(f"\n{player_name} walked through Route 2... ({steps}/8)")
            dialogue.next_dialogue()

            if steps >= 8:
                dialogue.narration(f"\n{player_name} reached the entrance of Viridian Forest.")
                dialogue.next_dialogue()

                forest_result = viridian_forest(player_name, player_pokemon)

                if forest_result == "TITLE":
                    return "TITLE"

                break

        elif choice == "2":
            battle_result = wild_encounter(player_name, player_pokemon, ["RATTATA", "PIDGEY", "MANKEY", "SPEAROW"], 3, 7, [30, 30, 20, 20])

            if battle_result == "LOSE":
                defeat_result = handle_viridian_defeat(player_name, player_pokemon)

                if defeat_result == "TITLE":
                    return "TITLE"

                break

        elif choice == "3":
            dialogue.clear_screen()
            dialogue.narration(f"\n{player_name} returned to Viridian City!")
            dialogue.next_dialogue()
            
            city_result = viridian_city(player_name, player_pokemon)

            if city_result == "TITLE":
                return "TITLE"

            break

        elif choice == "4":
            menu_result = menu.player_menu(player_pokemon)

            if menu_result == "TITLE":
                return "TITLE"

        else:
            dialogue.clear_screen()
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()

def viridian_forest(player_name, player_pokemon):

    steps = 0

    dialogue.clear_screen()

    while True:

        print("\n--- VIRIDIAN FOREST ---")
        print(f"Progress: {steps}/10\n")

        print("1 - WALK")
        print("2 - WALK ON THE GRASS")
        print("3 - RETURN TO ROUTE 2")
        print("4 - MENU")

        choice = input("\nChoose: ")

        if choice == "1":
            dialogue.clear_screen()

            steps += 1

            dialogue.narration(f"\n{player_name} walked deeper into Viridian Forest... ({steps}/10)")
            dialogue.next_dialogue()

            if steps >= 10:
                dialogue.clear_screen()
                dialogue.narration(f"\n{player_name} reached the exit of Viridian Forest!")
                dialogue.next_dialogue()

                route_result = route_3(player_name, player_pokemon)

                if route_result == "TITLE":
                    return "TITLE"

                break

        elif choice == "2":
            battle_result = wild_encounter(player_name, player_pokemon, ["CATERPIE", "WEEDLE", "PIKACHU"], 4, 6, [45, 45, 10])

            if battle_result == "LOSE":
                defeat_result = handle_viridian_defeat(player_name, player_pokemon)

                if defeat_result == "TITLE":
                    return "TITLE"

                break

        elif choice == "3":
            dialogue.clear_screen()
            dialogue.narration(f"\n{player_name} returned to Route 2!")
            dialogue.next_dialogue()
            
            route_result = route_2(player_name, player_pokemon)

            if route_result == "TITLE":
                return "TITLE"

            break

        elif choice == "4":
            menu_result = menu.player_menu(player_pokemon)

            if menu_result == "TITLE":
                return "TITLE"

        else:
            dialogue.clear_screen()
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()

def route_3(player_name, player_pokemon):

    steps = 0

    dialogue.clear_screen()

    while True:

        print("\n--- ROUTE 3 ---")
        print(f"Progress: {steps}/5\n")

        print("1 - WALK")
        print("2 - WALK ON THE GRASS")
        print("3 - RETURN TO VIRIDIAN FOREST")
        print("4 - MENU")

        choice = input("\nChoose: ")

        if choice == "1":
            dialogue.clear_screen()

            steps += 1

            dialogue.narration(f"\n{player_name} walked through Route 3... ({steps}/5)")
            dialogue.next_dialogue()

            if steps >= 5:
                dialogue.narration(f"\n{player_name} arrived in Pewter City.")
                dialogue.next_dialogue()

                city_result = pewter_city(player_name, player_pokemon)

                if city_result == "TITLE":
                    return "TITLE"

                break

        elif choice == "2":
            battle_result = wild_encounter(player_name, player_pokemon, ["RATTATA", "PIDGEY", "MANKEY", "SPEAROW"], 4, 8, [30, 30, 20, 20])

            if battle_result == "LOSE":
                dialogue.narration(f"\n{player_name} was taken to the nearest POKEMON CENTER...")
                dialogue.next_dialogue()

                pokemon_center(player_pokemon)

                city_result = pewter_city(player_name, player_pokemon)

                if city_result == "TITLE":
                    return "TITLE"

                break

        elif choice == "3":
            dialogue.clear_screen()
            dialogue.narration(f"\n{player_name} returned to Viridian Forest!")
            dialogue.next_dialogue()
            
            forest_result = viridian_forest(player_name, player_pokemon)

            if forest_result == "TITLE":
                return "TITLE"

            break

        elif choice == "4":
            menu_result = menu.player_menu(player_pokemon)

            if menu_result == "TITLE":
                return "TITLE"

        else:
            dialogue.clear_screen()
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()

def pewter_city(player_name, player_pokemon):

    dialogue.clear_screen()

    while True:

        print("\n--- PEWTER CITY ---\n")

        print("1 - POKEMON CENTER")
        print("2 - RETURN TO ROUTE 3")
        print("3 - GYM")
        print("4 - MENU")

        choice = input("\nChoose: ")

        if choice == "1":
            pokemon_center(player_pokemon)

        elif choice == "2":
            dialogue.clear_screen()
            dialogue.narration(f"\n{player_name} returned to Route 3.")
            dialogue.next_dialogue()

            route_result = route_3(player_name, player_pokemon)

            if route_result == "TITLE":
                return "TITLE"

            break

        elif choice == "3":
            dialogue.clear_screen()
            dialogue.narration("\nPEWTER GYM's doors are locked.")
            dialogue.next_dialogue()

        elif choice == "4":
            menu_result = menu.player_menu(player_pokemon)

            if menu_result == "TITLE":
                return "TITLE"

        else:
            dialogue.clear_screen()
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()