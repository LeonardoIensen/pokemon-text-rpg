import pokemon
import dialogue

class Trainer:
    def __init__(self, name, pokemon, ):
        self.name = name
        self.party = [pokemon]
        self.pc_box = []
        self.defeated = False
        self.pewter_gym_defeated = False

    def add_pokemon(self, pokemon):
        if 3 > len(self.party):
            self.party.append(pokemon)

        else:
            dialogue.clear_screen()
            print(f"Party cheia! {pokemon.name} foi tranferido para o PC!")
            dialogue.next_dialogue()

            self.pc_box.append(pokemon)

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
