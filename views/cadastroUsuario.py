import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
# from controller.controllerUsuario import Usuario

ui_file = 'biblioteca-poo\\views\\cadastroUsuario.ui'

class cadastroUsuario(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi(ui_file, self)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = cadastroUsuario()
  window.show()
  sys.exit(app.exec_())