cores = ["Preto", "Verde", "Azul"]

# ! Operador 'in' é um teste para saber se algum item está dentro de uma lista

if "Rosa" in cores:
    print("A cor está lá dentro da lista!")
elif "Verde" in cores:
    print("Agora sim, essa tem!")
else:
    print("Não tem essa cor lá")

# ! ÍNDICE NEGATIVO

arsenal = ["Espada", "Lança", "Machado", "Arco", "Besta", "Estrela da Manhã", "Maça", "Marreta", "Montante", "Cimitarra", "Sabre", "Alabarda", "Tacape", "Porrete", "Clava", "Faca", "Adaga", "Punhal", "Katar", "Katana", "Rapieira"]

# ! Ordem inversa (-1) é o ultimo item

print("-1: ", arsenal[-1])

# ! Ordem inversa (-2) é o penultimo item
print("-2: ", arsenal[-2])
