import random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    pontos = 1000
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    print("escolha a dificuldade")
    print("Facil (1) normal (2) dificil (3)")
    dificuldade = int(input("defina a dificuldade:"))
    if (dificuldade == 1):
        total_de_tentativas = 20
    elif (dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5



    for rodada in range(1, total_de_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input(" digite seu numero: ")
        print ("voce digitou", chute_str)
        chute = int(chute_str)
        if (chute < 1 or chute > 100):
            print("digite um numero entre 0 e 100")
            continue
        acertou = numero_secreto == chute
        menor = numero_secreto > chute
        maior = numero_secreto < chute
        if (acertou):
            print("voce acertou e fez", pontos, "pontos")
            break
        else:
            if(maior):
                print(" voce errou! seu chute foi maior que o numero")
            elif(menor):
                print(" voce errou! seu chute foi menor que o numero")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


        rodada = rodada + 1

    print(" fim do jogo")
if (__name__ == "__main__"):
    jogar()
