import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from controller.controllerUsuario import controllerUsuario

ui_file = 'biblioteca-poo\\views\\cadastroUsuario.ui'

class cadastroUsuario(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi(ui_file, self)
    self.cadastrarUsuario.clicked.connect(self.clicked)
  
  def clicked(self):
    nome = self.nomeCadastro.text()
    email = self.cadastroEmail.text()
    cpf = self.cadastroCpf.text()
    telefone = self.telefoneCadastro.text()
    controllerUsuario(nome,email,cpf,telefone).inserirUsuario()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = cadastroUsuario()
  window.show()
  sys.exit(app.exec_())