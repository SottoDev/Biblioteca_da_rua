from model import Livro
import matplotlib.pyplot as plt
from collections import Counter
import time

livros = []  # Lista que armazena os livros cadastrados

#Cadastro dos livros
def cadastrar_livro():
    print("\n--- Cadastro de Livro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Gênero: ")
    quantidade = int(input("Quantidade: "))

    # Verifica se o livro já existe
    for livro in livros:
        if livro.titulo.lower() == titulo.lower():
            print(f"Erro 02 - O livro '{titulo}' já foi cadastrado!")
            livro.quantidade += quantidade
            print(f"Atualizada a quantidade: agora tem {livro.quantidade} exemplares.\n")
            return

    # Se não existir, cadastra normalmente
    novo_livro = Livro(titulo, autor, genero, quantidade)
    livros.append(novo_livro)
    print(f"Livro '{titulo}' cadastrado com sucesso. Obrigado\n")

# Função para listar livros
def listar_livros():
    print("\n--- Lista de Livros ---")
    if not livros:
        print("Nenhum livro cadastrado.\n")
        return
    for idx, livro in enumerate(livros, 1):
        print(f"{idx}. {livro.titulo} - {livro.autor} ({livro.genero}) | Quantidade: {livro.quantidade}")
    print()


# Função para buscar livro
def buscar_livro():
    titulo = input("\nDigite o título do livro que deseja buscar: ")
    for livro in livros:
        if livro.titulo.lower() == titulo.lower():
            print(f"Livro encontrado: {livro.titulo} - {livro.autor} ({livro.genero}) | Quantidade: {livro.quantidade}\n")
            return
    print("Error01 - Livro não encontrado.\n")

#animação para de saindo
def saindo():
    print("Saindo...", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(0.5)
    print()


#Cria o gráfico
def gerar_grafico():
    if not livros:
        print("Error..\n")
        return

    contagem = Counter()
    for livro in livros:
        contagem[livro.genero] += livro.quantidade

    generos = list(contagem.keys())
    quantidades = list(contagem.values())

    plt.bar(generos, quantidades)
    plt.title("Quantidade de livros por gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de exemplares")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

