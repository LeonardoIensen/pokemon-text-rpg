import os
import time

def next_dialogue():
    print("\n[Press Enter to continue...]")

    input()

    os.system("cls")

def narration(text):
    for letter in text:
        time.sleep(0.01)
        print(letter, end="", flush=True)

    print()

def talk(character, text):
    print(f"\n{character}: ",end="")
    narration(text)
    next_dialogue()

def ask(character, text):
    print(f"\n{character}: ",end="")
    narration(text)

def intro():
    talk("PROF. OAK", "Hello! It's a pleasure to meet you!")
    talk("PROF. OAK", "Welcome to the fabulous world of Pokémon!")
    talk("PROF. OAK", "My name is OAK. But everyone here calls me PROFESSOR OAK.")
    talk("PROF. OAK", "This world is inhabited by creatures called POKEMON.")
    talk("PROF. OAK", "Some people treat them as pets.")
    talk("PROF. OAK", "Others use them in battles.")
    talk("PROF. OAK", "Well, As for me...")
    talk("PROF. OAK", "I study POKEMON as a profession.")
    talk("PROF. OAK", "But first, tell us a little about yourself.")

    ask("PROF. OAK", "First, what is your name?")

    while True:
        player_name = input("\nYour name: ").strip().upper()

        if 0 < len(player_name) <= 10:
            break
        else:
            narration("\n[Invalid name! It must be between 1 and 10 characters.]")
            next_dialogue()
            ask("PROF. OAK", "First, what is your name?")


    talk("PROF. OAK", f"Right! So your name is {player_name}!")
    talk("PROF. OAK", "Ah, yes... I also have a grandson.")
    talk("PROF. OAK", "He's been your rival since you both were babies.")

    ask("PROF. OAK", "Erm... What was his name now?")

    while True:
        rival_name = input("\nName of the rival: ").strip().upper()

        if 0 < len(rival_name) <= 10:
            break
        else:
             narration("\n[Invalid name! It must be between 1 and 10 characters.]")
             next_dialogue()
             ask("PROF. OAK", "Um... What was his name again?")

    talk("PROF. OAK", f"That's right! I remember now! His name is {rival_name}!")
    talk("PROF. OAK", f"{player_name}! Your own Pokémon legend is about to begin!")
    talk("PROF. OAK", "A world of dreams and adventures awaits you! So, let's go!");

    return player_name, rival_name

def start_journey(player_name, rival_name):
    narration(f"{player_name} wakes up late on the big day to choose their first Pokemon.")

    talk("MOM", "Right... All boys leave home someday. It said so on TV.")
    talk("MOM", "Oh yes. PROF. OAK wants to see you.")

    narration(f"Curious, {player_name} leaves home and walks through the small town of Pallet.")

    talk("PROF. OAK", "Hey! Wait!")

    narration("The older professor quickly approaches.")

    talk("PROF. OAK", "Wild Pokémon live in tall grass!")
    talk("PROF. OAK", "Without a Pokémon, it would be dangerous to go alone.")
    talk("PROF. OAK", "Come with me to my lab.")

    narration(f"{player_name} accompanies PROF. OAK to his lab.")
    narration(f"Upon entering the lab, {player_name} finds {rival_name} waiting impatiently.")

    talk(f"{rival_name}", "Finally arrived!")
    talk(f"{rival_name}", "Gramps! I'm tired of waiting!")
    talk("PROF. OAK", "Be patient...")
    talk("PROF. OAK", "You two will get your own Pokémon today.")
    talk("PROF. OAK", "There are three Pokémon here.")
    talk("PROF. OAK", "They were raised especially for young trainers.")

    narration(f"Choose one of them, {player_name}.")

    print("--- STARTER POKÉMON ---")
    print("\n1 - Bulbasaur")
    print("\n2 - Squirtle")
    print("\n3 - Charmander")

