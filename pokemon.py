import dialogue

MAX_LEVEL = 20
MAX_MOVES = 4

pokedex  = {

    "CHARMANDER": {
        "type": "FIRE",
        "hp": 50,
        "attack": 70,
        "defense": 50,
        "speed": 60,
        "base_exp": 65,

        "moves": [
            "SCRATCH",
        ],

        "learnset": {
            7: "EMBER",
            13: "METAL CLAW",
            16: "FLAME WHEEL",
        }
    },

    "CHARMELEON": {
        "type": "FIRE",
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
        ],
        
        "learnset": {
            18: "SLASH",
            20: "FLAMETHROWER",
        }
    },

    "BULBASAUR": {
        "type": "GRASS / POISON",
        "hp": 50,
        "attack": 60,
        "defense": 60,
        "speed": 50,
        "base_exp": 65,

        "moves": [
            "TACKLE",
        ],

        "learnset": {
            7: "VINE WHIP",
            13: "SLAM",
            16: "RAZOR LEAF",
        }
    },

    "IVYSAUR": {
        "type": "GRASS / POISON",
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
        ],

        "learnset": {
            18: "GIGA DRAIN",
        }
    },

    "SQUIRTLE": {
        "type": "WATER",
        "hp": 50,
        "attack": 60,
        "defense": 70,
        "speed": 50,
        "base_exp": 65,

        "moves": [
            "TACKLE",
        ],

        "learnset": {
            7: "BUBBLE",
            13: "WATER GUN",
            16: "BITE",
        }
    },

    "WARTORTLE": {
        "type": "WATER",
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
        ],

        "learnset": {
            18: "WATER PULSE",
        }
    },

    "PIKACHU": {
        "type": "ELECTRIC",
        "hp": 30,
        "attack": 70,
        "defense": 40,
        "speed": 90,
        "base_exp": 65,

        "moves": [
            "THUNDER SHOCK",
        ],

        "learnset": {
            7: "QUICK ATTACK",
            14: "SLAM",
            18: "THUNDERBOLT",
        }
    },

    "RATTATA": {
        "type": "NORMAL",
        "hp": 40,
        "attack": 50,
        "defense": 40,
        "speed": 50,
        "base_exp": 60,

        "moves": [
            "TACKLE",
        ],

        "learnset": {
            7: "QUICK ATTACK",
            12: "HYPER FANG",
            16: "SLAM",
        }
    },

    "RATICATE": {
        "type": "NORMAL",
        "hp": 60,
        "attack": 95,
        "defense": 85,
        "speed": 120,
        "base_exp": 140,

        "moves": [
            "TACKLE",
            "QUICK ATTACK",
            "HYPER FANG",
            "SLAM",
        ],

        "learnset": {
            20: "BITE",
        }
    },

    "PIDGEY": {
        "type": "NORMAL / FLYING",
        "hp": 50,
        "attack": 40,
        "defense": 40,
        "speed": 50,
        "base_exp": 60,

        "moves": [
            "TACKLE",
        ],

        "learnset": {
            7: "PECK",
            11: "GUST",
            15: "QUICK ATTACK",
        }
    },

    "PIDGEOTTO": {
        "type": "NORMAL / FLYING",
        "hp": 75,
        "attack": 82,
        "defense": 70,
        "speed": 85,
        "base_exp": 140,

        "moves": [
            "TACKLE",
            "PECK",
            "GUST",
            "QUICK ATTACK",
        ],

        "learnset": {
            18: "AERIAL ACE",
        }
    },

    "SPEAROW": {
        "type": "NORMAL / FLYING",
        "hp": 40,
        "attack": 60,
        "defense": 40,
        "speed": 70,
        "base_exp": 60,

        "moves": [
            "PECK",
        ],

        "learnset": {
            7: "GUST",
            11: "FURY ATTACK",
            15: "QUICK ATTACK",
        }
    },

    "FEAROW": {
        "type": "NORMAL / FLYING",
        "hp": 65,
        "attack": 100,
        "defense": 73,
        "speed": 100,
        "base_exp": 140,

        "moves": [
            "PECK",
            "GUST",
            "FURY ATTACK",
            "QUICK ATTACK",
        ],

        "learnset": {
            18: "AERIAL ACE",
        }
    },

    "MANKEY": {
        "type": "FIGHT",
        "hp": 40,
        "attack": 70,
        "defense": 40,
        "speed": 70,
        "base_exp": 60,

        "moves": [
            "SCRATCH",
        ],

        "learnset": {
            6: "LOW KICK",
            10: "DOUBLE KICK",
            14: "KARATE CHOP",
            18: "QUICK ATTACK",
        }
    },

    "CATERPIE": {
        "type": "BUG",
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
        "type": "BUG",
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
        "type": "BUG / FLYING",
        "hp": 60,
        "attack": 55,
        "defense": 65,
        "speed": 72,
        "base_exp": 140,

        "moves": [
            "CONFUSION",
        ],

        "learnset": {
            10: "CONFUSION",
            12: "GUST",
            16: "AERIAL ACE",
            18: "PSYBEAM",
        }
    },

    "WEEDLE": {
        "type": "BUG / POISON",
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
        "type": "BUG / POISON",
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
        "type": "BUG / POISON",
        "hp": 70,
        "attack": 80,
        "defense": 55,
        "speed": 85,
        "base_exp": 140,

        "moves": [
            "POISON STING",
        ],

        "learnset": {
            10: "FURY ATTACK",
            13: "FURY CUTTER",
            17: "AERIAL ACE",
        }
    },

    "GEODUDE": {
        "type": "ROCK / GROUND",
        "hp": 40,
        "attack": 80,
        "defense": 100,
        "speed": 20,
        "base_exp": 70,

        "moves": [
            "TACKLE",
        ]
    },

    "SANDSHREW": {
        "type": "GROUND",
        "hp": 50,
        "attack": 70,
        "defense": 80,
        "speed": 40,
        "base_exp": 60,

        "moves": [
            "SCRATCH",
            "POISON STING",
        ]
    },

    "ONIX": {
        "type": "ROCK / GROUND",
        "hp": 80,
        "attack": 70,
        "defense": 90,
        "speed": 40,
        "base_exp": 150,

        "moves": [
            "TACKLE",
            "ROCK TOMB",
            "BIND",
        ]
    },

}

