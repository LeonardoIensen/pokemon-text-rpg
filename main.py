import dialogue

while True:

    print("\n--- POKEMON RPG ---\n")
    print("1 - NOVO JOGO")
    print("2 - CONTINUAR")
    print("3 - SAIR")

    opcao = input("\nDigite sua escolha: ")

    if opcao == "1":
        dialogue.clear_screen()
        print("\nFuncao ainda nao implementada!")
        dialogue.next_dialogue()

    elif opcao == "2":
        dialogue.clear_screen()
        print("\nFuncao ainda nao implementada!")
        dialogue.next_dialogue()

    elif opcao == "3":
        dialogue.clear_screen()
        print("\nSaindo do jogo...")
        dialogue.next_dialogue()
        break

    else:
        dialogue.clear_screen()
        print("\n[Opcao invalida! Tente novamente.]")
        dialogue.next_dialogue()

    