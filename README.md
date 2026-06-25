# 🎮 Pokémon Text-Based RPG

A classic text-based Pokémon RPG built from scratch in Python, inspired by the retro Game Boy Pokémon games.

This project focuses on learning Python fundamentals, object-oriented programming, modular architecture, and game logic development through a fully terminal-based RPG experience.

---

## 🚀 Features

### ✅ Implemented Mechanics

* **Game Loop & Main Menu**

  * Functional start menu with navigation options.

* **Dynamic Dialogue Engine**

  * Typewriter-style text animation.
  * Integrated screen-clearing system for cleaner gameplay flow.

* **Character & Rival Creation**

  * Professor Oak introduction sequence.
  * Player and rival naming system with validation and formatting.

* **Story Prologue**

  * Introductory narrative events fully implemented.
  * Mom dialogue, Oak stopping the player near tall grass, and lab arrival sequence.

* **Starter Pokémon Selection**

  * Choose between Bulbasaur, Squirtle, and Charmander.
  * Hidden Pikachu easter egg option.

* **Pokémon Data System**

  * Structured Pokémon database using dictionaries.
  * Base stats system implementation.
  * Pokémon move list integration.

* **Pokémon System (OOP)**

  * Object-oriented Pokémon creation system.
  * Dynamic stat calculation based on level.
  * Individual move sets assigned to each Pokémon.

* **Move Database System**

  * Dedicated move database using dictionaries.
  * Move power, accuracy, and type data implemented.

* **Rival Starter Logic**

  * Rival automatically chooses a starter based on type advantage.
  * Special random selection behavior when the player chooses Pikachu.

* **First Battle Sequence**

  * Initial rival battle introduction implemented.
  * Classic Pokémon Fire Red-inspired dialogue flow.
  * Functional turn-based battle system.
  * Damage calculation system implemented.
  * Speed-based turn order system implemented.
  * Speed tie resolution with random priority.
  * Run mechanic implemented.
  * Trainer battle escape restriction implemented.
  * Wild battle escape system implemented.
  * Win and lose conditions implemented.
  * Battle interface with dynamic HP display.

* **Basic Route Exploration System**
  * Added Route 1 exploration after the first rival battle.
  * Implemented walking progress toward Viridian City.
  * Added basic tall grass wild encounters with random Route 1 Pokémon.
  * Added random wild Pokémon levels for Route 1 encounters.
  * Added defeat handling that heals the player’s Pokémon and resets Route 1 progress.
  * Added basic Viridian City hub after Route 1.
  * Added basic Pokémon Center healing system.
  * Added option to return from Viridian City to Route 1.
  * Added placeholder options for menu and Route 2 access.

---

## 🛣️ Future Roadmap

* [ ] Pokémon switching system
* [ ] Bag system
* [ ] Type effectiveness system
* [ ] Accuracy and critical hit system
* [ ] Experience and leveling system
* [ ] Move learning system
* [x] Basic wild Pokémon encounter system
* [ ] Expanded wild encounter tables by route
* [ ] Pokémon catching mechanics
* [ ] Party and PC storage system
* [ ] Status effects and healing items
* [ ] Trainer battles and Gym Leader Brock
* [ ] Save and load system

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Built-in Modules:** `os`, `time`, `random`

---

## 📂 Project Structure

```text
pokemon-text-rpg/
│
├── main.py
├── dialogue.py
├── pokemon.py
├── battle.py
├── map.py
├── items.py
├── trainer.py
└── save.py
```

---

## 📦 How to Run the Project

1. Ensure Python 3 is installed on your machine.

2. Clone this repository:

```bash
git clone https://github.com/LeonardoIensen/pokemon-text-rpg.git
```

3. Navigate to the project directory:

```bash
cd pokemon-text-rpg
```

4. Run the game:

```bash
python main.py
```

---

## 🎯 Project Goals

This project is currently in early gameplay development phase, focusing on core battle mechanics and system architecture.

* Learning Python from scratch
* Practicing programming logic
* Understanding object-oriented programming
* Improving code organization and modularization
* Practicing Git and GitHub workflows
* Building a portfolio project for future internship opportunities
