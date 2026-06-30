# Input - Entrada de Dados
# É quando pedimos para o usuário digitar algo

# Isso faz com que nosso programa fique personalizado, pois funcionará com dados dos clientes/usuarios

# input() == leia(nome_filme)
# Mas nele colocamos a pergunta JUNTO
nome_filme = input("Digite o nome do seu filme favorito: ")
ano_filme = int(input("Digite o ano de lançamento dele: "))

total_anos = 2026 - ano_filme

print("O seu filme tem: ", total_anos, " anos")


