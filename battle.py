import dialogue
import pokemon
import random

def calculate_damage(attacker, defender, move):

    power = pokemon.moves_data[move]["power"]
    
    damage = (((attacker.level * 2) // 5 + 2) * power * attacker.attack) // defender.defense
    damage = damage // 50 + 2

    return damage

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

def show_battle_stats(player_starter, rival_starter):
    print("\n-----------------------")

    print(f"RIVAL: {rival_starter.name} Lv{rival_starter.level}")
    print(f"HP: {rival_starter.current_hp}/{rival_starter.max_hp}")

    print("\nVS\n")

    print(f"YOUR: {player_starter.name} Lv{player_starter.level}")
    print(f"HP: {player_starter.current_hp}/{player_starter.max_hp}")

    print("-----------------------\n")

def show_attack_message(attacker, move, rival_starter):
    if attacker == rival_starter:
        dialogue.narration(f"\nFoe {attacker.name} used {move}!")
    else:
        dialogue.narration(f"\n{attacker.name} used {move}!")

def define_turn_order(player_starter, rival_starter, player_move, rival_move):
    if player_starter.speed > rival_starter.speed:
        first_pokemon = player_starter
        first_move = player_move

        second_pokemon = rival_starter
        second_move = rival_move

    elif rival_starter.speed > player_starter.speed:
        first_pokemon = rival_starter
        first_move = rival_move

        second_pokemon = player_starter
        second_move = player_move

    else:
        speed_roll = random.randint(0, 1)

        if speed_roll == 0:
            first_pokemon = player_starter
            first_move = player_move

            second_pokemon = rival_starter
            second_move = rival_move

        else:
            first_pokemon = rival_starter
            first_move = rival_move

            second_pokemon = player_starter
            second_move = player_move

    return first_pokemon, first_move, second_pokemon, second_move

def handle_faint(fainted_pokemon, player_starter, rival_starter, player_name, rival_name):
        fainted_pokemon.current_hp = 0

        if fainted_pokemon == rival_starter:

            dialogue.narration(f"\nFoe {rival_starter.name} fainted!")
            dialogue.narration(f"\n{player_name} defeated {rival_name}!")
            dialogue.next_dialogue()

            dialogue.talk(rival_name,"WHAT? Unbelievable! I picked the wrong POKEMON!")

            return "WIN"

        if fainted_pokemon == player_starter:

            dialogue.narration(f"\nYour {player_starter.name} fainted!")
            dialogue.narration(f"\nYou were defeated by {rival_name}!")
            dialogue.next_dialogue()

            dialogue.talk(rival_name, f"{rival_starter.name} come back! Yeah! Am I great or what?")

            return "LOSE"


def battle_turn(player_starter, rival_starter, player_move, player_name, rival_name):

    dialogue.clear_screen()

    rival_move = random.choice(rival_starter.moves)

    first_pokemon, first_move, second_pokemon, second_move = define_turn_order(player_starter, rival_starter, player_move, rival_move)

    show_attack_message(first_pokemon, first_move, rival_starter)

    first_damage = calculate_damage(first_pokemon, second_pokemon, first_move)

    second_pokemon.current_hp -= first_damage

    if second_pokemon.current_hp <= 0:
        return handle_faint(second_pokemon, player_starter, rival_starter, player_name, rival_name)
    
    show_attack_message(second_pokemon, second_move, rival_starter)

    dialogue.next_dialogue()

    second_damage = calculate_damage(second_pokemon, first_pokemon, second_move)

    first_pokemon.current_hp -= second_damage

    if first_pokemon.current_hp <= 0:
        return handle_faint(first_pokemon, player_starter, rival_starter, player_name, rival_name)

def battle_menu(player_starter, rival_starter, player_name, rival_name):
    while True:
        
        dialogue.clear_screen()

        show_battle_stats(player_starter, rival_starter)

        dialogue.narration(f"What will {player_starter.name} do?\n")

        dialogue.narration("1 - FIGHT")
        dialogue.narration("2 - POKEMON")
        dialogue.narration("3 - BAG")
        dialogue.narration("4 - RUN")

        choice = input("\nChoose: ")

        if choice == "1":

            move = fight_menu(player_starter)

            if move is None:
                continue

            result = battle_turn(player_starter, rival_starter, move, player_name, rival_name)

            if result in ("WIN", "LOSE"):
                break
                

        elif choice == "2":
            dialogue.narration("\nFeature not implemented yet.")
            dialogue.next_dialogue()

        elif choice == "3":
            dialogue.narration("\nFeature not implemented yet.")
            dialogue.next_dialogue()

        elif choice == "4":
            dialogue.narration("\nFeature not implemented yet.")
            dialogue.next_dialogue()

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

    battle_menu(player_starter, rival_starter, player_name, rival_name)