import dialogue
import pokemon
import random

CRITICAL_HIT_CHANCE = 16

TYPE_EFFECTIVENESS = {

    "NORMAL": {
        "ROCK": 0.5,
    },

    "FIRE": {
        "GRASS": 2,
        "BUG": 2,
        "FIRE": 0.5,
        "WATER": 0.5,
        "ROCK": 0.5,
    },

    "WATER": {
        "FIRE": 2,
        "ROCK": 2,
        "GROUND": 2,
        "WATER": 0.5,
        "GRASS": 0.5,
    },

    "GRASS": {
        "WATER": 2,
        "ROCK": 2,
        "GROUND": 2,
        "FIRE": 0.5,
        "GRASS": 0.5,
        "POISON": 0.5,
        "BUG": 0.5,
        "FLYING": 0.5,
    },

    "ELECTRIC": {
        "WATER": 2,
        "FLYING": 2,
        "ELECTRIC": 0.5,
        "GRASS": 0.5,
        "GROUND": 0,
    },

    "FLYING": {
        "GRASS": 2,
        "BUG": 2,
        "FIGHT": 2,
        "ELECTRIC": 0.5,
        "ROCK": 0.5,
    },

    "POISON": {
        "GRASS": 2,
        "POISON": 0.5,
        "GROUND": 0.5,
        "ROCK": 0.5,
    },

    "PSYCHIC": {
        "FIGHT": 2,
        "POISON": 2,
        "PSYCHIC": 0.5,
    },

    "STEEL": {
        "ROCK": 2,
        "FIRE": 0.5,
        "WATER": 0.5,
        "ELECTRIC": 0.5,
    },

    "FIGHT": {
        "NORMAL": 2,
        "ROCK": 2,
        "POISON": 0.5,
        "FLYING": 0.5,
        "BUG": 0.5,
        "PSYCHIC": 0.5,
    },

    "DARK": {
        "PSYCHIC": 2,
        "FIGHT": 0.5,
    },

    "ROCK": {
        "FIRE": 2,
        "FLYING": 2,
        "BUG": 2,
        "FIGHT": 0.5,
        "GROUND": 0.5,
    },

    "GROUND": {
        "FIRE": 2,
        "ELECTRIC": 2,
        "POISON": 2,
        "ROCK": 2,
        "GRASS": 0.5,
        "BUG": 0.5,
        "FLYING": 0,
    },
}

