lista = [1, 3, 5, 3, 7, 9, 3]

# ? Entrada de usuário
numero = int(input("Digite um número: "))

# ? Contador
contador = 0
for item in lista:
    if item == numero:
        contador += 1

print("O número", numero,"apareceu", contador, "vez(es) na lista.")