moves = {

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

    "BIND": {
        "power": 15,
        "accuracy": 75,
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
    
    "AERIAL ACE": {
        "power": 60,
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
    
    "PSYBEAM": {
        "power": 65,
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

    "FURY CUTTER": {
        "power": 40,
        "accuracy": 95,
        "type": "BUG"
    },

    "ROCK TOMB": {
        "power": 50,
        "accuracy": 80,
        "type": "ROCK"
    },

}

class Pokemon:
    def __init__(self, name, level):
        self.name = name

        if level > MAX_LEVEL:
            level = MAX_LEVEL

        if level < 1:
            level = 1

        self.level = level
        self.experience = 0

        self.type = pokedex[name]["type"]
        self.base_hp = pokedex[name]["hp"]
        self.base_attack = pokedex[name]["attack"]
        self.base_defense = pokedex[name]["defense"]
        self.base_speed = pokedex[name]["speed"]
        self.base_exp = pokedex[name]["base_exp"]
        self.moves = pokedex[name]["moves"].copy()
        self.learnset = pokedex[name].get("learnset", {})

        self.calculate_stats()
        self.load_moves()
        self.heal_full()

    def calculate_stats(self):
        self.max_hp = int(((self.base_hp * 2) * self.level) / 100) + self.level + 10
        self.attack = int(((self.base_attack * 2) * self.level) / 100) + 5
        self.defense = int(((self.base_defense * 2) * self.level) / 100) + 5
        self.speed = int(((self.base_speed * 2) * self.level) / 100) + 5

    def load_moves(self):
        for level, move in self.learnset.items():
            if self.level >= level and move not in self.moves:
                if len(self.moves) < MAX_MOVES:
                    self.moves.append(move)

    def exp_next_level(self):
        required_experience = self.level * 10

        return required_experience

    def gain_experience(self, experience_gained):
        self.experience = self.experience + experience_gained

        print(f"{self.name} ganhou {experience_gained} de EXP.!")

        while self.experience >= self.exp_next_level() and self.level < MAX_LEVEL:
            required_experience = self.exp_next_level()

            self.level = self.level + 1

            print(f"\n{self.name} upou para o Lv{self.level}!")

            exceeded_exp = self.experience - required_experience
            self.experience = exceeded_exp

            self.calculate_stats()
            self.heal_full()
            self.learn_move()

    def learn_move(self):
        if self.level in self.learnset:
            new_move = self.learnset[self.level]

            if new_move in self.moves:
                return

            if len(self.moves) < MAX_MOVES:
                self.moves.append(new_move)
                print(f"\n{self.name} aprendeu {new_move}!")
                dialogue.next_dialogue()
                return

            print(f"\n{self.name} quer aprender {new_move}!")
            dialogue.next_dialogue()

            while True:
                dialogue.clear_screen()

                print(f"\nMas {self.name} já conhece 4 golpes.")
                print("\nEscolha um golpe para esquecer:\n")

                for i, move in enumerate(self.moves, start=1):
                    move_type = moves[move]["type"]

                    print(f"{i} - {move} ({move_type})")

                print(f"0 - Não aprender {new_move}")

                choice = input("\nEscolha: ")

                if not choice.isdigit():
                    dialogue.clear_screen()
                    print("\n[ Opcao invalida! Tente novamente. ]")
                    dialogue.next_dialogue()
                    continue

                choice = int(choice)

                if choice == 0:
                    dialogue.clear_screen()
                    print(f"\n{self.name} não aprendeu {new_move}!")
                    dialogue.next_dialogue()
                    return

                elif 1 <= choice <= len(self.moves):
                    forgotten_move = self.moves[choice - 1]
                    self.moves[choice - 1] = new_move

                    dialogue.clear_screen()
                    print(f"\n{self.name} esqueceu {forgotten_move}!")
                    print(f"\n{self.name} aprendeu {new_move}!")
                    dialogue.next_dialogue()
                    return

                else:
                    dialogue.clear_screen()
                    print("\n[ Opcao invalida! Tente novamente. ]")
                    dialogue.next_dialogue()

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