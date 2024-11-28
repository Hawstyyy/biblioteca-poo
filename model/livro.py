from usuario import Usuario

class Livro:
  def __init__(self, autor, titulo, genero, cod_livro, status):
    self.autor = autor
    self.titulo = titulo
    self.genero = genero
    self.cod_livro = cod_livro
    self.status = status
    self.usuario = None
  
  def emprestimo_livro(self, usuario: Usuario):
      if self.status != 'disponivel':
          return

      self.usuario = usuario.titulo
      self.status= "Emprestado"

  def devolver_livro(self):
      if self.status != 'Emprestado':
              return 'Não'

      self.usuario = None
      self.status = 'Disponivel'

  def inserirLivro(self):
    return f'insert into livro(autor, titulo, genero,codigo, status) values ("{self.autor}","{self.titulo}","{self.genero}","{self.cod_livro}","{self.status}")'
  
  def visualizarLivro(self, titulo):
    return f'select * from livro where titulo = "{titulo}"'

  def updateLivro(self, coluna1, valor1, coluna2, valor2):
    return f'update livro set {coluna1} = "{valor1}" where {coluna2} = "{valor2}"'
      

  def deleteLivro(self, coluna, valor):
    return f'delete from livro where {coluna} = "{valor}"'

Livro.__name__ = 'Livro'