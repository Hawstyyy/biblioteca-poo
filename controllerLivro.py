from livro import Livro
from database import Database
import mysql.connector

class controllerLivro:
  def inserirLivro(self):
    db = Database('10.28.2.16','suporte','suporte','biblioteca')
    db.conectar()
    query = Livro('teste','teste','testando', 123).inserirLivro()
    print(query)
    db.executarQuery(query)
    db.desconectar()
  
  def visualizarLivro(self):
    db = Database('10.28.2.16','suporte','suporte','biblioteca')
    db.conectar()
    db.desconectar()

controllerLivro().inserirLivro()
controllerLivro().visualizarLivro()