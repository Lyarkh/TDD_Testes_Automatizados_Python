import pytest
from src.leilao.dominio import Usuario, Leilao
from src.leilao.excecao import LanceInvalido

@pytest.fixture
def lucas():
    return Usuario('Lucas', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Café')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(lucas, leilao):
    lucas.propoe_lance(leilao, 50)

    assert lucas.carteira == 50.0

def test_deve_permitir_propor_lance_menor_que_o_valor_da_carteira(lucas, leilao):
    lucas.propoe_lance(leilao, 1.0)

    assert lucas.carteira == 99.0

def test_deve_permitir_propor_lance_igual_ao_valor_da_carteira(lucas, leilao):
    lucas.propoe_lance(leilao, 100.0)

    assert lucas.carteira == 0.0   

def test_nao_deve_permitir_propor_lance_maior_que_o_valor_da_carteira(lucas, leilao):
    with pytest.raises(LanceInvalido):
        lucas.propoe_lance(leilao, 200.0)

        assert lucas.carteira == 100.0
