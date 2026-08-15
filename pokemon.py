import dialogue

pokedex = {

    "BULBASAUR": {
        "type": "GRASS / POISON",
        "hp": 50,
        "attack": 60,
        "defense": 60,
        "speed": 50,
    },

    "SQUIRTLE": {
        "type": "WATER",
        "hp": 50,
        "attack": 60,
        "defense": 70,
        "speed": 50,
    },

    "CHARMANDER": {
        "type": "FIRE",
        "hp": 50,
        "attack": 70,
        "defense": 50,
        "speed": 60,
    },

    "RATTATA": {
        "type": "NORMAL",
        "hp": 40,
        "attack": 50,
        "defense": 40,
        "speed": 50,
    }

}

class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

        self.type = pokedex[name]["type"]
        self.base_hp = pokedex[name]["hp"]
        self.base_attack = pokedex[name]["attack"]
        self.base_defense = pokedex[name]["defense"]
        self.base_speed = pokedex[name]["speed"]

        self.calculate_stats()
        self.heal_full()

    def calculate_stats(self):

        self.max_hp = int(((self.base_hp * 2) * self.level) / 100) + self.level + 10

        self.attack = int(((self.base_attack * 2) * self.level) / 100) + 5
        self.defense = int(((self.base_defense * 2) * self.level) / 100) + 5
        self.speed = int(((self.base_speed * 2) * self.level) / 100) + 5

    def heal_full(self):
        self.current_hp = self.max_hp
        
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