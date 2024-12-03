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
    query = Usuario('teste','testando','12312121312',0, '123').visualizarUsuario('12312121312')
    visu = self.db.visualizarQuery(query)
    for x in visu:
      print(f'Usuário: {x}')
    self.db.desconectar()

  def atualizarUsuario(self):
    self.db.conectar()
    query = Usuario('teste','testando','12312121312',0, '123').updateUsuario('nome', 'teste', "nome", "enzo")
    self.db.executarQuery(query)
    self.db.desconectar()
  
  def deletarUsuario(self):
    self.db.conectar()
    query = Usuario('teste','testando','12312121312',0, '123').deleteUsuario('nome', 'teste')
    self.db.executarQuery(query)
    self.db.desconectar()

  def checarUsuario(self,nome,cpf):
    self.db.conectar()
    query = Usuario(nome, cpf=cpf)
    self.db.desconectar()
  
  def pegarUsuario(self):
    self.db.conectar()
    query = Usuario('any', 'any', 'any', 'any').searchUsuario()
    fetch = self.db.visualizarQuery(query)
    self.db.desconectar()
    return fetch
  