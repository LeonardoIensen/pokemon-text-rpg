import dialogue

pokedex = {

    "BULBASAUR": {
        "type": "GRASS / POISON",
        "hp": 50,
        "attack": 60,
        "defense": 60,
        "speed": 50,
        "base_exp": 60,

        "moves": [
            "TACKLE"
        ],
    },

    "SQUIRTLE": {
        "type": "WATER",
        "hp": 50,
        "attack": 60,
        "defense": 70,
        "speed": 50,
        "base_exp": 60,

        "moves": [
            "TACKLE"
        ],
    },

    "CHARMANDER": {
        "type": "FIRE",
        "hp": 50,
        "attack": 70,
        "defense": 50,
        "speed": 60,
        "base_exp": 60,

        "moves": [
            "SCRATCH"
        ],
    },

    "RATTATA": {
        "type": "NORMAL",
        "hp": 40,
        "attack": 50,
        "defense": 40,
        "speed": 50,
        "base_exp": 50,

        "moves": [
            "TACKLE"
        ],
    },

    "PIDGEY": {
        "type": "NORMAL / FLYING",
        "hp": 40,
        "attack": 50,
        "defense": 40,
        "speed": 60,
        "base_exp": 50,

        "moves": [
            "TACKLE"
        ],
    },

    "SPEAROW": {
        "type": "NORMAL / FLYING",
        "hp": 40,
        "attack": 60,
        "defense": 40,
        "speed": 50,
        "base_exp": 50,

        "moves": [
            "PECK"
        ],
    },

    "MANKEY": {
        "type": "FIGHT",
        "hp": 40,
        "attack": 60,
        "defense": 40,
        "speed": 60,
        "base_exp": 50,

        "moves": [
            "SCRATCH"
        ],
    },

}

moves = {
    "SCRATCH": {
        "type": "NORMAL",
        "power": 40,
        "accuracy": 100,
    },

    "TACKLE": {
        "type": "NORMAL",
        "power": 40,
        "accuracy": 95,
    },

    "PECK": {
        "type": "FLYING",
        "power": 35,
        "accuracy": 100,
    },
}

class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.experience = 0

        self.type = pokedex[name]["type"]
        self.base_hp = pokedex[name]["hp"]
        self.base_attack = pokedex[name]["attack"]
        self.base_defense = pokedex[name]["defense"]
        self.base_speed = pokedex[name]["speed"]
        self.base_exp = pokedex[name]["base_exp"]
        self.moves = pokedex[name]["moves"]

        self.calculate_stats()
        self.heal_full()

    def calculate_stats(self):
        self.max_hp = int(((self.base_hp * 2) * self.level) / 100) + self.level + 10
        self.attack = int(((self.base_attack * 2) * self.level) / 100) + 5
        self.defense = int(((self.base_defense * 2) * self.level) / 100) + 5
        self.speed = int(((self.base_speed * 2) * self.level) / 100) + 5

    def exp_next_level(self):
        required_experience = self.level * 10

        return required_experience

    def gain_experience(self, experience_gained):
        self.experience = self.experience + experience_gained

        print(f"{self.name} ganhou {experience_gained} de EXP.!")

        while self.experience >= self.exp_next_level():
            required_experience = self.exp_next_level()

            self.level = self.level + 1

            print(f"{self.name} upou para o Lv{self.level}!")

            exceeded_exp = self.experience - required_experience
            self.experience = exceeded_exp

            self.calculate_stats()
            self.heal_full()

    def heal_full(self):
        self.current_hp = self.max_hp
        
def show_menu_starters():
    print("--- STARTER POKEMON ---\n")
    print("1 - Bulbasaur")
    print("2 - Squirtle")
    print("3 - Charmander")

def choose_starter(player_name):

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

    dialogue.clear_screen()
    print(f"{player_name} escolheu {player_starter_name}!")

    return player_starter_name

def choose_rival_starter(player_starter, rival_name):

    if player_starter == "BULBASAUR":
        rival_starter_name = "CHARMANDER"

    elif player_starter == "SQUIRTLE":
        rival_starter_name = "BULBASAUR"

    else:
        rival_starter_name = "SQUIRTLE"

    print(f"\n{rival_name} escolheu {rival_starter_name}!")
    dialogue.next_dialogue()

    return rival_starter_name