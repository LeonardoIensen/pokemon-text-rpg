import dialogue
import pokemon
import trainer
import battle
import map

while True:

    print("--- POKEMON RPG ---\n")
    print("1 - NOVO JOGO")
    print("2 - CONTINUAR")
    print("3 - SAIR")

    opcao = input("\nDigite sua escolha: ")

    if opcao == "1":
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

        map.route_1(player)

    elif opcao == "2":
        dialogue.clear_screen()
        print("Funcao ainda nao implementada!")
        dialogue.next_dialogue()

    elif opcao == "3":
        dialogue.clear_screen()
        print("Saindo do jogo...")
        dialogue.next_dialogue()
        break

    else:
        dialogue.clear_screen()
        print("[ Opcao invalida! Tente novamente. ]")
        dialogue.next_dialogue()

    