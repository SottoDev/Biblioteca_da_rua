# 📚 Sistema de Gestão de Livros

---

## 🚀 O que é isso?

Um projetinho em Python que faz a gestão de livros de uma pequena biblioteca.
Com ele você pode:

-  Adicionar livros (com título, autor, gênero e quantidade)
-  Listar todos os livros cadastrados
-  Buscar um livro pelo título
-  Gerar um gráfico de quantidade de livros por gênero
- Evitar duplicação (se cadastrar um livro repetido, ele soma a quantidade)

---

## ⚙️ Como funciona?

Você abre o programa e o menu interativo aparece.
Escolhe a opção desejada (cadastrar, listar, buscar, gerar gráfico ou sair).
Os livros ficam guardados numa lista de objetos em memória.

---

## 📝 Regras

Livro repetido não é cadastrado novamente → apenas atualiza a quantidade.
Se não houver livros cadastrados, o sistema avisa nas opções de listagem, busca ou gráfico.

---

## 🎯 Exemplo
  ```bash
Menu inicial
=== Biblioteca da Rua ===
1 - Cadastrar livro
2 - Listar livros
3 - Buscar livro
4 - Gerar gráfico
5 - Sair
```

---

## 📌 Cadastro de livro

  ```bash
--- Cadastro de Livro ---
Título: Dom Casmurro
Autor: Machado de Assis
Gênero: Romance
Quantidade: 2
Livro 'Dom Casmurro' cadastrado com sucesso!
```

---

## 📌 Busca de livro

  ```bash
Digite o título do livro que deseja buscar: Dom Casmurro
Encontrado: Dom Casmurro - Machado de Assis (Romance) | Quantidade: 2
```

---

## 📌 Exemplo de gráfico

O sistema gera um gráfico de barras mostrando a quantidade de livros por gênero:


## 📂 Estrutura do código

- O sistema é dividido em funções para ficar mais organizado:
- cadastrar_livro() → cadastra um novo livro ou atualiza a quantidade.
- listar_livros() → mostra todos os livros cadastrados.
- buscar_livro() → pesquisa um livro pelo título.
- gerar_grafico() → cria um gráfico com a quantidade de livros por gênero.
- menu() → ponto de entrada que organiza a execução.

## 📌 Observações

- Dá pra cadastrar qualquer quantidade de livros.
- Se o mesmo título for inserido mais de uma vez, a quantidade é atualizada automaticamente.
- Se não houver livros cadastrados, o sistema avisa em vez de quebrar.
- Código está comentado para facilitar o entendimento.