from usuario import Usuario

class Admin(Usuario):
  def __init__(self, nome, email, cpf, telefone, admin):
    super().__init__(nome, email, cpf, telefone)
    self.admin = admin