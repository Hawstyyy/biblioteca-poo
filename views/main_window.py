import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.cadastroLivro import cadastroLivro
from views.cadastroUsuario import cadastroUsuario

ui_file = 'biblioteca-poo\\views\\main_window.ui'

class mainwindow(QMainWindow):
  def __init__(self) -> None:
    super().__init__()
    uic.loadUi(ui_file, self)
    self.cadastroButton.clicked.connect(self.clicked1)
    self.cadastroLivro = cadastroLivro()
    self.cadastroUsuario = cadastroUsuario()
  
  def clicked1(self):
    self.cadastroLivro.show()
    self.close()
  
  def clicked2(self):
    self.cadastroUsuario.show()
    self.close()