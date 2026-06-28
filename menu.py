import dialogue
import items

def player_menu(player_pokemon):

    while True:
        dialogue.clear_screen()

        print("\n--- MENU ---\n")
        print("1- POKEMON")
        print("2- BAG")
        print("3- SAVE")
        print("4- EXIT")
        print("0- BACK")

        choice = input("\nChoose: ")

        if choice == "1":
            dialogue.clear_screen()

            player_pokemon.show_stats()
            dialogue.next_dialogue()

        elif choice == "2":
            items.open_bag()

        elif choice == "3":
            dialogue.clear_screen()
            dialogue.narration("\nSave is not available yet.")
            dialogue.next_dialogue()

        elif choice == "4":
            dialogue.clear_screen()
            dialogue.narration("\nExit is not available yet.")
            dialogue.next_dialogue()

        elif choice == "0":
            dialogue.clear_screen()
            return

        else:
            dialogue.clear_screen()
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()