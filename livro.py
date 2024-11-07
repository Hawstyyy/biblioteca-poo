from usuario import Usuario

class Livro:
  def __init__(self, autor, nome, genero, cod_livro):
    self.autor = autor
    self.nome = nome
    self.genero = genero
    self.cod_livro = cod_livro
    self.status = 'Disponível'
    self.usuario = None
  
  def emprestimo_livro(self, usuario: Usuario):
      if self.status != 'disponivel':
          return

      self.usuario = usuario.nome
      self.status= "Emprestado"

  def devolver_livro(self):
      if self.status != 'Emprestado':
              return 'Não'

      self.usuario = None
      self.status = 'Disponivel'

  def inserirLivro(self):
    query = f'insert into livro(autor, titulo, genero,codigo, status) values ("{self.autor}","{self.nome}","{self.genero}","{self.cod_livro}","{self.status}")'
    return query
  
  def visualizarLivro(self):
      query = f'select * from livro'
      return query