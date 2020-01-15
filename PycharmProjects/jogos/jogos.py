import forca
import adivinhacao
def escolhe_jogo():
    print("*********************")
    print("Escolha seu jogo")
    print("*********************")


    print("(1) Forca (2) Adivinhação")
    jogo = input(("Qual o jogo?"))

    if (jogo == 1 ):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2 ):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
