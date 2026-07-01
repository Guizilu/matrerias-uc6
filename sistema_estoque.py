
# ! CRIANDO UMA LISTA VAZIA
produtos = []

# ? Váriavel auxiliar para controlar o loop
sair = False

print("Bem-vindo ao Sistema de Estoque!")
# ! Repita enquanto sair é igual a false
while sair == False:
    # ? Menu dentro do loop para repetir
    print("-"*20)
    print("1- Listar produtos")
    print("2- Cadastrar um novo produto")
    print("3- Deletar um produto")
    print("0- Sair do sistema")
    # ! Pedir para a pessoa digitar a opção:
    opcao = input("Sua opção: ")
    # ! Escolha Caso / Match Case
    match opcao:
        case '0':
            # ? Colocamos sair como verdadeiro para que quando rodar o çoop ele sair.
            sair = True
        case '1':
            # & Listar produtos
            for p in produtos:
                print("-", p)
            print("#"*30)
        case '2':
            print("Cadastrar novo produto: ") 
            nome_produto = input("Nome do produto: ")
            # ! A função append adiciona um novo item em uma lista
            produtos.append(nome_produto)
        case '3':
            print("Remover produto: ")
            nome_produto = input("Qual deletado: ")
            # !Checar se o deletado existe na lista
            if nome_produto in produtos:    
                produtos.remove(nome_produto)
                print("Removido com sucesso!")
            else:
                print(nome_produto, " não existe na lista!")

            input("Pressione enter para continuar...")    