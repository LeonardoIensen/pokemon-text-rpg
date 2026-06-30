import dialogue
import random

pokemon_data = {

    "CHARMANDER": {
        "element": "FIRE",
        "hp": 50,
        "attack": 70,
        "defense": 50,
        "speed": 60,
        "base_exp": 65,

        "moves": [
            "SCRATCH",
        ]
    },

    "CHARMELEON": {
        "element": "FIRE",
        "hp": 75,
        "attack": 73,
        "defense": 73,
        "speed": 97,
        "base_exp": 145,

        "moves": [
            "SCRATCH",
            "EMBER",
            "METAL CLAW",
            "FLAME WHEEL",
        ]
    },

    "BULBASAUR": {
        "element": "GRASS / POISON",
        "hp": 50,
        "attack": 60,
        "defense": 60,
        "speed": 50,
        "base_exp": 65,

        "moves": [
            "TACKLE",
        ]
    },

    "IVYSAUR": {
        "element": "GRASS / POISON",
        "hp": 70,
        "attack": 67,
        "defense": 67,
        "speed": 80,
        "base_exp": 145,

        "moves": [
            "TACKLE",
            "VINE WHIP",
            "SLAM",
            "RAZOR LEAF",
        ]
    },

    "SQUIRTLE": {
        "element": "WATER",
        "hp": 50,
        "attack": 60,
        "defense": 70,
        "speed": 50,
        "base_exp": 65,

        "moves": [
            "TACKLE",
        ]
    },

    "WARTORTLE": {
        "element": "WATER",
        "hp": 78,
        "attack": 67,
        "defense": 87,
        "speed": 67,
        "base_exp": 145,

        "moves": [
            "TACKLE",
            "BUBBLE",
            "WATER GUN",
            "BITE",
        ]
    },

    "PIKACHU": {
        "element": "ELECTRIC",
        "hp": 30,
        "attack": 70,
        "defense": 40,
        "speed": 90,
        "base_exp": 65,

        "moves": [
            "THUNDER SHOCK",
        ]
    },

    "RATTATA": {
        "element": "NORMAL",
        "hp": 40,
        "attack": 50,
        "defense": 40,
        "speed": 50,
        "base_exp": 60,

        "moves": [
            "TACKLE",
        ]
    },

    "RATICATE": {
        "element": "NORMAL",
        "hp": 60,
        "attack": 95,
        "defense": 85,
        "speed": 120,
        "base_exp": 140,

        "moves": [
            "TACKLE",
            "QUICK ATTACK",
            "HYPER FANG",
        ]
    },

    "PIDGEY": {
        "element": "NORMAL / FLYING",
        "hp": 50,
        "attack": 40,
        "defense": 40,
        "speed": 50,
        "base_exp": 60,

        "moves": [
            "TACKLE",
        ]
    },

    "PIDGEOTTO": {
        "element": "NORMAL / FLYING",
        "hp": 75,
        "attack": 82,
        "defense": 70,
        "speed": 85,
        "base_exp": 140,

        "moves": [
            "TACKLE",
            "GUST",
            "QUICK ATTACK",
        ]
    },

    "SPEAROW": {
        "element": "NORMAL / FLYING",
        "hp": 40,
        "attack": 60,
        "defense": 40,
        "speed": 70,
        "base_exp": 60,

        "moves": [
            "PECK",
        ]
    },

    "FEAROW": {
        "element": "NORMAL / FLYING",
        "hp": 65,
        "attack": 100,
        "defense": 73,
        "speed": 100,
        "base_exp": 140,

        "moves": [
            "PECK",
            "GUST",
            "FURY ATTACK",
        ]
    },

    "MANKEY": {
        "element": "FIGHT",
        "hp": 40,
        "attack": 70,
        "defense": 40,
        "speed": 70,
        "base_exp": 60,

        "moves": [
            "SCRATCH",
        ]
    },

    "NIDORAN": {
        "element": "POISON",
        "hp": 45,
        "attack": 60,
        "defense": 50,
        "speed": 40,
        "base_exp": 60,

        "moves": [
            "PECK",
        ]
    },

    "NIDORINO": {
        "element": "POISON",
        "hp": 70,
        "attack": 95,
        "defense": 70,
        "speed": 70,
        "base_exp": 140,

        "moves": [
            "POISON STING",
            "DOUBLE KICK",
            "PECK",
        ]
    },

    "CATERPIE": {
        "element": "BUG",
        "hp": 40,
        "attack": 40,
        "defense": 40,
        "speed": 40,
        "base_exp": 60,

        "moves": [
            "TACKLE",
        ]
    },

    "METAPOD": {
        "element": "BUG",
        "hp": 50,
        "attack": 30,
        "defense": 70,
        "speed": 30,
        "base_exp": 70,

        "moves": [
            "TACKLE",
        ]
    },

    "BUTTERFREE": {
        "element": "BUG / FLYING",
        "hp": 60,
        "attack": 55,
        "defense": 65,
        "speed": 72,
        "base_exp": 140,

        "moves": [
            "CONFUSION",
            "GUST",
        ]
    },

    "WEEDLE": {
        "element": "BUG / POISON",
        "hp": 40,
        "attack": 30,
        "defense": 30,
        "speed": 50,
        "base_exp": 60,

        "moves": [
            "POISON STING",
        ]
    },

    "KAKUNA": {
        "element": "BUG / POISON",
        "hp": 50,
        "attack": 30,
        "defense": 70,
        "speed": 30,
        "base_exp": 70,

        "moves": [
            "POISON STING",
        ]
    },

    "BEEDRILL": {
        "element": "BUG / POISON",
        "hp": 70,
        "attack": 80,
        "defense": 55,
        "speed": 85,
        "base_exp": 140,

        "moves": [
            "POISON STING",
            "FURY ATTACK",
        ]
    },

}

