import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from controller.controllerEmprestimo import controllerEmprestimo

ui_file = 'biblioteca-poo\\views\\visualizarUsuario.ui'

class visualizarUsuario(QMainWindow):
  def __init__(self) -> None:
    super().__init__()
    uic.loadUi(ui_file, self)
    users = controllerEmprestimo().pegarTudoUsers()
    ls = []
    for x in users:
      user = list(x.values())
      ls.append(user)
    self.tableWidget.setRowCount(len(ls))
    for row in range(len(ls)):
      for column in range(6):
        self.tableWidget.setItem(row, column, QTableWidgetItem(str(ls[row][column])))
    self.fechar.clicked.connect(self.close)
    self.atualizar.clicked.connect(self.clicked1)
  
  def clicked1(self):
    users = controllerEmprestimo().pegarTudoUsers()
    ls = []
    for x in users:
      user = list(x.values())
      ls.append(user)
    self.tableWidget.setRowCount(len(ls))
    for row in range(len(ls)):
      for column in range(6):
        self.tableWidget.setItem(row, column, QTableWidgetItem(str(ls[row][column])))