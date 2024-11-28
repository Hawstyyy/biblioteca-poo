import model
import controller
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
import views.login as login
import views.cadastroLivro as cadastroLivro

app = QApplication(sys.argv)
window = login.mainwindow()

