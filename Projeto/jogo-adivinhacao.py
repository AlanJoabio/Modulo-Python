#Criando um jogo de adivinhação com orientação do professor Diego

import random

def jogo_da_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Estou pensando em um número de 1 a 100.")

    while True:
        tentativa = int(input("Digite o seu palpite: "))
        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break
        elif tentativa < numero_secreto:
            print("O número é maior. Tente novamente!")
        else:
            print("O número é menor. Tente novamente!")

    reiniciar = input("Deseja jogar novamente? (s/n): ")
    if reiniciar.lower() == "s":
        jogo_da_adivinhacao()
    else:
        print("Obrigado por jogar. Até a próxima!")

jogo_da_adivinhacao()
