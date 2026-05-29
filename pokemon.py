import dialogue
import random

pokemon_data = {

    "CHARMANDER": {
        "element": "FIRE",
        "hp": 50,
        "attack": 70,
        "defense": 50,
        "speed": 60
    },

    "BULBASAUR": {
        "element": "GRASS",
        "hp": 50,
        "attack": 60,
        "defense": 60,
        "speed": 50
    },

    "SQUIRTLE": {
        "element": "WATER",
        "hp": 50,
        "attack": 60,
        "defense": 70,
        "speed": 50
    },

    "PIKACHU": {
        "element": "ELECTRIC",
        "hp": 30,
        "attack": 70,
        "defense": 40,
        "speed": 90
    },

}



class Pokemon:
    def __init__(self, name, level):
        self.name = name
        data = pokemon_data[name]
        self.level = level

        self.element_type = data["element"]
        self.base_hp = data["hp"]
        self.base_attack = data["attack"]
        self.base_defense = data["defense"]
        self.base_speed = data["speed"]

        self.calculate_stats()

    def calculate_stats(self):

        self.max_hp = int(((self.base_hp * 2) * self.level) / 100) + self.level + 10
        self.current_hp = self.max_hp

        self.attack = int(((self.base_attack * 2) * self.level) / 100) + 5
        self.defense = int(((self.base_defense * 2) * self.level) / 100) + 5
        self.speed = int(((self.base_speed * 2) * self.level) / 100) + 5

    def show_stats(self):
        
        print("\n--- POKEMON STATS ---")
        print(f"NAME : {self.name} Lv{self.level}")
        print(f"TYPE : {self.element_type}")

        print()

        print(f"HP : {self.current_hp}/{self.max_hp}")
        print(f"ATTACK : {self.attack}")
        print(f"DEFENSE : {self.defense}")
        print(f"SPEED : {self.speed}")

def show_menu_starters():
    print("\n--- STARTER POKEMON ---\n")
    print("1 - Bulbasaur")
    print("2 - Squirtle")
    print("3 - Charmander")
    print("4 - ???")

def choose_starter(player_name):

    show_menu_starters()

    while True:
        choice = input("\nChoose: ")

        if choice == "1":
            player_starter_name = "BULBASAUR"

        elif choice == "2":
            player_starter_name = "SQUIRTLE"

        elif choice == "3":
            player_starter_name = "CHARMANDER"

        elif choice == "4":
            player_starter_name = "PIKACHU"
            dialogue.narration("\nWait... a fourth Pokeball?")

        else:
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()

            show_menu_starters()

            continue


        player_starter = Pokemon(player_starter_name, 5)
        dialogue.narration(f"\n{player_name} received the {player_starter_name}!")
        dialogue.next_dialogue()
        return player_starter

def choose_rival_starter(player_starter, rival_name):

    dialogue.talk(f"{rival_name}", "I'll take this one, then!")

    if player_starter.name == "BULBASAUR":
        rival_starter_name = "CHARMANDER"

    elif player_starter.name == "SQUIRTLE":
        rival_starter_name = "BULBASAUR"


    elif player_starter.name == "CHARMANDER":
        rival_starter_name = "SQUIRTLE"

    else:
        starters = ["BULBASAUR", "SQUIRTLE", "CHARMANDER"]
        random_starter_name = random.choice(starters)
        rival_starter_name = random_starter_name
    
    rival_starter = Pokemon(rival_starter_name, 5)
    dialogue.narration(f"\n{rival_name} received the {rival_starter.name}!")
    dialogue.next_dialogue()
    return rival_starter
