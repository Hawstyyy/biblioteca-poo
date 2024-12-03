import sys
from PyQt5.QtWidgets import QApplication
from views.login import login

app = QApplication(sys.argv)
login = login()
sys.exit(app.exec_())