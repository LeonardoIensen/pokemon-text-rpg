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
                print("Rota 2 ainda nao implementada.")
                dialogue.next_dialogue()

                break

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