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


def check_route_trainer(player, route_trainers, steps):
    for t_data in route_trainers.values():
        if steps == t_data["step"] and not t_data["defeated"]:
            dialogue.clear_screen()
            dialogue.talk(t_data["name"], t_data["intro"])

            first_poke_name, first_poke_level = t_data["pokemons"][0]
            first_pokemon = pokemon.Pokemon(first_poke_name, first_poke_level)
            npc_trainer = trainer.Trainer(t_data["name"], first_pokemon)

            for poke_name, poke_level in t_data["pokemons"][1:]:
                npc_trainer.add_pokemon(pokemon.Pokemon(poke_name, poke_level))

            result = battle.trainer_battle(player, npc_trainer)

            if result == "WIN":
                print()
                dialogue.talk(t_data["name"], t_data["lose_msg"])
                t_data["defeated"] = True
                return "WIN"

            elif result == "LOSE":
                print()
                dialogue.talk(t_data["name"], t_data["win_msg"])
                dialogue.clear_screen()
                print(f"Sem Pokémon para batalhar, {player.name} retorna para o Centro Pokémon mais próximo para recuperar sua equipe.")
                dialogue.next_dialogue()

                for p in player.party:
                    p.heal_full()

                return "FAINTED"

    return None


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
    while True:
        dialogue.clear_screen()

        print("--- CENTRO POKÉMON ---\n")
        print("1- CURAR POKEMONS")
        print("2- ACESSAR PC")
        print("\n0- SAIR")

        choice = input("\nEscolha: ")

        if choice == "0":
            return

        if choice == "1":
            dialogue.clear_screen()
            print("Enfermeira Joy: Olá! Bem-vindo ao Centro Pokémon.\n")
            print("Nós curamos seus Pokémon desmaiados ou feridos até sua saúde total.")
            dialogue.next_dialogue()

            for pokemon in player.party:
                pokemon.heal_full()

            dialogue.clear_screen()
            print("Enfermeira Joy: Seus POKÉMON foram totalmente restaurados! Esperamos ver você novamente!")
            dialogue.next_dialogue()

        elif choice == "2":
            pc_menu(player)

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()


def view_pc_box(player):
    while True:
        dialogue.clear_screen()

        print("--- BOX PC ---\n")
        for i, pokemon in enumerate(player.pc_box, start=1):
            print(f"{i}- {pokemon.name:<12} LV {pokemon.level}")

        print("\n0- VOLTAR")

        try:
            choice = int(input("\nEscolha um Pokémon para ver o sumário: "))

        except ValueError:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()

            continue

        if choice == 0:
            return

        if 1 <= choice <= len(player.pc_box):
            selected_pokemon = player.pc_box[choice - 1]
            battle.show_summary(selected_pokemon)

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()


def deposit_pokemon_menu(player):
    if len(player.party) <= 1:
        dialogue.clear_screen()
        print("Você precisa ter pelo menos um Pokémon na party!")
        dialogue.next_dialogue()

        return

    while True:
        dialogue.clear_screen()

        print("--- PARTY ---\n")
        for i, pokemon in enumerate(player.party, start=1):
            print(f"{i}- {pokemon.name:<12} LV {pokemon.level}")

        print("\n0- VOLTAR")

        try:
            choice = int(input("\nEscolha qual deseja depositar no PC: "))

        except ValueError:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()

            continue

        if choice == 0:
            return

        if 1 <= choice <= len(player.party):
            index = choice - 1

            deposited_pokemon = player.party.pop(index)
            player.pc_box.append(deposited_pokemon)

            dialogue.clear_screen()
            print(f"{deposited_pokemon.name} foi guardado no PC!")
            dialogue.next_dialogue()

            return
        
        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()


def withdraw_pokemon_menu(player):
    if len(player.party) >= 3:
        dialogue.clear_screen()
        print("Sua equipe ja esta cheia! (MAX 3 POKEMONS)")
        dialogue.next_dialogue()

        return

    while True:
        dialogue.clear_screen()

        print("--- BOX PC ---\n")
        for i, pokemon in enumerate (player.pc_box, start=1):
            print(f"{i}- {pokemon.name:<12} LV {pokemon.level}")

        print("\n0- VOLTAR")

        try:
            choice = int(input("\nEscolha qual deseja retirar no PC: "))

        except ValueError:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()

            continue

        if choice == 0:
            return

        if 1 <= choice <= len(player.pc_box):
            index = choice - 1

            withdrawn_pokemon = player.pc_box.pop(index)
            player.party.append(withdrawn_pokemon)

            dialogue.clear_screen()
            print(f"{withdrawn_pokemon.name} foi colocado na equipe!")
            dialogue.next_dialogue()

            return
        
        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()


