import dialogue

def route_1(player_name):

    steps = 0

    dialogue.clear_screen()

    while True:

        print("\n--- ROUTE 1 ---")
        print(f"Progress: {steps}/10\n")

        print("1 - WALK")
        print("2 - WALK ON THE GRASS")
        print("3 - MENU")
        print("4 - MAP")

        choice = input("\nChoose: ")

        if choice == "1":
            dialogue.clear_screen()

            steps += 1

            dialogue.narration(f"\n{player_name} walked through Route 1... ({steps}/10)")
            dialogue.next_dialogue()

            if steps >= 10:
                dialogue.narration(f"\n{player_name} arrived in Viridian City!")
                dialogue.next_dialogue()
                break

        elif choice == "2":
            dialogue.clear_screen()

            dialogue.narration(f"\n{player_name} walked through the tall grass...")
            dialogue.narration("\nNothing happened yet.")
            dialogue.next_dialogue()

        elif choice == "3":
            dialogue.clear_screen()

            print("\nMenu is not available yet.")
            dialogue.next_dialogue()

        elif choice == "4":
            dialogue.clear_screen()

            print("\nMap is not available yet.")
            dialogue.next_dialogue()

        else:
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()
            
