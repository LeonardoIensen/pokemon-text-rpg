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


route_1_trainers = {

    "TRAINER_1": {
        "name": "JOVEM JOEY",
        "pokemons": [("RATTATA", 4)],
        "intro": "Ei! Nossos olhares se cruzaram, agora temos que batalhar!",
        "win_msg": "Eu disse que meu Rattata era forte!",
        "lose_msg": "Aww... meu Rattata perdeu!",
        "step": 2,
        "defeated": False
    },

    "TRAINER_2": {
        "name": "LADY MILA",
        "pokemons": [("PIDGEY", 5)],
        "intro": "Ugh! O que você está olhando, esquisitão!?",
        "win_msg": "Seu Pokémon é um fracote! HAHA!",
        "lose_msg": "Droga! Você deu sorte...",
        "step": 5,
        "defeated": False
    },

}

route_2_trainers = {

    "TRAINER_1": {
        "name": "JOVEM ANTONY",
        "pokemons": [("RATTATA", 5), ("MANKEY", 6)],
        "intro": "Treinei hoje, vamos testar nossos Pokemons!",
        "win_msg": "Falei que meu time estava mais forte!",
        "lose_msg": "Incrível... você me surpreendeu!",
        "step": 2,
        "defeated": False
    },

    "TRAINER_2": {
        "name": "CAMPISTA ANYA",
        "pokemons": [("PIDGEY", 6), ("SPEAROW", 7)],
        "intro": "Cuidado! Meus Pokémon pássaros vão te pegar de surpresa!",
        "win_msg": "Ninguém supera a velocidade das minhas aves!",
        "lose_msg": "Ah não! As asas dos meus Pokémon cansaram...",
        "step": 5,
        "defeated": False
    },

}

viridian_forest_trainers = {

    "TRAINER_1": {
        "name": "CAÇA INSETOS RICK",
        "pokemons": [("WEEDLE", 6), ("KAKUNA", 8)],
        "intro": "Você não vai passar do Bosque sem enfrentar meus insetos!",
        "win_msg": "A Picada Venenosa do meu Weedle é imbatível!",
        "lose_msg": "Argh! Preciso evoluir meus Pokémon logo...",
        "step": 2,
        "defeated": False
    },

    "TRAINER_2": {
        "name": "CAÇA INSETOS ANDREW",
        "pokemons": [("CATERPIE", 6), ("METAPOD", 8)],
        "intro": "Olhe como a defesa do meu Metapod é resistente!",
        "win_msg": "Nenhum ataque seu conseguiu passar pela nossa defesa!",
        "lose_msg": "Minha tática de endurecer não funcionou...",
        "step": 4,
        "defeated": False
    },

    "TRAINER_3": {
        "name": "CAÇA INSETOS FRANKIE",
        "pokemons": [("METAPOD", 7), ("BUTTERFREE", 10)],
        "intro": "Contemple a beleza da minha Butterfree!",
        "win_msg": "O pó da minha Butterfree acabou com você!",
        "lose_msg": "Minha linda Butterfree... foi derrotada!",
        "step": 6,
        "defeated": False
    },

    "TRAINER_4": {
        "name": "CAÇA INSETOS ARTHUR",
        "pokemons": [("KAKUNA", 7), ("BEEDRILL", 10)],
        "intro": "A saída da floresta é minha! Prepare-se para as ferroadas!",
        "win_msg": "A Beedrill dominou a batalha completamente!",
        "lose_msg": "Você é muito forte... pode seguir para a Rota 3.",
        "step": 8,
        "defeated": False
    },

}

route_3_trainers = {

    "TRAINER_1": {
        "name": "LADY KAMILA",
        "pokemons": [("WEEDLE", 7), ("MANKEY", 10), ("PIKACHU", 8)],
        "intro": "Tenho uma equipe variada e elegante! Acha que pode me vencer?",
        "win_msg": "Como esperado, meus Pokémon são refinados e poderosos!",
        "lose_msg": "Não posso acreditar que perdi aqui tão perto de Pewter!",
        "step": 2,
        "defeated": False
    },

    "TRAINER_2": {
        "name": "JOVEM CARL",
        "pokemons": [("BEEDRILL", 8), ("BUTTERFREE", 10)],
        "intro": "O Ginásio do Brock é logo ali! Vamos ver se você está pronto!",
        "win_msg": "Se não consegue me vencer, nem tente desafiar o Brock!",
        "lose_msg": "Impressionante! Você com certeza tem chance contra o Líder Brock!",
        "step": 5,
        "defeated": False
    },

}