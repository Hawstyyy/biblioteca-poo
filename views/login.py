import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

ui_file = 'biblioteca-poo\\views\\login.ui'

class mainwindow(QMainWindow):
  def __init__(self) -> None:
    super().__init__()
    uic.loadUi(ui_file, self)
    self.entrarButton.clicked.connect(self.clicked)
  def clicked(self):
    self.close()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = mainwindow()
  window.show()
  sys.exit(app.exec_())