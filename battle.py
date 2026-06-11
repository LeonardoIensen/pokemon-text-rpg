import dialogue
import pokemon
import random

ESCAPE_CHANCE = 90

def calculate_damage(attacker, defender, move):

    power = pokemon.moves_data[move]["power"]
    
    damage = (((attacker.level * 2) // 5 + 2) * power * attacker.attack) // defender.defense
    damage = damage // 50 + 2

    return damage

def try_run(battle_type):

    if battle_type == "TRAINER":
        dialogue.narration("\nNo! There's no running from a TRAINER battle!")
        dialogue.next_dialogue()

        return "FAILED"
    
    elif battle_type == "WILD":

        escape_roll = random.randint(1, 100)

        if escape_roll <= ESCAPE_CHANCE:
            dialogue.narration("\nGot away safely!")
            dialogue.next_dialogue()

            return "ESCAPED"
        
        else:
            dialogue.narration("\nCan't escape!")
            dialogue.next_dialogue()

            return "FAILED"

def fight_menu(player_starter):
    while True:

        dialogue.clear_screen()

        dialogue.narration("\nMOVES\n")

        for i, move in enumerate(player_starter.moves, 1):
            move_type = pokemon.moves_data[move]["type"]

            dialogue.narration(f"{i} - {move} ({move_type})")

        dialogue.narration("0 - BACK")

        choice = input("\nChoose: ")
        choice = int(choice)

        if choice == 0:
            return

        elif 1 <= choice <= len(player_starter.moves):
            selected_move = player_starter.moves[choice - 1]
            return selected_move
        
        else:
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()

def show_battle_stats(player_starter, enemy_starter):
    print("\n-----------------------")

    print(f"FOE: {enemy_starter.name} Lv{enemy_starter.level}")
    print(f"HP: {enemy_starter.current_hp}/{enemy_starter.max_hp}")

    print("\nVS\n")

    print(f"YOUR: {player_starter.name} Lv{player_starter.level}")
    print(f"HP: {player_starter.current_hp}/{player_starter.max_hp}")

    print("-----------------------\n")

def show_attack_message(attacker, move, enemy_starter):
    if attacker == enemy_starter:
        dialogue.narration(f"\nFoe {attacker.name} used {move}!")
    else:
        dialogue.narration(f"\n{attacker.name} used {move}!")

def define_turn_order(player_starter, enemy_starter, player_move, enemy_move):
    if player_starter.speed > enemy_starter.speed:
        first_pokemon = player_starter
        first_move = player_move

        second_pokemon = enemy_starter
        second_move = enemy_move

    elif enemy_starter.speed > player_starter.speed:
        first_pokemon = enemy_starter
        first_move = enemy_move

        second_pokemon = player_starter
        second_move = player_move

    else:
        speed_roll = random.randint(0, 1)

        if speed_roll == 0:
            first_pokemon = player_starter
            first_move = player_move

            second_pokemon = enemy_starter
            second_move = enemy_move

        else:
            first_pokemon = enemy_starter
            first_move = enemy_move

            second_pokemon = player_starter
            second_move = player_move

    return first_pokemon, first_move, second_pokemon, second_move

def handle_faint(fainted_pokemon, player_starter, enemy_starter, player_name, enemy_name):
    fainted_pokemon.current_hp = 0

    if fainted_pokemon == enemy_starter:

        dialogue.narration(f"\nFoe {enemy_starter.name} fainted!")
        dialogue.narration(f"\n{player_name} defeated {enemy_name}!")
        dialogue.next_dialogue()

        dialogue.talk(enemy_name, "WHAT? Unbelievable! I picked the wrong POKEMON!")

        return "WIN"

    if fainted_pokemon == player_starter:

        dialogue.narration(f"\nYour {player_starter.name} fainted!")
        dialogue.narration(f"\nYou were defeated by {enemy_name}!")
        dialogue.next_dialogue()

        dialogue.talk(enemy_name, f"{enemy_starter.name} come back! Yeah! Am I great or what?")

        return "LOSE"

def battle_turn(player_starter, enemy_starter, player_move, player_name, enemy_name):

    dialogue.clear_screen()

    enemy_move = random.choice(enemy_starter.moves)

    first_pokemon, first_move, second_pokemon, second_move = define_turn_order(
        player_starter,
        enemy_starter,
        player_move,
        enemy_move
    )

    show_attack_message(first_pokemon, first_move, enemy_starter)

    first_damage = calculate_damage(first_pokemon, second_pokemon, first_move)

    second_pokemon.current_hp -= first_damage

    if second_pokemon.current_hp <= 0:
        return handle_faint(second_pokemon, player_starter, enemy_starter, player_name, enemy_name)
    
    show_attack_message(second_pokemon, second_move, enemy_starter)

    dialogue.next_dialogue()

    second_damage = calculate_damage(second_pokemon, first_pokemon, second_move)

    first_pokemon.current_hp -= second_damage

    if first_pokemon.current_hp <= 0:
        return handle_faint(first_pokemon, player_starter, enemy_starter, player_name, enemy_name)

def battle_menu(player_starter, enemy_starter, player_name, enemy_name, battle_type):
    while True:
        
        dialogue.clear_screen()

        show_battle_stats(player_starter, enemy_starter)

        dialogue.narration(f"What will {player_starter.name} do?\n")

        print("1 - FIGHT")
        print("2 - POKEMON")
        print("3 - BAG")
        print("4 - RUN")

        choice = input("\nChoose: ")

        if choice == "1":

            move = fight_menu(player_starter)

            if move is None:
                continue

            result = battle_turn(player_starter, enemy_starter, move, player_name, enemy_name)

            if result in ("WIN", "LOSE"):
                break
                
        elif choice == "2":
            dialogue.narration("\nFeature not implemented yet.")
            dialogue.next_dialogue()

        elif choice == "3":
            dialogue.narration("\nFeature not implemented yet.")
            dialogue.next_dialogue()

        elif choice == "4":
            result = try_run(battle_type)

            if result == "ESCAPED":
                break

        else:
            dialogue.narration("\nFeature not implemented yet.")
            dialogue.next_dialogue()

def rival_first_battle(
    player_name,
    rival_name,
    player_starter,
    rival_starter
):
    dialogue.talk(f"{rival_name}", f"{player_name}! Let's check out our POKEMON! Come on, I'll take you on!")

    dialogue.narration(f"\n{rival_name} challenges you to a battle!")
    dialogue.narration(f"\n{rival_name} sent out {rival_starter.name}!")
    dialogue.next_dialogue()

    dialogue.narration(f"\nGo! {player_starter.name}!")
    dialogue.next_dialogue()

    battle_menu(player_starter, rival_starter, player_name, rival_name, "TRAINER")