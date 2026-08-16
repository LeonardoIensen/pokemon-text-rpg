class Trainer:
    def __init__(self, name, pokemon):
        self.name = name
        self.party = [pokemon]

    def add_pokemon(self, pokemon):
        self.party.append(pokemon)

    def show_party(self):
        print("--- PARTY ---\n")
        for i, pokemon in enumerate(self.party, start=1):
            print(f"{i} - {pokemon.name}")