def calculate_damage(attacker, defender, move, is_critical=False):
    move_data = pokemon.moves[move]

    power = move_data["power"]
    accuracy = move_data["accuracy"]

    accuracy_roll = random.randint(1, 100)

    if accuracy_roll > accuracy:
        damage = 0

    else:
        damage = (((attacker.level * 2) // 5 + 2) * power * attacker.attack) // defender.defense
        damage = damage // 50 + 2

        if is_critical:
            damage = damage * 2

        type_multiplier = get_type_multiplier(move, defender)

        if type_multiplier == 0:
            return 0

        damage = int(damage * type_multiplier)

        if damage < 1:
            damage = 1

    return int(damage)


def check_critical_hit():
    critical_roll = random.randint(1, CRITICAL_HIT_CHANCE)

    if critical_roll == 1:
        return True

    else:
        return False


def get_type_multiplier(move, defender):
    move_type = pokemon.moves[move]["type"]
    defender_types = defender.type.split(" / ")

    multiplier = 1

    for def_type in defender_types:
        type_val = TYPE_EFFECTIVENESS.get(move_type, {}).get(def_type, 1)

        multiplier = multiplier * type_val

    return multiplier


def calculate_exp_gain(enemy_pokemon, is_trainer_battle):
    exp_gain = int(enemy_pokemon.base_exp * enemy_pokemon.level / 9)

    if is_trainer_battle:
        exp_gain = int(exp_gain * 1.5)

    return exp_gain


def decide_first_attacker(player_pokemon, enemy_pokemon):
    if player_pokemon.speed > enemy_pokemon.speed:
        first_attacker = "player"

    elif enemy_pokemon.speed > player_pokemon.speed:
        first_attacker = "enemy"

    else:
        first_attacker = random.choice(["player", "enemy"])

    return first_attacker


def enemy_turn(player_pokemon, enemy_pokemon):
    dialogue.clear_screen()

    enemy_move = random.choice(enemy_pokemon.moves)

    print(f"{enemy_pokemon.name} usou {enemy_move}!")

    is_critical = check_critical_hit()
    type_multiplier = get_type_multiplier(enemy_move, player_pokemon)

    damage = calculate_damage(enemy_pokemon, player_pokemon, enemy_move, is_critical)

    if damage == 0:
        if type_multiplier == 0:
            show_type_effectiveness_message(type_multiplier)
        else:
            print(f"\n{enemy_pokemon.name} errou o ataque!")

    else:
        show_type_effectiveness_message(type_multiplier)

        if is_critical:
            print(f"\n{enemy_pokemon.name} acertou um golpe crítico!")

        player_pokemon.current_hp -= damage

        if player_pokemon.current_hp < 0:
            player_pokemon.current_hp = 0

    if player_pokemon.current_hp <= 0:
        print(f"\nSeu {player_pokemon.name} foi derrotado!")
        dialogue.next_dialogue()
        return "LOSE"

    dialogue.next_dialogue()


def player_turn(player_pokemon, enemy_pokemon, move):
    dialogue.clear_screen()

    print(f"{player_pokemon.name} usou {move}!")

    is_critical = check_critical_hit()
    type_multiplier = get_type_multiplier(move, enemy_pokemon)

    damage = calculate_damage(player_pokemon, enemy_pokemon, move, is_critical)

    if damage == 0:
        if type_multiplier == 0:
            show_type_effectiveness_message(type_multiplier)
        else:
            print(f"\n{player_pokemon.name} errou o ataque!")

    else:
        show_type_effectiveness_message(type_multiplier)

        if is_critical:
            print(f"\n{player_pokemon.name} acertou um golpe crítico!")

        enemy_pokemon.current_hp -= damage

        if enemy_pokemon.current_hp < 0:
            enemy_pokemon.current_hp = 0

    if enemy_pokemon.current_hp <= 0:
        print(f"\n{enemy_pokemon.name} foi derrotado!")
        dialogue.next_dialogue()
        return "WIN"

    dialogue.next_dialogue()


def execute_turn(player_pokemon, enemy_pokemon, first_attacker, move):
    if first_attacker == "player":
        result = player_turn(player_pokemon, enemy_pokemon, move)

        if result == "WIN":
            return "WIN"

        result = enemy_turn(player_pokemon, enemy_pokemon)

        if result == "LOSE":
            return "LOSE"

    else:
        result = enemy_turn(player_pokemon, enemy_pokemon)

        if result == "LOSE":
            return "LOSE"

        result = player_turn(player_pokemon, enemy_pokemon, move)

        if result == "WIN":
            return "WIN"


def try_to_run(is_trainer_battle):
    if is_trainer_battle:
        dialogue.clear_screen()
        print("Não é possível fugir de uma batalha contra um treinador!")
        dialogue.next_dialogue()

        return False

    run_chance = random.randint(1, 100)

    if run_chance > 90:
        dialogue.clear_screen()
        print("Nao conseguiu escapar!")

        return False

    dialogue.clear_screen()
    print("Conseguiu escapar!")
    dialogue.next_dialogue()

    return True


def show_type_effectiveness_message(multiplier):
    if multiplier > 1:
        print("\nFoi super efetivo!")

    elif 0 < multiplier < 1:
        print("\nNão fez muito efeito...")

    elif multiplier == 0:
        print("\nNão teve efeito...")


def show_battle_stats(player_pokemon, enemy_pokemon):
    print("------------------------")

    print(f"{enemy_pokemon.name} Lv{enemy_pokemon.level}")
    print(f"HP: {enemy_pokemon.current_hp}/{enemy_pokemon.max_hp}")

    print("\nVS\n")

    print(f"{player_pokemon.name} Lv{player_pokemon.level}")
    print(f"HP: {player_pokemon.current_hp}/{player_pokemon.max_hp}    XP: {player_pokemon.experience}/{player_pokemon.exp_next_level()}")

    print("------------------------\n")


def show_summary(selected_pokemon):
    dialogue.clear_screen()

    print("--- SUMARIO ---")
    print(f"Name: {selected_pokemon.name} Lv: {selected_pokemon.level}")
    print(f"TYPE: {selected_pokemon.type}\n")

    print(f"HP: {selected_pokemon.current_hp}/{selected_pokemon.max_hp}")
    print(f"XP: {selected_pokemon.experience}/{selected_pokemon.exp_next_level()}")
    print(f"ATTACK: {selected_pokemon.attack}")
    print(f"DEFENSE: {selected_pokemon.defense}")
    print(f"SPEED: {selected_pokemon.speed}\n")

    print("--- MOVES ---")
    for i, move in enumerate(selected_pokemon.moves, start=1):
        print(f"{i} - {move}")

    dialogue.next_dialogue()


def swap_pokemon_party(player, first_index):
    while True:
        dialogue.clear_screen()

        print("--- PARTY ---\n")

        for i, pokemon in enumerate (player.party, start=1):
            print(f"{i}- {pokemon.name}")

        print("\n0- VOLTAR")

        try:
            choice = int(input("\nEscolha o segundo Pokemon: "))

        except ValueError:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()

            continue

        if choice == 0:
            return

        if 1 <= choice <= len(player.party):
            second_index = choice - 1

            if second_index == first_index:
                dialogue.clear_screen()
                print("Não pode trocar um Pokémon por ele mesmo!")
                dialogue.next_dialogue()

                continue

            first_pokemon_name = player.party[first_index].name
            second_pokemon_name = player.party[second_index].name

            player.party[first_index], player.party[second_index] = player.party[second_index], player.party[first_index]

            dialogue.clear_screen()
            print(f"{player.name} trocou {first_pokemon_name} por {second_pokemon_name}!")
            dialogue.next_dialogue()

            return True

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()


def pokemon_options_menu(player, selected_pokemon, firs_index):
    while True:
        dialogue.clear_screen()

        print(f"--- {selected_pokemon.name} ---\n")

        print("1- SUMARIO")
        print("2- TROCAR")
        print("\n0- VOLTAR")

        choice = input("\nEscolha: ")

        if choice == "0":
            return

        if choice == "1":
            show_summary(selected_pokemon)

        elif choice == "2":
            result = swap_pokemon_party(player, firs_index)

            if result:
                return

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()


def party_menu(player):
    while True:
        dialogue.clear_screen()

        print("--- PARTY ---\n")

        for i, pokemon in enumerate (player.party, start=1):
            print(f"{i}- {pokemon.name}")

        print("\n0- VOLTAR")

        try:
            choice = int(input("\nEscolha: "))

        except ValueError:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()

            continue

        if choice == 0:
            return

        if 1 <= choice <= len(player.party):
            selected_pokemon = player.party[choice - 1]

            first_index = choice - 1

            pokemon_options_menu(player, selected_pokemon, first_index)

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()


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


def rival_first_battle(player, rival):
    dialogue.clear_screen()

    dialogue.talk(rival.name, f"{player.name}! Vamos ver nossos POKÉMON! Vamos lá, vou enfrentar você!")

    print(f"\n{rival.name} desafia você para uma batalha!")
    print(f"\n{rival.name} enviou {rival.party[0].name}!")
    dialogue.next_dialogue()

    print(f"\nVai! {player.party[0].name}!")
    dialogue.next_dialogue()

    result, player_pokemon = battle_menu(player, rival.party[0], is_trainer_battle=True, player_pokemon=player.party[0])

    if result == "LOSE":
        dialogue.talk(rival.name, f"{rival.party[0].name}, volte! Isso aí! Eu não sou demais?")

    elif result == "WIN":
        handle_victory(player_pokemon, rival.party[0], is_trainer_battle=True)

        dialogue.talk(rival.name, "O QUÊ? Inacreditável! Escolhi o POKÉMON errado!")

    dialogue.clear_screen()
    print(f"Após testar seus POKÉMON em uma batalha intensa, {player.name} se despede e se encaminha para fora de Pallet Town...")
    dialogue.next_dialogue()


def has_available_pokemon(player):
    for pokemon in player.party:
        if pokemon.current_hp > 0:
            return True

    return False


def choose_battle_menu(player, current_pokemon=None, force_switch=False):
    while True:
        dialogue.clear_screen()

        print("--- PARTY ---\n")

        for i, pokemon in enumerate(player.party, start=1):
            hp = max(0, pokemon.current_hp)
            print(f"{i}- {pokemon.name:<12} HP: {hp}/{pokemon.max_hp}")

        if not force_switch:
            print("\n0- VOLTAR")

        try:
            choice = int(input("\nEscolha: "))

        except ValueError:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()

            continue

        if choice == 0 and not force_switch:
            return

        if 1 <= choice <= len(player.party):
            selected_pokemon = player.party[choice - 1]

            if selected_pokemon.current_hp <= 0:
                dialogue.clear_screen()
                print("Esse Pokémon está derrotado!")
                dialogue.next_dialogue()

            elif selected_pokemon == current_pokemon:
                dialogue.clear_screen()
                print("Esse Pokémon já está em batalha!")
                dialogue.next_dialogue()

            else:
                return selected_pokemon

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()


def trainer_battle(player, trainer):
    dialogue.clear_screen()

    print(f"{trainer.name} desafia você para uma batalha!")
    dialogue.next_dialogue()

    player_pokemon = player.party[0]

    for pokemon in trainer.party:
        dialogue.clear_screen()
        print(f"{trainer.name} enviou {pokemon.name}!")

        print(f"\nVai! {player_pokemon.name}!")
        dialogue.next_dialogue()

        result, player_pokemon = battle_menu(player, pokemon, is_trainer_battle=True, player_pokemon=player_pokemon)

        if result == "LOSE":
            print(f"{player.name} perdeu para {trainer.name}!")
            dialogue.next_dialogue()

            return "LOSE"

        handle_victory(player_pokemon, pokemon, is_trainer_battle=True)

    print(f"{player.name} derrotou {trainer.name}!")

    return "WIN"


def wild_battle(player, wild_pokemon):
    dialogue.clear_screen()
    print(f"Um {wild_pokemon.name} selvagem apareceu!")

    print(f"\nVai! {player.party[0].name}!")
    dialogue.next_dialogue()

    result, player_pokemon = battle_menu(player, wild_pokemon, is_trainer_battle=False, player_pokemon=player.party[0])

    if result == "WIN":
        handle_victory(player_pokemon, wild_pokemon, is_trainer_battle=False)

    return result


def handle_victory(player_pokemon, enemy_pokemon, is_trainer_battle):
    exp_gain = calculate_exp_gain(enemy_pokemon, is_trainer_battle)

    dialogue.clear_screen()

    player_pokemon.gain_experience(exp_gain)

    dialogue.next_dialogue()


def battle_menu(player, enemy_pokemon, is_trainer_battle, player_pokemon):

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

                first_attacker = decide_first_attacker(player_pokemon, enemy_pokemon)

                result = execute_turn(player_pokemon, enemy_pokemon, first_attacker, move)

                if result == "WIN":
                    return "WIN", player_pokemon

                elif result == "LOSE":
                    if has_available_pokemon(player):
                        player_pokemon = choose_battle_menu(player, player_pokemon, force_switch=True)

                        if player_pokemon is None:
                            return "LOSE", player_pokemon

                        dialogue.clear_screen()
                        print(f"\nVai! {player_pokemon.name}!")
                        dialogue.next_dialogue()

                        result = enemy_turn(player_pokemon, enemy_pokemon)

                        if result == "LOSE":
                            if not has_available_pokemon(player):
                                return "LOSE", player_pokemon

                            continue

                    else:
                        return "LOSE", player_pokemon

        elif choice == "2":
            result = try_to_run(is_trainer_battle)

            if result:
                return "RUN", player_pokemon

            elif not result and not is_trainer_battle:
                result = enemy_turn(player_pokemon, enemy_pokemon)

                if result == "LOSE":
                    if has_available_pokemon(player):
                        player_pokemon = choose_battle_menu(player, player_pokemon, force_switch=True)

                        if player_pokemon is None:
                            return "LOSE", player_pokemon

                        dialogue.clear_screen()
                        print(f"\nVai! {player_pokemon.name}!")
                        dialogue.next_dialogue()

                    else:
                        return "LOSE", player_pokemon

        elif choice == "3":
            print("Nao implementado.")

        elif choice == "4":
            selected_pokemon = choose_battle_menu(player, player_pokemon)

            if selected_pokemon is not None:
                player_pokemon = selected_pokemon

                dialogue.clear_screen()
                print(f"\nVai! {player_pokemon.name}!")
                dialogue.next_dialogue()

                result = enemy_turn(player_pokemon, enemy_pokemon)

                if result == "LOSE":
                    if not has_available_pokemon(player):
                        return "LOSE", player_pokemon

                    player_pokemon = choose_battle_menu(player, player_pokemon, force_switch=True)

                    if player_pokemon is None:
                        return "LOSE", player_pokemon

                    dialogue.clear_screen()
                    print(f"\nVai! {player_pokemon.name}!")
                    dialogue.next_dialogue()

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()