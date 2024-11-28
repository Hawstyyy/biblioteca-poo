import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from model.emprestimo import Emprestimo
from controller.controllerEmprestimo import controllerEmprestimo

ui_file = 'biblioteca-poo\\views\\emprestimo.ui'

class Emprestimo(QMainWindow):
  def __init__(self) -> None:
    super().__init__()
    uic.loadUi(ui_file, self)
    self.values = controllerEmprestimo().pegarEmprestimo()
    self.lista = []
    for x in self.values:
      teste = ''.join(x.values())
      self.lista.append(teste)
      print(self.lista)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Emprestimo()
  window.show()
  sys.exit(app.exec_())