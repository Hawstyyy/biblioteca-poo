from model.emprestimo import Emprestimo
from model.database import Database

class controllerEmprestimo:
  def __init__(self):
    self.db = Database('10.28.2.16','suporte','suporte','biblioteca')

  def inserirEmprestimo(self):
    self.db.conectar()
    query = Emprestimo('any','any')
    self.db.executarQuery(query)
    self.db.desconectar()
  
  