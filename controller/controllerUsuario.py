from model.usuario import Usuario
from model.database import Database

class controllerUsuario:
  def __init__(self, nome, email, cpf, telefone) -> None:
    self.db = Database('10.28.2.16','suporte','suporte','biblioteca')
    self.nome = nome
    self.email = email
    self.cpf = cpf
    self.telefone = telefone

  def inserirUsuario(self):
    self.db.conectar()
    query = Usuario(self.nome, self.email, self.cpf, self.telefone).inserirUsuario()
    self.db.executarQuery(query)
    self.db.desconectar()
  
  def visualizarUsuario(self):
    self.db.conectar()
    query = Usuario('any', 'any', 'any', 'any').visualizarUsuario('12312121312')
    visu = self.db.visualizarQuery(query)
    for x in visu:
      print(f'Usuário: {x}')
    self.db.desconectar()

  def atualizarUsuario(self):
    self.db.conectar()
    query = Usuario('any', 'any', 'any', 'any').updateUsuario('nome', 'teste', "nome", "enzo")
    self.db.executarQuery(query)
    self.db.desconectar()
  
  def deletarUsuario(self):
    self.db.conectar()
    query = Usuario('any', 'any', 'any', 'any').deleteUsuario('nome', 'teste')
    self.db.executarQuery(query)
    self.db.desconectar()
  
  def pegarUsuario(self):
    self.db.conectar()
    query = Usuario('any', 'any', 'any', 'any').searchUsuario()
    fetch = self.db.visualizarQuery(query)
    self.db.desconectar()
    return fetch
  
  def checarUsuario(self):
    self.db.conectar()
    query = Usuario('any', 'any', 'any', 'any').verificarUsuario()
    fetch = self.db.visualizarQuery(query)  
    self.db.desconectar()
    return fetch