moves_data = {

    "SCRATCH": {
        "power": 40,
        "accuracy": 100,
        "type": "NORMAL"
    },

    "TACKLE": {
        "power": 35,
        "accuracy": 95,
        "type": "NORMAL"
    },

    "FURY ATTACK": {
        "power": 15,
        "accuracy": 90,
        "type": "NORMAL"
    },

    "SLASH": {
        "power": 70,
        "accuracy": 95,
        "type": "NORMAL"
    },

    "QUICK ATTACK": {
        "power": 40,
        "accuracy": 100,
        "type": "NORMAL"
    },

    "HYPER FANG": {
        "power": 80,
        "accuracy": 90,
        "type": "NORMAL"
    },

    "SLAM": {
        "power": 60,
        "accuracy": 85,
        "type": "NORMAL"
    },

    "EMBER": {
        "power": 40,
        "accuracy": 100,
        "type": "FIRE"
    },
    
    "FLAME WHEEL": {
        "power": 60,
        "accuracy": 100,
        "type": "FIRE"
    },

    "FLAMETHROWER": {
        "power": 95,
        "accuracy": 100,
        "type": "FIRE"
    },

    "VINE WHIP": {
        "power": 35,
        "accuracy": 95,
        "type": "GRASS"
    },

    "RAZOR LEAF": {
        "power": 55,
        "accuracy": 95,
        "type": "GRASS"
    },

    "GIGA DRAIN": {
        "power": 60,
        "accuracy": 100,
        "type": "GRASS"
    },

    "BUBBLE": {
        "power": 30,
        "accuracy": 100,
        "type": "WATER"
    },

    "WATER GUN": {
        "power": 40,
        "accuracy": 100,
        "type": "WATER"
    },

    "WATER PULSE": {
        "power": 60,
        "accuracy": 100,
        "type": "WATER"
    },

    "BITE": {
        "power": 60,
        "accuracy": 100,
        "type": "DARK"
    },

    "THUNDER SHOCK": {
        "power": 40,
        "accuracy": 100,
        "type": "ELECTRIC"
    },

    "THUNDERBOLT": {
        "power": 95,
        "accuracy": 100,
        "type": "ELECTRIC"
    },

    "PECK": {
        "power": 35,
        "accuracy": 95,
        "type": "FLYING"
    },

    "GUST": {
        "power": 40,
        "accuracy": 100,
        "type": "FLYING"
    },

    "POISON STING": {
        "power": 15,
        "accuracy": 100,
        "type": "POISON"
    },

    "CONFUSION": {
        "power": 50,
        "accuracy": 100,
        "type": "PSYCHIC"
    },

    "METAL CLAW": {
        "power": 50,
        "accuracy": 95,
        "type": "STEEL"
    },

    "DOUBLE KICK": {
        "power": 30,
        "accuracy": 100,
        "type": "FIGHT"
    },

    "LOW KICK": {
        "power": 30,
        "accuracy": 100,
        "type": "FIGHT"
    },

    "KARATE CHOP": {
        "power": 50,
        "accuracy": 100,
        "type": "FIGHT"
    },

}

class Pokemon:
    def __init__(self, name, level):
        self.name = name
        data = pokemon_data[name]
        self.level = level
        self.exp = 0

        self.element_type = data["element"]
        self.base_hp = data["hp"]
        self.base_attack = data["attack"]
        self.base_defense = data["defense"]
        self.base_speed = data["speed"]
        self.moves = data["moves"].copy()
        self.base_exp = data["base_exp"]

        self.calculate_stats()
        self.heal_to_full()

    def calculate_stats(self):

        self.max_hp = int(((self.base_hp * 2) * self.level) / 100) + self.level + 10

        self.attack = int(((self.base_attack * 2) * self.level) / 100) + 5
        self.defense = int(((self.base_defense * 2) * self.level) / 100) + 5
        self.speed = int(((self.base_speed * 2) * self.level) / 100) + 5

        self.exp_to_next_level = self.level * 10

    def heal_to_full(self):
        self.current_hp = self.max_hp

    def gain_exp(self, amount):
        self.exp = self.exp + amount

        dialogue.narration(f"\n{self.name} gained {amount} EXP!")

        while self.exp >= self.exp_to_next_level:

            self.exp = self.exp - self.exp_to_next_level
            self.level = self.level + 1
            dialogue.narration(f"\n{self.name} grew to Lv{self.level}!")

            self.calculate_stats()
            self.heal_to_full()

    def show_stats(self):
        
        print("\n--- POKEMON STATS ---")
        print(f"NAME : {self.name} Lv{self.level}")
        print(f"TYPE : {self.element_type}")

        print()

        print(f"HP : {self.current_hp}/{self.max_hp}")
        print(f"EXP : {self.exp}/{self.exp_to_next_level}")
        print(f"ATTACK : {self.attack}")
        print(f"DEFENSE : {self.defense}")
        print(f"SPEED : {self.speed}")

        print("\nMOVES:")

        for move in self.moves:
            print(f"- {move}")

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
            dialogue.clear_screen()
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
