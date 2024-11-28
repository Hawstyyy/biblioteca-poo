import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from controller.controllerLivro import controllerLivro

ui_file = 'biblioteca-poo\\views\\cadastroLivro.ui'

class cadastroLivro(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi(ui_file, self)
    self.botaoTeste.clicked.connect(self.clicked)

  def clicked(self):
    titulo = self.titulo.text()
    autor = self.autor.text()
    genero = self.genero.text()
    codigo = self.codigo.text()
    status = self.status.currentText()
    controllerLivro().inserirLivro(autor, titulo, genero, codigo, status)