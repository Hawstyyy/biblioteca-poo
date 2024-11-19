import sys
sys.path[0] += '\\..'
from model.livro import Livro
from model.database import Database

class controllerLivro:
  def inserirLivro(self):
    db = Database('10.28.2.16','suporte','suporte','biblioteca')
    db.conectar()
    query = Livro('teste','teste','testando', 123).inserirLivro()
    db.executarQuery(query)
    db.desconectar()
  
  def visualizarLivro(self):
    db = Database('10.28.2.16','suporte','suporte','biblioteca')
    db.conectar()
    query = Livro('teste','teste','testando', 123).visualizarLivro('teste')
    visu = db.visualizarQuery(query)
    for x in visu:
      print(f'Livro: {x}')
    db.desconectar()

  def atualizarLivro(self):
    db = Database('10.28.2.16','suporte','suporte','biblioteca')
    db.conectar()
    query = Livro('teste','teste','testando', 123).updateLivro('autor', 'teste', "autor", "enzo")
    db.executarQuery(query)
    db.desconectar()
  
  def deletarLivro(self):
    db = Database('10.28.2.16','suporte','suporte','biblioteca')
    db.conectar()
    query = Livro('teste','teste','testando', 123).deleteLivro('autor', 'teste')
    db.executarQuery(query)
    db.desconectar()

controllerLivro().inserirLivro()
controllerLivro().visualizarLivro()
controllerLivro().atualizarLivro()
controllerLivro().deletarLivro()
