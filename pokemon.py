import dialogue

pokedex = {

    "BULBASAUR": {
        "element": "GRASS / POISON",
        "hp": 50,
        "attack": 60,
        "defense": 60,
        "speed": 50,
    },

    "SQUIRTLE": {
        "element": "WATER",
        "hp": 50,
        "attack": 60,
        "defense": 70,
        "speed": 50,
    },

    "CHARMANDER": {
        "element": "FIRE",
        "hp": 50,
        "attack": 70,
        "defense": 50,
        "speed": 60,
    }

}
        
def show_menu_starters():
    print("--- STARTER POKEMON ---\n")
    print("1 - Bulbasaur")
    print("2 - Squirtle")
    print("3 - Charmander")

def choose_starter():

    show_menu_starters()

    while True:

        choice = input("\nEscolha seu inicial: ")

        if choice == "1":
            player_starter_name = "BULBASAUR"
            break

        elif choice == "2":
            player_starter_name = "SQUIRTLE"
            break

        elif choice == "3":
            player_starter_name = "CHARMANDER"
            break

        else:
            dialogue.clear_screen()
            print("[ Opcao invalida! Tente novamente. ]")
            dialogue.next_dialogue()

            show_menu_starters()

    return player_starter_name

def choose_rival_starter(player_starter):

    if player_starter == "BULBASAUR":
        rival_starter_name = "CHARMANDER"

    elif player_starter == "SQUIRTLE":
        rival_starter_name = "BULBASAUR"

    else:
        rival_starter_name = "SQUIRTLE"

    return rival_starter_name