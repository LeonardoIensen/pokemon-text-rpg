import os

def clear_screen():
    os.system("cls")

def next_dialogue():
    print("\n[Pressione ENTER para continuar...]")

    input()

    os.system("cls")

def talk(character, text):
    print(f"{character}: {text}")
    next_dialogue()

def intro():
    talk("PROF. OAK", "Olá! É um prazer conhecê-lo! Bem-vindo ao fabuloso mundo dos Pokémon!") 
    talk("PROF. OAK", "Meu nome é OAK. Mas todos aqui me chamam de PROFESSOR OAK.") 
    talk("PROF. OAK", "Este mundo é habitado por criaturas chamadas POKEMON.") 
    talk("PROF. OAK", "Algumas pessoas os tratam como animais de estimação, outras os usam em batalhas.") 
    talk("PROF. OAK", "Bem, quanto a mim... eu estudo POKEMON como profissão.") 
    talk("PROF. OAK", "Mas primeiro, conte-nos um pouco sobre você.")

    print("PROF. OAK: Primeiro, qual é o seu nome?")

    while True:
        player_name = input("\nDigite seu nome: ")

        if 0 < len(player_name) <= 10:
            break

        else:
            clear_screen()
            print("[ Nome invalido! Digite um nome entre 1-10 caracteres. ]")
            next_dialogue()
            print("PROF. OAK: Primeiro, qual é o seu nome?")

    clear_screen()
    talk("PROF. OAK", f"Certo! Então seu nome é {player_name}!") 
    talk("PROF. OAK", "Ah, sim... eu também tenho um neto. Ele é seu rival desde que vocês dois eram bebês.") 

    print("PROF. OAK: Erm... Qual era o nome dele agora?")

    while True:
            rival_name = input("\nDigite o nome do rival: ")
    
            if 0 < len(rival_name) <= 10:
                break
    
            else:
                clear_screen()
                print("[ Nome invalido! Digite um nome entre 1-10 caracteres. ]")
                next_dialogue()
                print("PROF. OAK: Erm... Qual era mesmo o nome dele?")

    clear_screen()
    talk("PROF. OAK", f"Isso mesmo! Agora me lembro! O nome dele é {rival_name}!") 
    talk("PROF. OAK", f"{player_name}! Sua própria lenda Pokémon está prestes a começar! Um mundo de sonhos e aventuras espera por você! Então, vamos lá!")

    return player_name, rival_name

def start_journey(player_name, rival_name):
    print(f"{player_name} acorda atrasado no grande dia de escolher seu primeiro Pokémon.")
    next_dialogue()

    talk("MÃE", "É... todo garoto sai de casa um dia. Disseram isso na TV... Ah, sim. O PROF. CARVALHO quer falar com você.")

    print(f"\nCurioso, {player_name} sai de casa e caminha pela pequena cidade de Pallet.")
    next_dialogue()

    talk("PROF. CARVALHO", "Ei! Espere! Pokémon selvagens vivem na grama alta!")
    talk("PROF. CARVALHO", "Sem um Pokémon, seria perigoso ir sozinho. Venha comigo ao meu laboratório.")

    print(f"\n{player_name} acompanha o PROF. CARVALHO até o laboratório dele.")
    next_dialogue()
    
    print(f"\nAo entrar no laboratório, {player_name} encontra {rival_name} esperando impacientemente.")
    next_dialogue()

    talk(f"{rival_name}", "Finalmente chegou! Vovô! Estou cansado de esperar!")
    talk("PROF. CARVALHO", "Tenha paciência... Vocês dois vão ganhar seus próprios Pokémon hoje.")
    talk("PROF. CARVALHO", "Há três Pokémon aqui. Eles foram criados especialmente para jovens treinadores.")
    talk("PROF. CARVALHO", f"Escolha um deles, {player_name}.")