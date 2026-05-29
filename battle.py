import dialogue

def rival_first_battle(
    player_name,
    rival_name,
    player_starter,
    rival_starter
):
    dialogue.talk(f"{rival_name}", f"{player_name}! Let's check out our POKEMON!")
    dialogue.talk(f"{rival_name}", "Come on, I'll take you on!")

    dialogue.narration(f"\n{rival_name} challenges you to a battle!")
    dialogue.next_dialogue()

    dialogue.narration(f"\n{rival_name} sent out {rival_starter.name}!")
    dialogue.next_dialogue()

    dialogue.narration(f"\nGo! {player_starter.name}!")
    dialogue.next_dialogue()