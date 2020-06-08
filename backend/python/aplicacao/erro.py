from base_cadastro import BaseCadastro


class Erro(BaseCadastro):
    def __init__(self, cod_app, cod_ambiente, codigo, titulo, mensagem, origem,
                 nivel, data, hora, usuario):
        super().__init__()
        self.cod_app = cod_app
        self.cod_ambiente = cod_ambiente
        self.codigo = codigo
        self.titulo = titulo
        self.mensagem = mensagem
        self.origem = origem
        self.nivel = nivel
        self.data = data
        self.hora = hora
        self.usuario = usuario

    def cadastrar(self):
        raise NotImplementedError

    def listar_por_nivel(self, cod_app, cod_ambiente, nivel):
        raise NotImplementedError

    def listar_por_descricao(self, cod_app, cod_ambiente, descricao):
        raise NotImplementedError

    def listar_por_origem(self, cod_app, cod_ambiente, origem):
        raise NotImplementedError
