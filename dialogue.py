import os
import time

def next_dialogue():
    print("\n[Press Enter to continue...]")

    input()

    os.system("cls")

def narration(text):
    for letter in text:
        time.sleep(0.02)
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
        player_name = input("\nName: ").strip().upper()

        if 0 < len(player_name) <= 10:
            break
        else:
            narration("\n[Invalid name! It must be between 1 and 10 characters.]")
            next_dialogue()
            ask("PROF. OAK", "First, what is your name?")


    talk("PROF. OAK", f"Right! So your name is {player_name}!")
        
    return player_name
