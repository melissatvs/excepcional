from base_cadastro import BaseCadastro


class Ambiente(BaseCadastro):
    def __init__(self, aplicativo, nome):
        super().__init__()
        self.aplicativo = aplicativo
        self.nome = nome

    def cadastrar(self):
        raise NotImplementedError

    def excluir(self):
        raise NotImplementedError
