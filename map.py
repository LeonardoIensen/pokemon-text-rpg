import dialogue
import pokemon
import battle
import random

route_1_pokemons = {

    "RATTATA": {
        "LEVEL": (2,5),
        "CHANCE": 50,
    },

    "PIDGEY": {
        "LEVEL": (2,5),
        "CHANCE": 50,
    }

}

route_2_pokemons = {

    "RATTATA": {
        "LEVEL": (2,5),
        "CHANCE": 50,
    },

    "SPEAROW": {
        "LEVEL": (2,5),
        "CHANCE": 50,
    },

    "MANKEY": {
        "LEVEL": (2,5),
        "CHANCE": 50,
    },

}


def wild_encounter(player, route_pokemon):
    dialogue.clear_screen() 
    print(f"\n{player.name} caminhou pela grama alta...")

    encounter_roll = random.randint(1, 100)

    if encounter_roll <= 85:
        available_pokemons = list(route_pokemon.keys())

        pokemon_name = random.choice(available_pokemons)

        level_pokemon = route_pokemon[pokemon_name]["LEVEL"]

        min_level = level_pokemon[0]
        max_level = level_pokemon[1]

        wild_level = random.randint(min_level, max_level)

        wild_pokemon = pokemon.Pokemon(pokemon_name, wild_level)

        result = battle.wild_battle(player, wild_pokemon)

    else:
        print("\nNenhum Pokémon apareceu...")
        dialogue.next_dialogue()

        result = None

    return result


def pokemon_center(player):
    dialogue.clear_screen()

    print("--- CENTRO POKÉMON ---\n")
    print("Enfermeira Joy: Olá! Bem-vindo ao Centro Pokémon.")
    print("Nós curamos seus Pokémon desmaiados ou feridos até sua saúde total.\n")

    for pokemon in player.party:
        pokemon.heal_full()
 
    print("Seus POKÉMON foram totalmente restaurados! Esperamos ver você novamente!")
    dialogue.next_dialogue()


def route_1(player):

    steps = 0

    while True:
        dialogue.clear_screen()

        print("--- ROTA 1 ---\n")
        print(f"Progresso: {steps}/5\n")

        print("1 - ANDAR")
        print("2 - ANDAR NA GRAMA")
        print("3 - MENU")

        choice = input("\nEscolha: ")

        if choice == "1":
            steps += 1

            if steps >= 5:
                dialogue.clear_screen()

                print(f"{player.name} chegou a cidade de Viridian!")
                dialogue.next_dialogue()

                steps = 0

                viridian_city(player)

        elif choice == "2":
            result = wild_encounter(player, route_1_pokemons)

            if result == "LOSE":
                dialogue.clear_screen()
                print(f"Sem Pokémon para batalhar, {player.name} retorna para casa em Pallet Town para recuperar sua equipe.")
                dialogue.next_dialogue()

                for pokemon in player.party:
                    pokemon.heal_full()
                
                steps = 0

        elif choice == "3":
            dialogue.clear_screen()
            print("Menu ainda nao implementado.")
            dialogue.next_dialogue()

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue() 


def route_2(player):

    steps = 0

    while True:
        dialogue.clear_screen()

        print("--- ROTA 2 ---\n")
        print(f"Progresso: {steps}/5\n")

        print("1 - ANDAR")
        print("2 - ANDAR NA GRAMA")
        print("3 - VOLTAR PARA VIRIDIAN")
        print("4 - MENU")

        choice = input("\nEscolha: ")

        if choice == "1":
            steps += 1

            if steps >= 5:
                dialogue.clear_screen()
                print(f"Bosque de Viridian nao implementado")
                dialogue.next_dialogue()

        elif choice == "2":
            result = wild_encounter(player, route_2_pokemons)

            if result == "LOSE":
                dialogue.clear_screen()
                print(f"Sem Pokémon para batalhar, {player.name} retorna para o centro pokemon mais proximo para recuperar sua equipe.")
                dialogue.next_dialogue()

                for pokemon in player.party:
                    pokemon.heal_full()

                steps = 0

                return

        elif choice == "3":
            return
        
        elif choice == "4":
            dialogue.clear_screen()
            print("Menu ainda nao implementado.")
            dialogue.next_dialogue()

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue() 


def viridian_city(player):
    while True:
        dialogue.clear_screen()

        print("--- VIRIDIAN CITY ---\n")

        print("1 - IR PARA A ROTA 2")
        print("2 - VOLTAR PARA A ROTA 1")
        print("3 - CENTRO POKEMON")
        print("4 - MENU")

        choice = input("\nEscolha: ")

        if choice == "1":
            dialogue.clear_screen()
            
            print(f"{player.name} chegou a Rota 2!")
            dialogue.next_dialogue()

            route_2(player)

        elif choice == "2":
            return

        elif choice == "3":
            pokemon_center(player)

        elif choice == "4":
            dialogue.clear_screen()
            print("Menu ainda nao implementado.")
            dialogue.next_dialogue()

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue() 