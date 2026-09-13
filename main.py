import dialogue
import pokemon
import trainer
import battle
import map
import save

while True:
    dialogue.clear_screen()

    print("--- POKEMON RPG ---\n")
    print("1 - NOVO JOGO")
    print("2 - CONTINUAR")
    print("3 - SAIR")

    opcao = input("\nDigite sua escolha: ")

    if opcao == "1":
        if save.has_save_file():
            dialogue.clear_screen()
            print("Você já tem um jogo salvo antigo.\nDeseja começar um NOVO JOGO mesmo?\n")
            print("1 - SIM")
            print("2 - NAO")

            confirm = input("\nEscolha: ")

            if confirm != "1":
                continue

        dialogue.clear_screen()

        player_name, rival_name = dialogue.intro()

        dialogue.start_journey(player_name, rival_name)

        player_starter = pokemon.choose_starter(player_name)
        rival_starter = pokemon.choose_rival_starter(player_starter, rival_name)

        player_pokemon = pokemon.Pokemon(player_starter, 5)
        rival_pokemon = pokemon.Pokemon(rival_starter, 5)

        player = trainer.Trainer(player_name, player_pokemon)
        rival = trainer.Trainer(rival_name, rival_pokemon)

        battle.rival_first_battle(player, rival)

        map.route_1(player, rival)

    elif opcao == "2":
        if not save.has_save_file():
            dialogue.clear_screen()
            print("Nenhum jogo salvo foi encontrado!")
            dialogue.next_dialogue()
        else:
            player, rival, location, steps = save.load_game()
            map.load_saved_location(player, rival, location, steps)

    elif opcao == "3":
        dialogue.clear_screen()
        print("Saindo do jogo...")
        dialogue.next_dialogue()
        break

    else:
        dialogue.clear_screen()
        print("[ Opcao invalida! Tente novamente. ]")
        dialogue.next_dialogue()