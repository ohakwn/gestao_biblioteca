# Importanto a biblioteca matplotlib para fazer a criação do gráfico
import matplotlib.pyplot as plt

# Fazendo a criação de uma classe e de suas funções com valores determinados
class Livro:
  def __init__(self, titulo, autor, genero, quantidade):
    self.titulo = titulo
    self.autor = autor
    self.genero = genero
    self.quantidade = quantidade
  def __str__(self):
    return f"\n Título: {self.titulo}\n   Autor: {self.autor}\n   Gênero: {self.genero}\n   Quantidade: {self.quantidade}\n"

# Criação de uma lista vazia para armazenar os livros cadastrados
biblioteca = []

# Função cadastrar_livro é usada para adicionar novos livros a lista biblioteca
def cadastrar_livro(titulo, autor, genero, quantidade):
  novo_livro = Livro(titulo, autor, genero, quantidade)
  biblioteca.append(novo_livro)
  print(f"O livro {titulo} foi adicionado a biblioteca")

# Função listar_livros para listar todos os livros presentes na biblioteca
def listar_livros():
  for livro in biblioteca:
    print(livro)

# Função procurar_livro é usada para procurar um livro na biblioteca usando o título
def procurar_livro(titulo):
  for livro in biblioteca:
    if livro.titulo.lower() == titulo.lower():
      print("Livro Encontrado:")
      print(livro)
      
# Função para gerar gráfico da quantidade de livros por gênero
def gerar_grafico():
  # Verificando se existem livros cadastrados com uma estrutura condicional
  if not biblioteca:
    print("Não há livros cadastrados parar gerar gráfico")
  # Dicionário vazio para filtrar dos livros o gênero e sua quantidade
  generos = {}
  # laço de repetição para buscar livro por livro na bibliteca
  for livro in biblioteca:
    # aqui as chaves(generos) são separadas pelo método get(), quando chaves iguais são encontradas, seus valores(quantidade) são somados
    generos[livro.genero] = generos.get(livro.genero, 0) + livro.quantidade

  # aqui é criado o gráfico onde X é o gênero e Y a quantidade de livros
  plt.bar(generos.keys(), generos.values(), color="purple")
  plt.title("Quantidade de livros por Gênero")
  plt.xlabel("Gênero")
  plt.ylabel("Quantidade")
  plt.show()

# Fazendo o chamado das funções
cadastrar_livro('Fundação', 'Isaac Asimov', 'Ficção científica', 12)
cadastrar_livro('1984', 'George Orwell', 'Política', 5)
cadastrar_livro('O Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien', 'Fantasia', 7)
cadastrar_livro('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 'Fantasia', 14)
cadastrar_livro('Percy Jackson e o Ladrão de Raios', 'Rick Riordan', 'Fantasia', 9)

listar_livros()
procurar_livro('Fundação')
gerar_grafico()