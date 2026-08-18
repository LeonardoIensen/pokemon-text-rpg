import dialogue
import pokemon
import random

def show_battle_stats(player_pokemon, enemy_pokemon):
    print("------------------")

    print(f"{enemy_pokemon.name} Lv{enemy_pokemon.level}")
    print(f"HP: {enemy_pokemon.current_hp}/{enemy_pokemon.max_hp}")

    print("\nVS\n")

    print(f"{player_pokemon.name} Lv{player_pokemon.level}")
    print(f"HP: {player_pokemon.current_hp}/{player_pokemon.max_hp}")

    print("------------------\n")

def fight_menu(player_pokemon):

    while True:
        dialogue.clear_screen()

        print("--- MOVES ---\n")

        for i, move in enumerate(player_pokemon.moves, start=1):
            print(f"{i} - {move}")

        print("0 - VOLTAR")

        try:
            choice = int(input("\nEscolha: "))

        except ValueError:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()

            continue

        if choice == 0:
            return

        if choice < 1 or choice > len(player_pokemon.moves):
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()

            continue

        choice = choice - 1

        move = player_pokemon.moves[choice]

        return move

def calculate_damage(attacker, defender, move):
    move_data = pokemon.moves[move]

    power = move_data["power"]
    accuracy = move_data["accuracy"]

    accuracy_roll = random.randint(1, 100)

    if accuracy_roll > accuracy:
        damage = 0

    else:
        damage = (((2 * attacker.level + 2) / 5) * (power *(attacker.attack / defender.defense)) / 50 ) + 2

    return int(damage * 1.5)

def enemy_turn(player_pokemon, enemy_pokemon):
    enemy_move = random.choice(enemy_pokemon.moves)
    
    print(f"\n{enemy_pokemon.name} usou {enemy_move}!")

    damage = calculate_damage(enemy_pokemon, player_pokemon, enemy_move)

    if damage == 0:
        print(f"\n{enemy_pokemon.name} errou o ataque!")

    else:
        player_pokemon.current_hp = player_pokemon.current_hp - damage
    
    if player_pokemon.current_hp <= 0:
        print(f"\nSeu {player_pokemon.name} foi derrotado!")
        dialogue.next_dialogue()
        return "LOSE"

def player_turn(player_pokemon, enemy_pokemon, move):
    dialogue.clear_screen()

    print(f"{player_pokemon.name} usou {move}!")

    damage = calculate_damage(player_pokemon, enemy_pokemon, move)

    if damage == 0:
        print(f"\n{player_pokemon.name} errou o ataque!")

    else:
        enemy_pokemon.current_hp = enemy_pokemon.current_hp - damage

    if enemy_pokemon.current_hp <= 0:
        print(f"\n{enemy_pokemon.name} foi derrotado!")
        dialogue.next_dialogue()
        return "WIN"
        
def battle_menu(player_name, enemy_name, player_pokemon, enemy_pokemon):
    while True:
        dialogue.clear_screen()

        show_battle_stats(player_pokemon, enemy_pokemon)

        print("1 - FIGHT")
        print("2 - RUN")
        print("3 - BAG")
        print("4 - POKEMON")

        choice = input("\nEscolha: ")

        if choice == "1":
            move = fight_menu(player_pokemon)

            if move is not None:
                result = player_turn(player_pokemon, enemy_pokemon, move)

                if result == "WIN":
                    return "WIN"

                result = enemy_turn(player_pokemon, enemy_pokemon)

                if result == "LOSE":
                    return "LOSE"

                dialogue.next_dialogue()

        elif choice == "2":
            print("Nao implementado.")

        elif choice == "3":
            print("Nao implementado.")

        elif choice == "4":
            print("Nao implementado.")

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()

def rival_first_battle(player_name, rival_name, player_pokemon, rival_pokemon):
    dialogue.clear_screen()

    dialogue.talk(rival_name, f"{player_name}! Vamos ver nossos POKÉMON! Vamos lá, vou enfrentar você!")

    print(f"\n{rival_name} desafia você para uma batalha!")
    print(f"\n{rival_name} enviou {rival_pokemon.name}!")
    dialogue.next_dialogue()

    print(f"\nVai! {player_pokemon.name}!")
    dialogue.next_dialogue()

    result = battle_menu(player_name, rival_name, player_pokemon, rival_pokemon)

    if result == "LOSE":
        dialogue.talk(rival_name, f"{rival_pokemon.name}, volte! Isso aí! Eu não sou demais?")

    elif result == "WIN":
        dialogue.talk(rival_name, "O QUÊ? Inacreditável! Escolhi o POKÉMON errado!")