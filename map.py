import dialogue
import pokemon
import battle
import random
import trainer

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
    
    "PIDGEY": {
        "LEVEL": (2,5),
        "CHANCE": 25,
    },

    "RATTATA": {
        "LEVEL": (2,5),
        "CHANCE": 25,
    },

    "SPEAROW": {
        "LEVEL": (2,5),
        "CHANCE": 25,
    },

    "MANKEY": {
        "LEVEL": (2,5),
        "CHANCE": 25,
    },

}

route_3_pokemons = {
    
    "PIDGEY": {
        "LEVEL": (4,10),
        "CHANCE": 25,
    },

    "RATTATA": {
        "LEVEL": (4,10),
        "CHANCE": 25,
    },

    "SPEAROW": {
        "LEVEL": (4,10),
        "CHANCE": 25,
    },

    "MANKEY": {
        "LEVEL": (4,10),
        "CHANCE": 25,
    },

}

viridian_forest_pokemons = {

    "CATERPIE": {
        "LEVEL": (4,6),
        "CHANCE": 25,
    },
    
    "METAPOD": {
        "LEVEL": (7,9),
        "CHANCE": 15,
    },
    
    "BUTTERFREE": {
        "LEVEL": (10,12),
        "CHANCE": 5,
    },

    "WEEDLE": {
        "LEVEL": (4,6),
        "CHANCE": 25,
    },

    "KAKUNA": {
        "LEVEL": (7,9),
        "CHANCE": 15,
    },

    "BEEDRILL": {
        "LEVEL": (10,12),
        "CHANCE": 5,
    },
        
    "PIKACHU": {
        "LEVEL": (3,5),
        "CHANCE": 10,
    },

}


def wild_encounter(player, route_pokemon):
    dialogue.clear_screen() 

    print(f"\n{player.name} caminhou pela grama alta...")

    encounter_roll = random.randint(1, 100)

    if encounter_roll <= 85:
        available_pokemons = list(route_pokemon.keys())

        chances = []

        for wild_poke in available_pokemons:
            valor = route_pokemon[wild_poke]["CHANCE"]

            chances.append(valor)

        pokemon_name = random.choices(available_pokemons, weights=chances, k=1)[0]

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


def player_menu(player):
    while True:
        dialogue.clear_screen()

        print("--- MENU ---\n")
        print("1- POKEMON")
        print("2- BAG")
        print("3- SAIR")
        print("4- SALVAR")
        print("\n0- VOLTAR")

        choice = input("\nEscolha: ")

        if choice == "0":
            return

        elif choice == "1":
            battle.party_menu(player)

        elif choice == "2":
            dialogue.clear_screen()
            print("Bag ainda nao implementado.")
            dialogue.next_dialogue()

        elif choice == "3":
            dialogue.clear_screen()
            print("Sair ainda nao implementado.")
            dialogue.next_dialogue()

        elif choice == "4":
            dialogue.clear_screen()
            print("Salvar ainda nao implementado.")
            dialogue.next_dialogue()

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()


def route_1(player):

    steps = 0

    while True:
        dialogue.clear_screen()

        print("--- ROTA 1 ---\n")
        print(f"Progresso: {steps}/5\n")

        print("1- ANDAR")
        print("2- ANDAR NA GRAMA")
        print("3- MENU")

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
            player_menu(player)

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue() 


def viridian_city(player):
    while True:
        dialogue.clear_screen()

        print("--- CIDADE DE VIRIDIAN ---\n")

        print("1- IR PARA A ROTA 2")
        print("2- VOLTAR PARA A ROTA 1")
        print("3- CENTRO POKEMON")
        print("4- MENU")

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
            player_menu(player)

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

        print("1- ANDAR")
        print("2- ANDAR NA GRAMA")
        print("3- VOLTAR PARA VIRIDIAN")
        print("4- MENU")

        choice = input("\nEscolha: ")

        if choice == "1":
            steps += 1

            if steps >= 5:
                dialogue.clear_screen()
                print(f"{player.name} chegou ao Bosque Viridian!")
                dialogue.next_dialogue()

                steps = 0

                result = viridian_forest(player)

                if result == "FAINTED":
                    steps = 0
                    return

        elif choice == "2":
            result = wild_encounter(player, route_2_pokemons)

            if result == "LOSE":
                dialogue.clear_screen()
                print(f"Sem Pokémon para batalhar, {player.name} retorna para o Centro Pokemon mais proximo para recuperar sua equipe.")
                dialogue.next_dialogue()

                for pokemon in player.party:
                    pokemon.heal_full()

                steps = 0

                return

        elif choice == "3":
            return
        
        elif choice == "4":
            player_menu(player)

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue() 


