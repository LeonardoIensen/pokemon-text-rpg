import dialogue
import items
import save

def confirm_exit():
    while True:
        dialogue.clear_screen()

        print("\nAre you sure you want to exit?\n")
        print("1 - YES")
        print("2 - NO")

        choice = input("\nChoose: ")

        if choice == "1":
            dialogue.clear_screen()
            dialogue.narration("\nReturning to title screen...")
            dialogue.next_dialogue()

            return "TITLE"

        elif choice == "2":
            return None
    
        else:
            dialogue.clear_screen()
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()

def player_menu(player_pokemon):

    while True:
        dialogue.clear_screen()

        print("\n--- MENU ---\n")
        print("1 - POKEMON")
        print("2 - BAG")
        print("3 - SAVE")
        print("4 - EXIT")
        print("0 - BACK")

        choice = input("\nChoose: ")

        if choice == "1":
            dialogue.clear_screen()

            player_pokemon.show_stats()
            dialogue.next_dialogue()

        elif choice == "2":
            items.open_bag()

        elif choice == "3":
            save.save_game()

        elif choice == "4":
            result = confirm_exit()

            if result == "TITLE":
                return result

        elif choice == "0":
            dialogue.clear_screen()
            return

        else:
            dialogue.clear_screen()
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()