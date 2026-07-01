# 🎮 Pokémon Text-Based RPG

A classic text-based Pokémon RPG built from scratch in Python, inspired by the retro Game Boy Pokémon games.

This project focuses on learning Python fundamentals, object-oriented programming, modular architecture, and game logic development through a fully terminal-based RPG experience.

---

## 🚀 Features

### ✅ Implemented Mechanics

* **Game Loop & Main Menu**

  * Functional start menu with navigation options.
  * Title screen return flow from the in-game player menu.

* **Dynamic Dialogue Engine**

  * Typewriter-style text animation.
  * Integrated screen-clearing system for cleaner gameplay flow.
  * Reusable dialogue, narration, input, and pause functions.

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
  * Base experience values assigned to Pokémon species.
  * Level-based move learnsets assigned to Pokémon species.
  * Pokémon move list integration.

* **Pokémon System (OOP)**

  * Object-oriented Pokémon creation system.
  * Dynamic stat calculation based on level.
  * Experience and level up system implemented.
  * Level-based move learning system implemented.
  * Full HP recovery on level up implemented as a gameplay mechanic.
  * Individual move sets assigned to each Pokémon.
  * Pokémon status display through the player menu.

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
  * Experience gain after winning battles.
  * Trainer battle experience bonus implemented.
  * Battle interface with dynamic HP display.

* **Basic Player Menu System**

  * Added a dedicated `menu.py` module.
  * Added a reusable player menu accessible from routes and cities.
  * Added Pokémon status option.
  * Connected Bag option to the `items.py` module.
  * Connected Save option to the `save.py` module.
  * Added Exit confirmation flow.
  * Added return-to-title-screen behavior from the in-game menu.
  * Added Back option to return to the current area.

* **Basic Route Exploration System**

  * Added Route 1 exploration after the first rival battle.
  * Implemented walking progress toward Viridian City.
  * Added basic tall grass wild encounters with random Route 1 Pokémon.
  * Added random wild Pokémon levels for Route 1 encounters.
  * Added defeat handling that heals the player's Pokémon and resets Route 1 progress.
  * Added basic Viridian City hub after Route 1.
  * Added basic Pokémon Center healing system.
  * Added option to return from Viridian City to Route 1.
  * Added basic Route 2 exploration after Viridian City.
  * Added Route 2 wild encounters with weighted Pokémon selection.
  * Added basic Viridian Forest exploration after Route 2.
  * Added Viridian Forest wild encounters with Caterpie, Weedle, and rare Pikachu.
  * Added defeat handling that returns the player to Viridian City from Route 2 and Viridian Forest.
  * Added player menu access across map areas.
  * Added basic Route 3 exploration after Viridian Forest.
  * Added Route 3 wild encounters with weighted Pokémon selection.
  * Added option to return from Route 3 to Viridian Forest.
  * Added basic Pewter City hub after Route 3.
  * Added Pewter City Pokémon Center access.
  * Added option to return from Pewter City to Route 3.
  * Added locked Pewter Gym placeholder.

---

## 🛣️ Future Roadmap

* [ ] Pokémon switching system
* [ ] Bag system
* [ ] Type effectiveness system
* [ ] Accuracy and critical hit system
* [x] Experience and leveling system
* [x] Move learning system
* [ ] Four-move limit and move replacement system
* [x] Basic wild Pokémon encounter system
* [x] Expanded wild encounter tables by route
* [ ] More route-specific encounter balancing
* [ ] Pokémon catching mechanics
* [ ] Party and PC storage system
* [ ] Status effects and healing items
* [ ] Trainer battles
* [x] Basic player menu system
* [x] Basic Pewter City hub
* [ ] Gym Leader Brock
* [ ] Save and load system
* [x] Exit confirmation system

---

## 🛠️ Tech Stack

* **Language:** Python 3.12
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
├── menu.py
├── items.py
├── trainer.py
├── save.py
└── README.md
```

---

## 📦 How to Run the Project

1. Ensure Python 3.12 or newer is installed on your machine.

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

On Windows, you can also use:

```bash
py main.py
```

---

## 🎯 Project Goals

This project is currently in early gameplay development phase, focusing on core battle mechanics, route exploration, menu structure, and system architecture.

* Learning Python from scratch
* Practicing programming logic
* Understanding object-oriented programming
* Improving code organization and modularization
* Practicing Git and GitHub workflows
* Building a portfolio project for future internship opportunities
