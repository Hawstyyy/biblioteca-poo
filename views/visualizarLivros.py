import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from controller.controllerEmprestimo import controllerEmprestimo

ui_file = 'biblioteca-poo\\views\\visualizarLivros.ui'

class visualizarLivro(QMainWindow):
  def __init__(self) -> None:
    super().__init__()
    uic.loadUi(ui_file, self)
    livros = controllerEmprestimo().pegarTudo()
    ls = []
    for x in livros:
      livro = list(x.values())
      ls.append(livro)
    self.tableWidget.setRowCount(len(ls))
    for row in range(len(ls)):
      for column in range(6):
        self.tableWidget.setItem(row, column, QTableWidgetItem(str(ls[row][column]))) 
    self.fechar.clicked.connect(self.close)
    self.atualizar.clicked.connect(self.clicked1)
  
  def clicked1(self):
    livros = controllerEmprestimo().pegarTudo()
    ls = []
    for x in livros:
      livro = list(x.values())
      ls.append(livro)
    self.tableWidget.setRowCount(len(ls))
    for row in range(len(ls)):
      for column in range(6):
        self.tableWidget.setItem(row, column, QTableWidgetItem(str(ls[row][column]))) 