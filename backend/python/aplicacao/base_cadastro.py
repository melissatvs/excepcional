from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import datetime


@dataclass
class BaseCadastro(ABC):
    def __init__(self):
        data_hora = datetime.now()
        # self.codigo = ?
        self.data_inclusao = data_hora.strftime('%d/%m/%Y')
        self.hora_inclusao = data_hora.strftime('%H/%M')

    @abstractmethod
    def cadastrar(self):
        pass

    @abstractmethod
    def excluir(self):
        pass
