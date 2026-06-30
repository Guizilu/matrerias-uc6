podeEntrar = False

while podeEntrar == False:
    eh_maior = input("Você tem mais de 18 anos? s/n ")
    if eh_maior == "s" or eh_maior == "S":
        tem_ingresso = input("Tem ingresso? s/n ")
        if tem_ingresso == "s" or tem_ingresso == "S":
            podeEntrar = True
        else:
            print("Infelizmente sem ingresso não dá")
    else:
        print("Num pode rapá")

    print("\n\n\n")

print("BEM VINDO A FESTA!!")