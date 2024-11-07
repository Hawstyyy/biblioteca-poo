from usuario import Usuario

class Livro:
  def __init__(self, autor, titulo, genero, cod_livro):
    self.autor = autor
    self.titulo = titulo
    self.genero = genero
    self.cod_livro = cod_livro
    self.status = 'Disponível'
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
    query = f'insert into livro(autor, titulo, genero,codigo, status) values ("{self.autor}","{self.titulo}","{self.genero}","{self.cod_livro}","{self.status}")'
    return query
  
  def visualizarLivro(self):
      query = f'select * from livro'
      return query

  def updateLivro(self, ctx1, ctx2, ctx3, ctx4):
      query = f'update livro set {ctx1} = "{ctx2}" where {ctx3} = "{ctx4}"'
      return query

  def deleteLivro(self, ctx1, ctx2):
      query = f'delete from livro where {ctx1} = "{ctx2}"'
      return query