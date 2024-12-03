class Emprestimo:
  def __init__(self, livro, usuario):
    self.livro = livro
    self.usuario = usuario
  
  def searchLivro(self):
    return 'select titulo from livro'
  
  def searchAll(self):
    return 'select * from livro'

  def inserirEmprestimo(self, usuario, titulo):
    return f'insert into emprestimo(nome, titulo) values ("{usuario}", "{titulo}");'