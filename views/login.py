import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.main_window import mainwindow

ui_file = 'biblioteca-poo\\views\\login.ui'

class login(QMainWindow):
  def __init__(self) -> None:
    super().__init__()
    uic.loadUi(ui_file, self)
    self.main_window = mainwindow()
    self.entrarButton.clicked.connect(self.clicked)
    self.show()

  def clicked(self):
    self.main_window.show()
    self.close()