def viridian_forest(player):

    steps = 0

    while True:
        dialogue.clear_screen()

        print("--- BOSQUE VIRIDIAN ---\n")
        print(f"Progresso: {steps}/5\n")

        print("1- ANDAR")
        print("2- ANDAR NA GRAMA")
        print("3- VOLTAR PARA ROTA 2")
        print("4- MENU")

        choice = input("\nEscolha: ")

        if choice == "1":
            steps += 1

            if steps >= 5:
                dialogue.clear_screen()
                print(f"{player.name} chegou a Rota 3!")
                dialogue.next_dialogue()

                steps = 0

                result = route_3(player)

                if result == "FAINTED":
                    return result

        elif choice == "2":
            result = wild_encounter(player, viridian_forest_pokemons)

            if result == "LOSE":
                dialogue.clear_screen()
                print(f"Sem Pokémon para batalhar, {player.name} retorna para o Centro Pokemon mais proximo para recuperar sua equipe.")
                dialogue.next_dialogue()

                for pokemon in player.party:
                    pokemon.heal_full()

                steps = 0

                return "FAINTED"

        elif choice == "3":
            return
        
        elif choice == "4":
            player_menu(player)

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue() 


def route_3(player):
    
    steps = 0

    while True:
        dialogue.clear_screen()

        print("--- ROTA 3 ---\n")
        print(f"Progresso: {steps}/5\n")

        print("1- ANDAR")
        print("2- ANDAR NA GRAMA")
        print("3- VOLTAR PARA BOSQUE VIRIDIAN")
        print("4- MENU")

        choice = input("\nEscolha: ")

        if choice == "1":
            steps += 1

            if steps >= 5:
                dialogue.clear_screen()
                print(f"{player.name} chegou a Cidade de Pewter!")
                dialogue.next_dialogue()

                steps = 0

                pewter_city(player)

        elif choice == "2":
            result = wild_encounter(player, route_3_pokemons)

            if result == "LOSE":
                dialogue.clear_screen()
                print(f"Sem Pokémon para batalhar, {player.name} retorna para o Centro Pokemon mais proximo para recuperar sua equipe.")
                dialogue.next_dialogue()

                for pokemon in player.party:
                    pokemon.heal_full()

                steps = 0

                return "FAINTED"

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


def pewter_city(player):
    while True:
        dialogue.clear_screen()

        print("--- CIDADE DE PEWTER ---\n")

        print("1- VOLTAR PARA ROTA 3")
        print("2- GINASIO DO BROCK")
        print("3- CENTRO POKEMON")
        print("4- MENU")

        choice = input("\nEscolha: ")

        if choice == "1":
           return

        elif choice == "2":
            pewter_gym(player)

        elif choice == "3":
            pokemon_center(player)

        elif choice == "4":
            player_menu(player)

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()


def pewter_gym(player):

    gym_trainer = trainer.gym_trainer()
    brock = trainer.gym_leader_brock()

    if player.pewter_gym_defeated:
        dialogue.clear_screen()
        print("Lider de ginasio ja derrotado, nao e possivel batalhar novamente!")
        dialogue.next_dialogue()
        return

    dialogue.clear_screen()
    print(f"{player.name} entrou no Ginasio!")
    dialogue.next_dialogue()

    while True:
        dialogue.clear_screen()

        print("--- GINASIO DE PEWTER ---\n")
        print("1- DESAFIAR TREINADOR LIAM")
        print("2- DESAFIAR LIDER DE GINASIO BROCK")
        print("3- SAIR DO GINASIO")
        print("4- MENU")

        choice = input("\nEscolha: ")

        if choice == "1":
            if gym_trainer.defeated == False:
                result = battle.trainer_battle(player, gym_trainer)

                if result == "WIN":
                    gym_trainer.defeated = True

            else:
                dialogue.clear_screen()
                print("Treinador ja derrotado, nao e possivel batalhar novamente!")
                dialogue.next_dialogue()

        elif choice == "2":
            if brock.defeated == False:
                result = battle.trainer_battle(player, brock)

                if result == "WIN":
                    dialogue.clear_screen()
                    print(f"PARABENS! {player.name} venceu o Lider de Ginasio, Brock! e conquistou sua Insígnia de pedra!")
                    dialogue.next_dialogue()

                    brock.defeated = True
                    player.pewter_gym_defeated = True

                    return

        elif choice == "3":
            return

        elif choice == "4":
            player_menu(player)

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()