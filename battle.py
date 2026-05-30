import dialogue
import pokemon

def show_battle_stats(player_starter, rival_starter):
    print("\n-----------------------")

    print(f"RIVAL: {rival_starter.name} Lv{rival_starter.level}")
    print(f"HP: {rival_starter.current_hp}/{rival_starter.max_hp}")

    print("\nVS\n")

    print(f"YOUR: {player_starter.name} Lv{player_starter.level}")
    print(f"HP: {player_starter.current_hp}/{player_starter.max_hp}")

    print("-----------------------\n")

def fight_menu(player_starter):
    while True:
        print("\nMOVES\n")

        for i, move in enumerate(player_starter.moves, 1):
            move_type = pokemon.moves_data[move]["type"]

            print(f"{i} - {move} ({move_type})")

        print("0 - BACK")

        choice = input("\nChoose: ")

        if choice == "0":
            return



def battle_menu(player_starter, rival_starter):
    while True:  

        show_battle_stats(player_starter, rival_starter)

        print(f"\nWhat will {player_starter.name} do?\n")

        print("1 - FIGHT")
        print("2 - POKEMON")
        print("3 - BAG")
        print("4 - RUN")

        choice = input("\nChoose: ")

        if choice == "1":
            fight_menu(player_starter)

        elif choice == "2":
            print()

        elif choice == "3":
            print()

        elif choice == "4":
            print()

        else:
            print()

def rival_first_battle(
    player_name,
    rival_name,
    player_starter,
    rival_starter
):
    dialogue.talk(f"{rival_name}", f"{player_name}! Let's check out our POKEMON!")
    dialogue.talk(f"{rival_name}", "Come on, I'll take you on!")

    dialogue.narration(f"\n{rival_name} challenges you to a battle!")
    dialogue.next_dialogue()

    dialogue.narration(f"\n{rival_name} sent out {rival_starter.name}!")
    dialogue.next_dialogue()

    dialogue.narration(f"\nGo! {player_starter.name}!")
    dialogue.next_dialogue()

    battle_menu(player_starter, rival_starter)