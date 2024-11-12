from ..model.database import Database
from ..model.usuario import Usuario
import mysql.connector

class controllerUsuario:
  def inserirUsuario(self):
    db = Database('10.28.2.16','suporte','suporte','biblioteca')
    db.conectar()
    query = Usuario('teste','testando','12312121312',0, '123').inserirUsuario()
    db.executarQuery(query)
    db.desconectar()
  
  def visualizarUsuario(self):
    db = Database('10.28.2.16','suporte','suporte','biblioteca')
    db.conectar()
    query = Usuario('teste','testando','12312121312',0, '123').visualizarUsuario('12312121312')
    visu = db.visualizarQuery(query)
    for x in visu:
      print(f'Usuário: {x}')
    db.desconectar()

  def atualizarUsuario(self):
    db = Database('10.28.2.16','suporte','suporte','biblioteca')
    db.conectar()
    query = Usuario('teste','testando','12312121312',0, '123').updateUsuario('nome', 'teste', "nome", "enzo")
    db.executarQuery(query)
    db.desconectar()
  
  def deletarUsuario(self):
    db = Database('10.28.2.16','suporte','suporte','biblioteca')
    db.conectar()
    query = Usuario('teste','testando','12312121312',0, '123').deleteUsuario('nome', 'teste')
    db.executarQuery(query)
    db.desconectar()

controllerUsuario().inserirUsuario()
controllerUsuario().visualizarUsuario()
controllerUsuario().atualizarUsuario()
controllerUsuario().deletarUsuario()