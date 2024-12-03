from model.emprestimo import Emprestimo
from model.database import Database

class controllerEmprestimo:
  def __init__(self):
    self.db = Database('10.28.2.16','suporte','suporte','biblioteca')

  def inserirEmprestimo(self, nome, titulo):
    self.db.conectar()
    query = Emprestimo('any','any').inserirEmprestimo(nome, titulo)
    self.db.executarQuery(query)
    self.db.desconectar()
  
  def pegarEmprestimo(self):
    self.db.conectar()
    query = Emprestimo('any','any').searchLivro()
    fetch = self.db.visualizarQuery(query)
    self.db.desconectar
    return fetch
  
  def pegarTudo(self):
    self.db.conectar()
    query = Emprestimo('any','any').searchAll()
    fetch = self.db.visualizarQuery(query)
    self.db.desconectar()
    return fetch