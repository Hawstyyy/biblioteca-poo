class Usuario:
    MAX_EMPRESTIMO = 3
    def __init__(self,nome,email,cpf,telefone):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.lista_livros = []

    def pegar_emprestado(self,livro):
        if len(self.lista_livros) == self.MAX_EMPRESTIMO:
            return 'Limite de Empréstimo atingido.'

        self.lista_livros.append(livro.nome)

    def inserirUsuario(self):
        return f'insert into usuario(nome,email,cpf,telefone) values ("{self.nome}","{self.email}" ,"{self.cpf}", "{self.telefone}")'

    def visualizarUsuario(self, cpf):
        return f'select * from usuario where cpf = {cpf}'

    def updateUsuario(self,coluna1, valor1, coluna2, valor2):
        return f'update usuario set {coluna1} = "{valor1}" where {coluna2} = "{valor2}"'
    
    def deleteUsuario(self, coluna, valor):
        return f'delete from usuario where {coluna} = "{valor}"'

    def searchUsuario(self):
        return 'select nome from usuario'

Usuario.__name__ = 'Usuario'