import mysql.connector

class Database:
  def __init__(self, host, user, senha, database):
    self.host = host
    self.user = user
    self.senha = senha
    self.database = database
    self.cursor = None
  
  def conectar(self):
    self.conexao = mysql.connector.connect(
      host = self.host,
      user = self.user,
      password = self.senha,
      database = self.database
    )

    self.cursor = self.conexao.cursor(dictionary=True)

    if self.conexao.is_connected():
      print('Ta conectado')
    
    else:
        print('Não ta conectado')
  
  def desconectar(self):
    self.conexao.close()
  
  def executarQuery(self, msg):
    self.cursor.execute(msg)
    self.conexao.commit()

  def visualizarQuery(self, msg):
    self.cursor.execute(msg)
    fetch = self.cursor.fetchall()
    return fetch