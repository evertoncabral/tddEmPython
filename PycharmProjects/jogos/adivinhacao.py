import random
from typing import Any, Union
def jogar():
    print("*********************")
    print("Bem vindo ao jogo de adivinhação")
    print("*********************")

    pontos =1000
    numero_secreto = round(random.randrange(0 , 101,1))
    total_de_tentativas = 0
    print(numero_secreto)
    print("Qual o nível de dificuldade?")
    print("1 Fácil, 2 Médio , 3 Difícil")

    nivel = int(input("Define o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range ( 1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute <1 or chute>100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if(acertou):
            print("Parabéns! Você acertou!")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
                print( "total de pontos:{}". format(pontos))
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
                print( "total de pontos:{}".format(pontos))


        rodada = rodada + 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()