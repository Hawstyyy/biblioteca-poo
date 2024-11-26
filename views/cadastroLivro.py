import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

ui_file = 'cadastroLivro.ui'

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi(ui_file, self)
    self.botaoTeste.clicked.connect(self.clicked)
    self.valor = 0

  def clicked(self):
    titulo = self.titulo.text()
    autor = self.autor.text()
    genero = self.genero.text()
    codigo = self.codigo.text()
    status = self.status.currentText()
    self.valor += 1
    print(f'''Título - {titulo}
Autor - {autor}
Gênero - {genero}
Código - {codigo}
Status - {status}''')
  
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())