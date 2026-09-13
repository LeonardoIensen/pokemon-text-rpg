import json
import os
import pokemon
import trainer


def has_save_file():
    return os.path.exists("savegame.json")


def pokemon_to_dict(poke):
    return {
        "name": poke.name,
        "level": poke.level,
        "current_hp": poke.current_hp,
        "max_hp": poke.max_hp,
        "experience": poke.experience,
        "moves": poke.moves
    }


def dict_to_pokemon(data):
    poke = pokemon.Pokemon(data["name"], data["level"])
    poke.current_hp = data["current_hp"]
    poke.max_hp = data["max_hp"]
    poke.experience = data["experience"]
    poke.moves = data["moves"]
    return poke


def save_game(player, rival, location="route_1", steps=0):
    player_party_data = []
    for p in player.party:
        player_party_data.append(pokemon_to_dict(p))

    player_pc_data = []
    for p in player.pc_box:
        player_pc_data.append(pokemon_to_dict(p))

    rival_party_data = []
    for p in rival.party:
        rival_party_data.append(pokemon_to_dict(p))

    route_1_data = {}
    for k, v in trainer.route_1_trainers.items():
        route_1_data[k] = v["defeated"]

    route_2_data = {}
    for k, v in trainer.route_2_trainers.items():
        route_2_data[k] = v["defeated"]

    viridian_forest_data = {}
    for k, v in trainer.viridian_forest_trainers.items():
        viridian_forest_data[k] = v["defeated"]

    route_3_data = {}
    for k, v in trainer.route_3_trainers.items():
        route_3_data[k] = v["defeated"]

    save_data = {
        "location": location,
        "steps": steps,
        "player": {
            "name": player.name,
            "party": player_party_data,
            "pc_box": player_pc_data,
            "pewter_gym_defeated": getattr(player, "pewter_gym_defeated", False)
        },
        "rival": {
            "name": rival.name,
            "party": rival_party_data,
            "defeated": getattr(rival, "defeated", False)
        },
        "trainers": {
            "route_1": route_1_data,
            "route_2": route_2_data,
            "viridian_forest": viridian_forest_data,
            "route_3": route_3_data
        }
    }

    with open("savegame.json", "w") as file:
        json.dump(save_data, file, indent=4)


def load_game():
    if not has_save_file():
        return None, None, "route_1", 0

    with open("savegame.json", "r") as file:
        save_data = json.load(file)

    location = save_data.get("location", "route_1")
    steps = save_data.get("steps", 0)

    player_data = save_data["player"]
    first_poke = dict_to_pokemon(player_data["party"][0])
    player = trainer.Trainer(player_data["name"], first_poke)

    player.party = []
    for p_data in player_data["party"]:
        player.party.append(dict_to_pokemon(p_data))

    player.pc_box = []
    for p_data in player_data["pc_box"]:
        player.pc_box.append(dict_to_pokemon(p_data))

    player.pewter_gym_defeated = player_data.get("pewter_gym_defeated", False)

    rival_data = save_data["rival"]
    rival_first_poke = dict_to_pokemon(rival_data["party"][0])
    rival = trainer.Trainer(rival_data["name"], rival_first_poke)

    rival.party = []
    for p_data in rival_data["party"]:
        rival.party.append(dict_to_pokemon(p_data))

    rival.defeated = rival_data.get("defeated", False)

    trainers_data = save_data.get("trainers", {})

    for k, v in trainers_data.get("route_1", {}).items():
        if k in trainer.route_1_trainers:
            trainer.route_1_trainers[k]["defeated"] = v

    for k, v in trainers_data.get("route_2", {}).items():
        if k in trainer.route_2_trainers:
            trainer.route_2_trainers[k]["defeated"] = v

    for k, v in trainers_data.get("viridian_forest", {}).items():
        if k in trainer.viridian_forest_trainers:
            trainer.viridian_forest_trainers[k]["defeated"] = v

    for k, v in trainers_data.get("route_3", {}).items():
        if k in trainer.route_3_trainers:
            trainer.route_3_trainers[k]["defeated"] = v

    return player, rival, location, steps