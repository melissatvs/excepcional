from base_cadastro import BaseCadastro


class Usuario(BaseCadastro):
    def __init__(self, email, senha):
        super().__init__()
        self.email = email
        self.senha = senha

    def cadastrar(self):
        raise NotImplementedError

    def excluir(self):
        raise NotImplementedError

    def acessar(self):
        raise NotImplementedError

    def recuperar_senha(self):
        raise NotImplementedError
