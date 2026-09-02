import pokemon

class Trainer:
    def __init__(self, name, pokemon, ):
        self.name = name
        self.party = [pokemon]
        self.defeated = False
        self.pewter_gym_defeated = False

    def add_pokemon(self, pokemon):
        self.party.append(pokemon)

    def show_party(self):
        print("--- PARTY ---\n")
        for i, pokemon in enumerate(self.party, start=1):
            print(f"{i} - {pokemon.name}")


def gym_trainer():

    geodude = pokemon.Pokemon("GEODUDE", 10)

    gym_trainer_liam = Trainer("TREINADOR LIAM", geodude)

    sandshrew = pokemon.Pokemon("SANDSHREW", 11)

    gym_trainer_liam.add_pokemon(sandshrew)

    return gym_trainer_liam


def gym_leader_brock():

    geodude = pokemon.Pokemon("GEODUDE", 12)

    gym_leader_brock = Trainer("LÍDER BROCK", geodude)

    onix = pokemon.Pokemon("ONIX", 15)

    gym_leader_brock.add_pokemon(onix)

    return gym_leader_brock
