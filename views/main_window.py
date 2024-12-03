import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.cadastroLivro import cadastroLivro
from views.cadastroUsuario import cadastroUsuario
from views.emprestimo import Emprestimo
from views.visualizarLivros import visualizarLivro

ui_file = 'biblioteca-poo\\views\\main_window.ui'

class mainwindow(QMainWindow):
  def __init__(self) -> None:
    super().__init__()
    uic.loadUi(ui_file, self)
    self.cadastroButton.clicked.connect(self.clicked1)
    self.cadastroUsuario.clicked.connect(self.clicked2)
    self.cadastroEmprestimo.clicked.connect(self.clicked3)
    self.visualizarLivro.clicked.connect(self.clicked4)
    self.cadastroLivro = cadastroLivro()
    self.cadastroUsuario = cadastroUsuario()
    self.Emprestimo = Emprestimo()
    self.visualizarLivro = visualizarLivro()
  
  def clicked1(self):
    self.cadastroLivro.show()
  
  def clicked2(self):
    self.cadastroUsuario.show()
  
  def clicked3(self):
    self.Emprestimo.show()

  def clicked4(self):
    self.visualizarLivro.show()