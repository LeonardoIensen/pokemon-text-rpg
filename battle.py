import dialogue
import pokemon
import random

ESCAPE_CHANCE = 85

def calculate_damage(attacker, defender, move):

    power = pokemon.moves_data[move]["power"]
    
    damage = (((attacker.level * 2) // 5 + 2) * power * attacker.attack) // defender.defense
    damage = damage // 50 + 2

    return damage

def enemy_free_attack(player_pokemon, enemy_pokemon, player_name, enemy_name, battle_type):
    dialogue.clear_screen()

    enemy_move = random.choice(enemy_pokemon.moves)

    show_attack_message(enemy_pokemon, enemy_move, enemy_pokemon)

    enemy_damage = calculate_damage(enemy_pokemon, player_pokemon, enemy_move)

    player_pokemon.current_hp -= enemy_damage

    if player_pokemon.current_hp <= 0:
        return handle_faint(player_pokemon, player_pokemon, enemy_pokemon, player_name, enemy_name, battle_type)
    
    dialogue.next_dialogue()
    return None

def try_run(battle_type):

    if battle_type == "TRAINER":
        dialogue.clear_screen()

        dialogue.narration("\nNo! There's no running from a TRAINER battle!")
        dialogue.next_dialogue()

        return "FAILED"
    
    elif battle_type == "WILD":

        escape_roll = random.randint(1, 100)

        if escape_roll <= ESCAPE_CHANCE:
            dialogue.clear_screen()

            dialogue.narration("\nGot away safely!")
            dialogue.next_dialogue()

            return "ESCAPED"
        
        else:
            dialogue.clear_screen()

            dialogue.narration("\nCan't escape!")
            dialogue.next_dialogue()

            return "FAILED"

def fight_menu(player_pokemon):
    while True:

        dialogue.clear_screen()

        dialogue.narration("\nMOVES\n")

        for i, move in enumerate(player_pokemon.moves, 1):
            move_type = pokemon.moves_data[move]["type"]

            dialogue.narration(f"{i} - {move} ({move_type})")

        dialogue.narration("0 - BACK")

        choice = input("\nChoose: ")

        if not choice.isdigit():
            dialogue.clear_screen()
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()
            continue

        choice = int(choice)

        if choice == 0:
            return

        elif 1 <= choice <= len(player_pokemon.moves):
            selected_move = player_pokemon.moves[choice - 1]
            return selected_move
        
        else:
            dialogue.clear_screen()
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()

def show_battle_stats(player_pokemon, enemy_pokemon):
    print("\n-----------------------")

    print(f"FOE: {enemy_pokemon.name} Lv{enemy_pokemon.level}")
    print(f"HP: {enemy_pokemon.current_hp}/{enemy_pokemon.max_hp}")

    print("\nVS\n")

    print(f"YOUR: {player_pokemon.name} Lv{player_pokemon.level}")
    print(f"HP: {player_pokemon.current_hp}/{player_pokemon.max_hp}")

    print("-----------------------\n")

def show_attack_message(attacker, move, enemy_pokemon):
    if attacker == enemy_pokemon:
        dialogue.narration(f"\nFoe {attacker.name} used {move}!")
    else:
        dialogue.narration(f"\n{attacker.name} used {move}!")

def define_turn_order(player_pokemon, enemy_pokemon, player_move, enemy_move):
    if player_pokemon.speed > enemy_pokemon.speed:
        first_pokemon = player_pokemon
        first_move = player_move

        second_pokemon = enemy_pokemon
        second_move = enemy_move

    elif enemy_pokemon.speed > player_pokemon.speed:
        first_pokemon = enemy_pokemon
        first_move = enemy_move

        second_pokemon = player_pokemon
        second_move = player_move

    else:
        speed_roll = random.randint(0, 1)

        if speed_roll == 0:
            first_pokemon = player_pokemon
            first_move = player_move

            second_pokemon = enemy_pokemon
            second_move = enemy_move

        else:
            first_pokemon = enemy_pokemon
            first_move = enemy_move

            second_pokemon = player_pokemon
            second_move = player_move

    return first_pokemon, first_move, second_pokemon, second_move

def handle_faint(fainted_pokemon, player_pokemon, enemy_pokemon, player_name, enemy_name, battle_type):
    fainted_pokemon.current_hp = 0

    if fainted_pokemon == enemy_pokemon:
        dialogue.narration(f"\nFoe {enemy_pokemon.name} fainted!")

        if battle_type == "TRAINER":
            dialogue.narration(f"\n{player_name} defeated {enemy_name}!")

        elif battle_type == "WILD":
            dialogue.narration(f"\nYou defeated the wild {enemy_pokemon.name}!")

        dialogue.next_dialogue()
        return "WIN"

    elif fainted_pokemon == player_pokemon:
        dialogue.narration(f"\nYour {player_pokemon.name} fainted!")

        if battle_type == "TRAINER":
            dialogue.narration(f"\nYou were defeated by {enemy_name}!")

        elif battle_type == "WILD":
            dialogue.narration(f"\n{player_name} is out of usable POKEMON!")

        dialogue.next_dialogue()
        return "LOSE"

def battle_turn(player_pokemon, enemy_pokemon, player_move, player_name, enemy_name, battle_type):

    dialogue.clear_screen()

    enemy_move = random.choice(enemy_pokemon.moves)

    first_pokemon, first_move, second_pokemon, second_move = define_turn_order(player_pokemon, enemy_pokemon, player_move, enemy_move)

    show_attack_message(first_pokemon, first_move, enemy_pokemon)

    first_damage = calculate_damage(first_pokemon, second_pokemon, first_move)

    second_pokemon.current_hp -= first_damage

    if second_pokemon.current_hp <= 0:
        return handle_faint(second_pokemon, player_pokemon, enemy_pokemon, player_name, enemy_name, battle_type)

    dialogue.next_dialogue()

    show_attack_message(second_pokemon, second_move, enemy_pokemon)

    second_damage = calculate_damage(second_pokemon, first_pokemon, second_move)

    first_pokemon.current_hp -= second_damage

    if first_pokemon.current_hp <= 0:
        return handle_faint(first_pokemon, player_pokemon, enemy_pokemon, player_name, enemy_name, battle_type)

    dialogue.next_dialogue()

def battle_menu(player_pokemon, enemy_pokemon, player_name, enemy_name, battle_type):
    while True:
        
        dialogue.clear_screen()

        show_battle_stats(player_pokemon, enemy_pokemon)

        print(f"What will {player_pokemon.name} do?\n")

        print("1 - FIGHT")
        print("2 - RUN")
        print("3 - BAG")
        print("4 - POKEMON")

        choice = input("\nChoose: ")

        if choice == "1":

            move = fight_menu(player_pokemon)

            if move is None:
                continue

            result = battle_turn(player_pokemon, enemy_pokemon, move, player_name, enemy_name, battle_type)

            if result in ("WIN", "LOSE"):
                return result
                
        elif choice == "2":
            result = try_run(battle_type)

            if result == "ESCAPED":
                return result
            
            if result == "FAILED" and battle_type == "WILD":
                result = enemy_free_attack(player_pokemon, enemy_pokemon, player_name, enemy_name, battle_type)

                if result == "LOSE":
                    return result


        elif choice == "3":
            dialogue.narration("\nFeature not implemented yet.")
            dialogue.next_dialogue()

        elif choice == "4":
            dialogue.narration("\nFeature not implemented yet.")
            dialogue.next_dialogue()

        else:
            dialogue.clear_screen()
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()

def rival_first_battle(player_name, rival_name, player_pokemon, rival_pokemon):
    dialogue.talk(rival_name, f"{player_name}! Let's check out our POKEMON! Come on, I'll take you on!")

    dialogue.narration(f"\n{rival_name} challenges you to a battle!")
    dialogue.narration(f"\n{rival_name} sent out {rival_pokemon.name}!")
    dialogue.next_dialogue()

    dialogue.narration(f"\nGo! {player_pokemon.name}!")
    dialogue.next_dialogue()

    result = battle_menu(player_pokemon, rival_pokemon, player_name, rival_name, "TRAINER")

    if result == "LOSE":
        dialogue.talk(rival_name, f"{rival_pokemon.name} come back! Yeah! Am I great or what?")

    elif result == "WIN":
        dialogue.talk(rival_name, "WHAT? Unbelievable! I picked the wrong POKEMON!")

def wild_battle(player_name, player_pokemon, wild_pokemon):
    dialogue.narration(f"\nA wild {wild_pokemon.name} appeared!")
    dialogue.next_dialogue()
    
    dialogue.narration(f"\nGo! {player_pokemon.name}!")
    dialogue.next_dialogue()
    
    result = battle_menu(player_pokemon, wild_pokemon, player_name, "Wild Pokemon","WILD")
    
    return result
    