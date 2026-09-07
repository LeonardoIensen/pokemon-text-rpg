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
        "base_exp": 60,

        "moves": [
            "SCRATCH",
            "GROWL",
        ],

        "learnset": {
            7: "EMBER",
            11: "TAIL WHIP",
            13: "METAL CLAW",
            16: "FLAME WHEEL",
        },

        "evolution": {
            "level": 16,
            "pokemon": "CHARMELEON"
        }
    },

    "CHARMELEON": {
        "type": "FIRE",
        "hp": 70,
        "attack": 80,
        "defense": 70,
        "speed": 90,
        "base_exp": 100,

        "moves": [
            "SCRATCH",
            "GROWL",
            "EMBER",
            "TAIL WHIP",
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
        "base_exp": 60,

        "moves": [
            "TACKLE",
            "GROWL",
        ],

        "learnset": {
            7: "VINE WHIP",
            11: "TAIL WHIP",
            13: "SLAM",
            16: "RAZOR LEAF",
        },

        "evolution": {
            "level": 16,
            "pokemon": "IVYSAUR"
        }
    },

    "IVYSAUR": {
        "type": "GRASS / POISON",
        "hp": 70,
        "attack": 70,
        "defense": 70,
        "speed": 80,
        "base_exp": 100,

        "moves": [
            "TACKLE",
            "GROWL",
            "VINE WHIP",
            "TAIL WHIP",
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
        "base_exp": 60,

        "moves": [
            "TACKLE",
            "TAIL WHIP",
        ],

        "learnset": {
            7: "BUBBLE",
            10: "HARDEN",
            13: "WATER GUN",
            16: "BITE",
        },

        "evolution": {
            "level": 16,
            "pokemon": "WARTORTLE"
        }
    },

    "WARTORTLE": {
        "type": "WATER",
        "hp": 80,
        "attack": 70,
        "defense": 80,
        "speed": 70,
        "base_exp": 100,

        "moves": [
            "TACKLE",
            "TAIL WHIP",
            "BUBBLE",
            "HARDEN",
        ],

        "learnset": {
            18: "WATER PULSE",
        }
    },

    "PIKACHU": {
        "type": "ELECTRIC",
        "hp": 50,
        "attack": 70,
        "defense": 40,
        "speed": 90,
        "base_exp": 50,

        "moves": [
            "THUNDER SHOCK",
            "GROWL",
        ],

        "learnset": {
            6: "TAIL WHIP",
            9: "QUICK ATTACK",
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
        "base_exp": 50,

        "moves": [
            "TACKLE",
            "TAIL WHIP",
        ],

        "learnset": {
            7: "QUICK ATTACK",
            10: "GROWL",
            12: "HYPER FANG",
            16: "SLAM",
        },

        "evolution": {
            "level": 18,
            "pokemon": "RATICATE"
        }
    },

    "RATICATE": {
        "type": "NORMAL",
        "hp": 60,
        "attack": 80,
        "defense": 70,
        "speed": 90,
        "base_exp": 100,

        "moves": [
            "TACKLE",
            "TAIL WHIP",
            "QUICK ATTACK",
            "GROWL",
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
        "base_exp": 50,

        "moves": [
            "TACKLE",
            "GROWL",
        ],

        "learnset": {
            7: "PECK",
            11: "GUST",
            13: "TAIL WHIP",
            15: "QUICK ATTACK",
        },

        "evolution": {
            "level": 18,
            "pokemon": "PIDGEOTTO"
        }
    },

    "PIDGEOTTO": {
        "type": "NORMAL / FLYING",
        "hp": 60,
        "attack": 80,
        "defense": 70,
        "speed": 90,
        "base_exp": 100,

        "moves": [
            "TACKLE",
            "GROWL",
            "PECK",
            "TAIL WHIP",
        ],

        "learnset": {
            20: "AERIAL ACE",
        }
    },

    "SPEAROW": {
        "type": "NORMAL / FLYING",
        "hp": 40,
        "attack": 60,
        "defense": 40,
        "speed": 70,
        "base_exp": 50,

        "moves": [
            "PECK",
            "GROWL",
        ],

        "learnset": {
            9: "GUST",
            12: "TAIL WHIP",
            15: "FURY ATTACK",
            17: "QUICK ATTACK",
        },

        "evolution": {
            "level": 18,
            "pokemon": "FEAROW"
        }
    },

    "FEAROW": {
        "type": "NORMAL / FLYING",
        "hp": 60,
        "attack": 80,
        "defense": 70,
        "speed": 90,
        "base_exp": 100,

        "moves": [
            "PECK",
            "GROWL",
            "GUST",
            "TAIL WHIP",
        ],

        "learnset": {
            20: "AERIAL ACE",
        }
    },

    "MANKEY": {
        "type": "FIGHT",
        "hp": 40,
        "attack": 70,
        "defense": 40,
        "speed": 70,
        "base_exp": 50,

        "moves": [
            "SCRATCH",
            "TAIL WHIP",
        ],

        "learnset": {
            6: "LOW KICK",
            9: "GROWL",
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
        "base_exp": 40,

        "moves": [
            "TACKLE",
            "STRING SHOT",
        ],

        "learnset": {
            5: "HARDEN",
        },

        "evolution": {
            "level": 7,
            "pokemon": "METAPOD"
        }
    },

    "METAPOD": {
        "type": "BUG",
        "hp": 50,
        "attack": 30,
        "defense": 70,
        "speed": 30,
        "base_exp": 60,

        "moves": [
            "HARDEN",
            "STRING SHOT",
        ],

        "evolution": {
            "level": 10,
            "pokemon": "BUTTERFREE"
        }
    },

    "BUTTERFREE": {
        "type": "BUG / FLYING",
        "hp": 60,
        "attack": 70,
        "defense": 70,
        "speed": 90,
        "base_exp": 100,

        "moves": [
            "CONFUSION",
            "HARDEN",
            "STRING SHOT",
        ],

        "learnset": {
            10: "CONFUSION",
            12: "GUST",
            14: "TAIL WHIP",
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
        "base_exp": 50,

        "moves": [
            "POISON STING",
            "STRING SHOT",
        ],

        "learnset": {
            5: "HARDEN",
        },

        "evolution": {
            "level": 7,
            "pokemon": "KAKUNA"
        }
    },

    "KAKUNA": {
        "type": "BUG / POISON",
        "hp": 50,
        "attack": 30,
        "defense": 70,
        "speed": 30,
        "base_exp": 60,

        "moves": [
            "HARDEN",
            "STRING SHOT",
        ],

        "evolution": {
            "level": 10,
            "pokemon": "BEEDRILL"
        }
    },

    "BEEDRILL": {
        "type": "BUG / POISON",
        "hp": 70,
        "attack": 80,
        "defense": 70,
        "speed": 90,
        "base_exp": 100,

        "moves": [
            "POISON STING",
            "HARDEN",
            "STRING SHOT",
        ],

        "learnset": {
            10: "FURY ATTACK",
            13: "FURY CUTTER",
            15: "TAIL WHIP",
            17: "AERIAL ACE",
        }
    },

    "GEODUDE": {
        "type": "ROCK / GROUND",
        "hp": 70,
        "attack": 60,
        "defense": 90,
        "speed": 30,
        "base_exp": 60,

        "moves": [
            "TACKLE",
            "HARDEN",
        ],

        "learnset": {
            8: "TAIL WHIP",
            11: "ROCK TOMB",
        }
    },

    "SANDSHREW": {
        "type": "GROUND",
        "hp": 60,
        "attack": 70,
        "defense": 80,
        "speed": 40,
        "base_exp": 60,

        "moves": [
            "SCRATCH",
            "HARDEN",
        ],

        "learnset": {
            6: "POISON STING",
            9: "TAIL WHIP",
            12: "SLASH",
        }
    },

    "ONIX": {
        "type": "ROCK / GROUND",
        "hp": 80,
        "attack": 70,
        "defense": 100,
        "speed": 30,
        "base_exp": 120,

        "moves": [
            "TACKLE",
            "HARDEN",
            "BIND",
        ],

        "learnset": {
            8: "TAIL WHIP",
            11: "ROCK TOMB",
        }
    },

}

moves = {

    "SCRATCH": {
        "power": 40,
        "accuracy": 100,
        "type": "NORMAL",
        "category": "DAMAGE"
    },

    "TACKLE": {
        "power": 35,
        "accuracy": 95,
        "type": "NORMAL",
        "category": "DAMAGE"
    },

    "FURY ATTACK": {
        "power": 15,
        "accuracy": 90,
        "type": "NORMAL",
        "category": "DAMAGE"
    },

    "SLASH": {
        "power": 70,
        "accuracy": 95,
        "type": "NORMAL",
        "category": "DAMAGE"
    },

    "QUICK ATTACK": {
        "power": 40,
        "accuracy": 100,
        "type": "NORMAL",
        "category": "DAMAGE"
    },

    "HYPER FANG": {
        "power": 80,
        "accuracy": 90,
        "type": "NORMAL",
        "category": "DAMAGE"
    },

    "SLAM": {
        "power": 60,
        "accuracy": 85,
        "type": "NORMAL",
        "category": "DAMAGE"
    },

    "EMBER": {
        "power": 40,
        "accuracy": 100,
        "type": "FIRE",
        "category": "DAMAGE"
    },

    "FLAME WHEEL": {
        "power": 60,
        "accuracy": 100,
        "type": "FIRE",
        "category": "DAMAGE"
    },

    "FLAMETHROWER": {
        "power": 95,
        "accuracy": 100,
        "type": "FIRE",
        "category": "DAMAGE"
    },

    "VINE WHIP": {
        "power": 35,
        "accuracy": 95,
        "type": "GRASS",
        "category": "DAMAGE"
    },

    "RAZOR LEAF": {
        "power": 55,
        "accuracy": 95,
        "type": "GRASS",
        "category": "DAMAGE"
    },

    "GIGA DRAIN": {
        "power": 60,
        "accuracy": 100,
        "type": "GRASS",
        "category": "DAMAGE"
    },

    "BUBBLE": {
        "power": 30,
        "accuracy": 100,
        "type": "WATER",
        "category": "DAMAGE"
    },

    "WATER GUN": {
        "power": 40,
        "accuracy": 100,
        "type": "WATER",
        "category": "DAMAGE"
    },

    "WATER PULSE": {
        "power": 60,
        "accuracy": 100,
        "type": "WATER",
        "category": "DAMAGE"
    },

    "BITE": {
        "power": 60,
        "accuracy": 100,
        "type": "DARK",
        "category": "DAMAGE"
    },

    "THUNDER SHOCK": {
        "power": 40,
        "accuracy": 100,
        "type": "ELECTRIC",
        "category": "DAMAGE"
    },

    "THUNDERBOLT": {
        "power": 95,
        "accuracy": 100,
        "type": "ELECTRIC",
        "category": "DAMAGE"
    },

    "PECK": {
        "power": 35,
        "accuracy": 95,
        "type": "FLYING",
        "category": "DAMAGE"
    },

    "GUST": {
        "power": 40,
        "accuracy": 100,
        "type": "FLYING",
        "category": "DAMAGE"
    },

    "AERIAL ACE": {
        "power": 60,
        "accuracy": 100,
        "type": "FLYING",
        "category": "DAMAGE"
    },

    "CONFUSION": {
        "power": 50,
        "accuracy": 100,
        "type": "PSYCHIC",
        "category": "DAMAGE"
    },

    "PSYBEAM": {
        "power": 65,
        "accuracy": 100,
        "type": "PSYCHIC",
        "category": "DAMAGE"
    },

    "METAL CLAW": {
        "power": 50,
        "accuracy": 95,
        "type": "STEEL",
        "category": "DAMAGE"
    },

    "DOUBLE KICK": {
        "power": 30,
        "accuracy": 100,
        "type": "FIGHT",
        "category": "DAMAGE"
    },

    "LOW KICK": {
        "power": 30,
        "accuracy": 100,
        "type": "FIGHT",
        "category": "DAMAGE"
    },

    "KARATE CHOP": {
        "power": 50,
        "accuracy": 100,
        "type": "FIGHT",
        "category": "DAMAGE"
    },

    "FURY CUTTER": {
        "power": 40,
        "accuracy": 95,
        "type": "BUG",
        "category": "DAMAGE"
    },

    "ROCK TOMB": {
        "power": 50,
        "accuracy": 80,
        "type": "ROCK",
        "category": "DAMAGE"
    },

    "BIND": {
        "power": 15,
        "accuracy": 75,
        "type": "NORMAL",
        "category": "DAMAGE"
    },

    "POISON STING": {
        "power": 15,
        "accuracy": 100,
        "type": "POISON",
        "category": "DAMAGE"
    },

    "HARDEN": {
        "power": 0,
        "accuracy": 100,
        "type": "NORMAL",
        "category": "STATUS",
        "stat": "defense",
        "change": 1,
        "target": "user"
    },

    "GROWL": {
        "power": 0,
        "accuracy": 100,
        "type": "NORMAL",
        "category": "STATUS",
        "stat": "attack",
        "change": -1,
        "target": "opponent"
    },

    "TAIL WHIP": {
        "power": 0,
        "accuracy": 100,
        "type": "NORMAL",
        "category": "STATUS",
        "stat": "defense",
        "change": -1,
        "target": "opponent"
    },

    "STRING SHOT": {
        "power": 0,
        "accuracy": 95,
        "type": "BUG",
        "category": "STATUS",
        "stat": "speed",
        "change": -1,
        "target": "opponent"
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
        self.evolution = pokedex[name].get("evolution", {})

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


    def evolve(self):
        if not self.evolution:
            return

        if self.level == self.evolution["level"]:
            new_name = self.evolution["pokemon"]
            old_name = self.name

            dialogue.clear_screen()
            print(f"O que!? {old_name} está evoluindo!\n")
            print(f"{old_name} evoluiu para {new_name}!")
            dialogue.next_dialogue()

            self.name = new_name
            self.type = pokedex[new_name]["type"]
            self.base_hp = pokedex[new_name]["hp"]
            self.base_attack = pokedex[new_name]["attack"]
            self.base_defense = pokedex[new_name]["defense"]
            self.base_speed = pokedex[new_name]["speed"]
            self.base_exp = pokedex[new_name]["base_exp"]
            self.learnset = pokedex[new_name].get("learnset", {})
            self.evolution = pokedex[new_name].get("evolution", {})    

            self.calculate_stats()
            self.heal_full()
            self.learn_move()


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
            self.evolve()


    def learn_move(self):
        if self.level in self.learnset:
            new_move = self.learnset[self.level]

            if new_move in self.moves:
                return

            new_move_data = moves[new_move]

            if len(self.moves) < MAX_MOVES:
                self.moves.append(new_move)
                print(f"\n{self.name} aprendeu {new_move}!")
                dialogue.next_dialogue()
                return

            print(f"\n{self.name} quer aprender {new_move}!")
            dialogue.next_dialogue()

            while True:
                dialogue.clear_screen()

                print(f"Mas {self.name} já conhece {MAX_MOVES} golpes.")
                print("\nEscolha um golpe para esquecer:\n")

                for i, move in enumerate(self.moves, start=1):
                    m_data = moves[move]
                    print(f"{i}- {move:<14} TYPE: {m_data['type']:<8} POWER: {m_data['power']:<3} ACC: {m_data['accuracy']}")

                print(f"\n0- Não aprender {new_move} (TYPE: {new_move_data['type']} | POWER: {new_move_data['power']} | ACC: {new_move_data['accuracy']})")

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
        self.calculate_stats()
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