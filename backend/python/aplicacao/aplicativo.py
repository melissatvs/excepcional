from base_cadastro import BaseCadastro


class Aplicativo(BaseCadastro):
    def __init__(self, usuario, nome):
        super().__init__()
        self.usuario = usuario
        self.nome = nome

    def cadastrar(self):
        raise NotImplementedError
