import dialogue

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




def choose_starter():
    print("\n--- STARTER POKEMON ---")
    print("1 - Bulbasaur")
    print("2 - Squirtle")
    print("3 - Charmander")

    while True:
        choice = input("\nChoose: ")

        if choice == "1":
            starter = Pokemon("BULBASAUR", 5)
            dialogue.narration("\nYou chose Bulbasaur!")
            dialogue.next_dialogue()
            return starter

        elif choice == "2":
            starter = Pokemon("SQUIRTLE", 5)
            dialogue.narration("\nYou chose Squirtle!")
            dialogue.next_dialogue()
            return starter

        elif choice == "3":
            starter = Pokemon("CHARMANDER", 5)
            dialogue.narration("\nYou chose Charmander!")
            dialogue.next_dialogue()
            return starter

        elif choice == "4":
            starter = Pokemon("PIKACHU", 5)
            dialogue.narration("\nWait... a fourth Pokeball?")
            dialogue.narration("\nYou chose Pikachu!")
            dialogue.next_dialogue()
            return starter

        else:
            dialogue.narration("\n[Invalid option! Please select again.]")
            dialogue.next_dialogue()
            print("\n--- STARTER POKEMON ---")
            print("1 - Bulbasaur")
            print("2 - Squirtle")
            print("3 - Charmander")

            
