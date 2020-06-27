from ambiente import Ambiente
import pytest


dict_values = [
    ('excepcional', 'producao'),
    ('excepcional', 'desenvolvimento')
]


@pytest.mark.parametrize('aplicativo, ambiente', dict_values)
def test_cadastrar_ambiente(aplicativo, ambiente):
    amb = Ambiente(aplicativo, ambiente)
    assert amb.cadastrar() == True
