import dialogue

def show_battle_stats(player_pokemon, enemy_pokemon):
    print("------------------")

    print(f"{enemy_pokemon.name} Lv{enemy_pokemon.level}")
    print(f"HP: {enemy_pokemon.current_hp}/{enemy_pokemon.max_hp}")

    print("\nVS\n")

    print(f"{player_pokemon.name} Lv{player_pokemon.level}")
    print(f"HP: {player_pokemon.current_hp}/{player_pokemon.max_hp}")

    print("------------------\n")

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
            print("Nao implementado.")

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