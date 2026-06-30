# Nesse jogo o sistema irá sortear um numero
# E o jogador deverá acertar esse número secreto
# Ele tem 5 vidas antes do gameover
# Precisamos importar a funcionalidade de sorteio
import random

# Dentro do 'random' que é o pacote de sorteio
# randint é uma função que escolhemos numero minimo e máximo para sorteio.
numero_secreto = random.randint(1, 100)
ganhou = False
vidas = 5

# O loop continua enquanto: Ainda não ganhou E ainda não morreu
while ganhou == False and vidas > 0:
    jogada = int(input("Sua jogada: "))
    # Se os numeros forem iguais VENCE
    if jogada == numero_secreto:
        ganhou = True
    else:
        # ERROU
        print("Você errou!")
        vidas = vidas - 1
        if jogada > numero_secreto:
            print("O seu número está acima do secreto")
        else:
            print("O seu número está abaixo do secreto")
    print("-" * 50)

if vidas > 0:
    print("PARABÉNS VOCÊ ACERTOU!")
    print("O número secreto: ", numero_secreto)
else:
    print("GAME OVER")
    print("O número secreto: ", numero_secreto)
