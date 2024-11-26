from controllerUsuario import controllerUsuario
from controllerLivro import controllerLivro
from controllerEmprestimo import Emprestimo
from model.database import Database
from model.admin import Admin

class controllerAdmin:
  def cadastrarLivro():
    controllerLivro.inserirLivro()