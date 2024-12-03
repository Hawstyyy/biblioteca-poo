import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from views.main_window import mainwindow
from controller.controllerUsuario import controllerUsuario

ui_file = 'biblioteca-poo\\views\\login.ui'

class login(QMainWindow):
  def __init__(self) -> None:
    super().__init__()
    uic.loadUi(ui_file, self)
    self.main_window = mainwindow()
    self.entrarButton.clicked.connect(self.clicked)
    self.show()
    self.controllerUsuario = controllerUsuario('any', 'any', 'any', 'any')

  def clicked(self):
    nome = self.nomeInput.text()
    cpf = self.senhaInput.text()
    fetch = self.controllerUsuario.checarUsuario()
    login = False
    for x in range (len(fetch)):
      if fetch[x]['nome'] == nome and fetch[x]['cpf'] == cpf:
        login = True
        break
      else:
        login = False
    
    if login == True:
      self.main_window.show()
      self.close()
    else:
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Critical)
      msg.setText("Error")
      msg.setInformativeText('nome ou senha incorretos')
      msg.setWindowTitle("Error")
      msg.exec_()