def pc_menu(player):
    while True:
        dialogue.clear_screen()

        print("--- PC ---\n")
        print("1- VER POKEMONS")
        print("2- RETIRAR POKEMONS")
        print("3- DEPOSITAR POKEMONS")
        print("\n0- VOLTAR")

        choice = input("\nEscolha: ")

        if choice == "0":
            return

        if choice == "1":
            if len(player.pc_box) == 0:
                dialogue.clear_screen()
                print("Seu PC esta vazio!")
                dialogue.next_dialogue()

            else:
                view_pc_box(player)

        elif choice == "2":
             if len(player.pc_box) == 0:
                dialogue.clear_screen()
                print("Seu PC esta vazio!")
                dialogue.next_dialogue()
            
             else:
                withdraw_pokemon_menu(player)

        elif choice == "3":
            deposit_pokemon_menu(player)

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
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
            battle.bag(player)

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


def route_1(player, rival):

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

            trainer_result = check_route_trainer(player, trainer.route_1_trainers, steps)

            if trainer_result == "FAINTED":
                steps = 0
                return

            if steps >= 5:
                dialogue.clear_screen()
                print(f"{player.name} chegou a cidade de Viridian!")
                dialogue.next_dialogue()

                steps = 0

                viridian_city(player, rival)

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


def viridian_city(player, rival):
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

            route_2(player, rival)

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


def route_2(player, rival):

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

            trainer_result = check_route_trainer(player, trainer.route_2_trainers, steps)

            if trainer_result == "FAINTED":
                steps = 0
                return            

            if steps >= 5:

                if not rival.defeated:
                    result = battle.rival_second_battle(player, rival)

                    if result == "LOSE":
                        dialogue.clear_screen()
                        print(f"Sem Pokémon para batalhar, {player.name} retorna para o Centro Pokémon mais próximo.")
                        dialogue.next_dialogue()

                        for pokemon in player.party:
                            pokemon.heal_full()

                            steps = 0
                            return "FAINTED"

                    rival.defeated = True  

                dialogue.clear_screen()
                print(f"{player.name} chegou ao Bosque Viridian!")
                dialogue.next_dialogue()

                steps = 0

                result = viridian_forest(player, rival)

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


def viridian_forest(player, rival):

    steps = 0

    while True:
        dialogue.clear_screen()

        print("--- BOSQUE VIRIDIAN ---\n")
        print(f"Progresso: {steps}/8\n")

        print("1- ANDAR")
        print("2- ANDAR NA GRAMA")
        print("3- VOLTAR PARA ROTA 2")
        print("4- MENU")

        choice = input("\nEscolha: ")

        if choice == "1":
            steps += 1

            trainer_result = check_route_trainer(player, trainer.viridian_forest_trainers, steps)

            if trainer_result == "FAINTED":
                steps = 0
                return

            if steps >= 8:
                dialogue.clear_screen()
                print(f"{player.name} chegou a Rota 3!")
                dialogue.next_dialogue()

                steps = 0

                result = route_3(player, rival)

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


def route_3(player, rival):
    
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

            trainer_result = check_route_trainer(player, trainer.route_3_trainers, steps)

            if trainer_result == "FAINTED":
                steps = 0
                return

            if steps >= 5:
                dialogue.clear_screen()
                print(f"{player.name} chegou a Cidade de Pewter!")
                dialogue.next_dialogue()

                steps = 0

                pewter_city(player, rival)

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
            player_menu(player)

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()


def pewter_city(player, rival):
    while True:
        dialogue.clear_screen()

        print("--- CIDADE DE PEWTER ---\n")

        print("1- VOLTAR PARA ROTA 3")
        print("2- GINASIO DO BROCK")
        print("3- CENTRO POKEMON")
        print("4- DESAFIAR RIVAL")
        print("5- MENU")

        choice = input("\nEscolha: ")

        if choice == "1":
           return

        elif choice == "2":
            pewter_gym(player)

        elif choice == "3":
            pokemon_center(player)

        elif choice == "4":
            if not player.pewter_gym_defeated:
                dialogue.clear_screen()
                print("Você precisa derrotar o Líder Brock primeiro!")
                dialogue.next_dialogue()

            else:
                battle.rival_third_battle(player, rival)

        elif choice == "5":
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

                elif result == "LOSE":
                    dialogue.clear_screen()
                    print(f"Sem Pokémon para batalhar, {player.name} retorna para o Centro Pokémon mais próximo para recuperar sua equipe.")
                    dialogue.next_dialogue()

                    for pokemon in player.party:
                        pokemon.heal_full()

                    return

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

                elif result == "LOSE":
                    dialogue.clear_screen()
                    print(f"Sem Pokémon para batalhar, {player.name} retorna para o Centro Pokémon mais próximo para recuperar sua equipe.")
                    dialogue.next_dialogue()

                    for pokemon in player.party:
                        pokemon.heal_full()

                    return

            else:
                dialogue.clear_screen()
                print("Lider de ginasio ja derrotado, nao e possivel batalhar novamente!")
                dialogue.next_dialogue()

        elif choice == "3":
            return

        elif choice == "4":
            player_menu(player)

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()