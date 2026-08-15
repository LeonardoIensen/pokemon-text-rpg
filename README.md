# 🎮 Pokémon Text RPG

Um RPG de texto inspirado em Pokémon FireRed, desenvolvido em Python como projeto de estudo.

O projeto tem como objetivo praticar Python, lógica de programação, organização de código e Git/GitHub através do desenvolvimento de um jogo.

---

## 🚧 Status

Em desenvolvimento.

### Funcionalidades implementadas

* **Menu principal**
  * Novo jogo
  * Continuar (ainda não implementado)
  * Sair

* **Introdução**
  * Introdução do Professor Carvalho
  * Criação do nome do jogador
  * Criação do nome do rival
  * Validação dos nomes com limite de 10 caracteres

* **Início da jornada**
  * Saída da casa do jogador
  * Encontro com o Professor Carvalho
  * Ida ao laboratório
  * Introdução à escolha do Pokémon inicial

* **Pokémon inicial**
  * Escolha entre Bulbasaur, Squirtle e Charmander
  * Escolha automática do inicial do rival baseada na vantagem de tipo

* **Sistema de Pokémon**
  * Pokédex com dados-base dos Pokémon
  * Classe `Pokemon` para criação dos Pokémon
  * Sistema de nível
  * Cálculo de HP, Attack, Defense e Speed baseado nos stats-base e nível
  * Sistema de HP atual e HP máximo
  * Recuperação completa do HP

* **Sistema de Treinador**
  * Classe `Trainer` para criação dos treinadores
  * Sistema de party para armazenar os Pokémon do treinador
  * Jogador e rival começam com seus Pokémon iniciais

---

## 🛠️ Tecnologias

* Python 3.12
* Visual Studio Code
* Git / GitHub

---

## 📂 Estrutura do projeto

```text
pokemon-text-rpg/
│
├── main.py
├── dialogue.py
├── pokemon.py
├── trainer.py
└── README.md
```

---

## ▶️ Como executar

No terminal, dentro da pasta do projeto:

```bash
py main.py
```

---

## 🎯 Objetivos do projeto

* Aprender Python de forma prática
* Praticar lógica de programação
* Aprender a organizar um projeto em múltiplos módulos
* Desenvolver um RPG de texto inspirado em Pokémon FireRed
* Praticar Git e GitHub
* Evoluir gradualmente os conhecimentos de Python e programação orientada a objetos
