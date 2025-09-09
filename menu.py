from service import cadastrar_livro, listar_livros, buscar_livro, gerar_grafico, saindo

def menu():
    while True:
        print("=== Biblioteca da Rua ===")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("4 - Gerar gráfico")
        print("5 - Sair")
        

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro()
        elif opcao == "4":
            gerar_grafico()
        elif opcao == "5":
            saindo()
            break
        else:
            print("Escolha uma opção valida.\n")