# Importações

import random
import time

# Introdução, diálogos e perguntas
CC = random.randint(1, 2)
print("\n== Russian Roulette ==\n")
time.sleep(0.5)
print("Loading...\n")
time.sleep(1.5)
print("Game made by: Manoel Antônio (GitHub: https://github.com/OCOYE)\n")
time.sleep(1)
input("Press 'Enter' to play")
time.sleep(0.5)
print("You throw the coin")
time.sleep(1.5)
if CC == 2:

    # Cara ou Coroa
    print("Heads comes up, and your opponent loads the bullet...")
    Bullet = int(input("\nYou as opponent, will you place the bullet where? [1 - 6]\n"))
    # Diálogo
    print("You and your opponente sit at the chair and start a dialog.")
    time.sleep(1.2)
    print("You:\n This game ends when I or you die, do you want play this?")
    time.sleep(1.2)
    print("Opponente:\n I want and you want.")
    time.sleep(1.2)
    print("You:\n Let the games begin...")
    time.sleep(1.2)

elif CC == 2:
    # Cara ou Coroa de novo
    print("Heads comes up, and you loads the bullet...")
    Bullet = int(input("\nWill you place the bullet where? [1 - 6]\n"))
    # Diálogo
    print("You and your opponente sit at the chair and start a dialog.")
    time.sleep(1.2)
    print("You:\n This game ends when I or you die, do you want play this?")
    time.sleep(1.2)
    print("Opponente:\n I want and you want.")
    time.sleep(1.2)
    print("You:\n Let the games begin...")
    time.sleep(1.2)
else:
    print("Error")
    input(" --- Error! My GitHub: https://github.com/OCOYE --- ")

# Jogo
while True:
    Generator = random.randint(1, 6)
    SeleRD = random.randint(1, 2)
    # Caso o seu adversário ganhe
    if Generator == Bullet and SeleRD == 1:
        print("You aimed the gun for your head and...")
        time.sleep(1.25)
        print("\n*PEW!* You got your head exploded. Your opponente won\n")
        # Diálogo
        print("...")
        time.sleep(1)
        print("*Laugh*")
        time.sleep(2.15)
        print("Opponente: I won... I WON!!")
        time.sleep(0.5)
        print("Dev Dialog: Thanks for playing my game :) - Manoel Antônio")
        # Terminar o jogo
        break
    # Caso você ganhe
    elif Generator == Bullet and SeleRD != 1:
        print("Your opponent aimed for head and...")
        time.sleep(1.25)
        print("\n*PEW!* You opponente died. You won!\n")
        # Diálogo
        print("...")
        time.sleep(1.5)
        print("You: He died...")
        time.sleep(0.5)
        print("Dev Dialog: Thanks for playing my game :) - Manoel Antônio")
        # Terminar o jogo
        break
    # Você
    elif Generator != Bullet and SeleRD == 1:
        print("You aimed the gun for your head and...")
        time.sleep(0.5)
        input("Shoot?")
        time.sleep(1.25)
        print("You're alive")
        input("Press 'Enter' to continue")
    # Adversário
    elif Generator != Bullet and SeleRD != 1:
        print("Your opponent aimed for head and...")
        time.sleep(0.5)
        print("He's alive")
        time.sleep(1)
        input("Grab the gun? (Press 'Enter')")
    else:
        # Caso dê algum erro
        print("\nError\n")
        input(" --- Error! My GitHub: https://github.com/OCOYE --- ")
        break