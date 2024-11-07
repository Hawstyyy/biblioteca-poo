class Usuario:
    MAX_EMPRESTIMO = 3
    def init(self,nome,email,cpf,admin):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.admin = admin
        self.lista_livros = []

    def pegar_emprestado(self,livro):
        if len(self.lista_livros) == self.MAX_EMPRESTIMO:
            return 'Limite de Empréstimo atingido.'

        self.lista_livros.append(livro.nome)