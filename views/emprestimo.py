import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from model.emprestimo import Emprestimo
from controller.controllerEmprestimo import controllerEmprestimo
from controller.controllerUsuario import controllerUsuario

ui_file = 'biblioteca-poo\\views\\emprestimo.ui'

class Emprestimo(QMainWindow):
  def __init__(self) -> None:
    super().__init__()
    uic.loadUi(ui_file, self)
    self.values = controllerEmprestimo().pegarEmprestimo()
    self.nomes = controllerUsuario('any', 'any', 'any', 'any').pegarUsuario()
    self.cadastroEmprestimo.clicked.connect(self.clicked1)
    self.cancelar.clicked.connect(self.close)
    self.lista = []
    self.nomesLista = []
    for x in self.values:
      teste = ''.join(x.values())
      self.lista.append(teste)
    for x in self.lista:
      self.comboBox.addItem(x)
    for x in self.nomes:
      nome = ''.join(x.values())
      self.nomesLista.append(nome)
    for x in self.nomesLista:
      self.comboBox_2.addItem(x)
  
  def clicked1(self):
    titulo = self.comboBox.currentText()
    nome = self.comboBox_2.currentText()
    controllerEmprestimo().inserirEmprestimo(nome, titulo)
    self.close()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Emprestimo()
  window.show()
  sys.exit(app.exec_())