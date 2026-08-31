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
  * Sistema de experiência (EXP)
  * Ganho de experiência
  * Level up automático
  * Level up múltiplo quando há EXP suficiente
  * Manutenção da EXP excedente após subir de nível
  * Cálculo de HP, Attack, Defense e Speed baseado nos stats-base e nível
  * Sistema de HP atual e HP máximo
  * Recuperação completa do HP ao subir de nível
  * Sistema de golpes
  * Pokémon possuem golpes disponíveis para batalha

* **Sistema de Treinador**

  * Classe `Trainer` para criação dos treinadores
  * Sistema de party para armazenar os Pokémon do treinador
  * Adição de Pokémon à party
  * Exibição dos Pokémon da party
  * Jogador e rival começam com seus Pokémon iniciais

* **Sistema de batalha**
  * Menu principal de batalha
  * Menu de Pokémon para visualizar a equipe da party
  * Tela de sumário com estatísticas completas, HP, XP e golpes do Pokémon
  * Exibição dos status, HP e XP atual/necessária dos Pokémon
  * Menu de golpes
  * Escolha de golpes pelo jogador
  * Cálculo de dano
  * Precisão dos golpes baseada na accuracy
  * Golpes podem errar e causar 0 de dano
  * Redução de HP
  * Sistema de velocidade para definir a ordem dos ataques
  * Sorteio da ordem de ataque quando os Pokémon possuem a mesma Speed
  * Turno do inimigo
  * Escolha aleatória do golpe do inimigo
  * Sistema de vitória e derrota
  * Ganho de experiência (EXP) e level up automático pós-vitória
  * Retorno ao menu de batalha após cada turno
  * Batalhas contra Pokémon selvagens
  * Sistema de fuga de batalhas
  * Fuga bloqueada contra treinadores
  * Chance de 90% de fuga contra Pokémon selvagens
  * Pokémon selvagem ataca após uma tentativa de fuga malsucedida

* **Mapa e Exploração**
  * Rota 1 com sistema de passos
  * Navegação entre opções de andar, grama alta e menu
  * Sistema de encontros selvagens com chance percentual melhorada
  * Sorteio aleatório do nível dos Pokémon selvagens dentro do intervalo da rota
  * Sistema de derrota com retorno para casa e recuperação de toda a equipe
  * Chegada em Viridian City ao completar os passos
  * Centro Pokémon em Viridian City para recuperação da equipe
  * Rota 2 com novos Pokémon selvagens (Spearow e Mankey)
  * Bosque de Viridian com contagem de passos e encontros selvagens
  * Rota 3 com caminho até a entrada de Pewter City
  * Cadeia de retornos e cura automática em Viridian City após desmaiar em áreas avançadas
  * Cidade de Pewter com acesso ao Centro Pokémon e opção de retorno à Rota 3
  * Menu do jogador acessível em todas as rotas e cidades para visualizar a party fora das batalhas

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
├── battle.py
├── map.py
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
