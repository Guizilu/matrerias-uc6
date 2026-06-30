produto1 = ["Playstation 5", 3500]
produto2 = ["GTA VI Six Seis", 549]
produto3 = ["RTX 5090", 27999]
produto4 = ["Injeção na Testa", 5000]

# ! Podemos colocar uma lista dentro da outra

produtos = [produto1, produto2, produto3, produto4]

# ! Mostrando o que tem dentro de 'produtos'
print(produtos)

# ! Acessando o nome de um produto
# ? [1] -> Acessa a lista toda do produto2
# ? [1][0] -> Acessa o produto2 e pega o nome (indice 0)
print("Nome do produto: ", produtos[1][0])

# ! Também podemos colocar uma lista dentro da outra na criação

carro = ["Fiat", ["Palio", "Punto", "Fastback", "Toro"]]

print("Acessando a Toro: ", carro[1][3])


