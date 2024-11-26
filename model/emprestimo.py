class Emprestimo:
  def __init__(self, livro, usuario):
    self.livro = livro
    self.usuario = usuario
  
  def inserirEmprestimo(self):
    return f'insert into emprestimo(nome_usuario, titulo_livro) values ({self.usuario}, {self.livro})'