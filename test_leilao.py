import unittest
from unittest import TestCase
from dominio import Lance, Usuario, Leilao

class TestLeilao(TestCase):

    def setUp(self):
        self.edyane = Usuario('Edyane')
        self.lance_da_edyane = Lance(self.edyane, 150.0)
        self.leilao = Leilao('PC')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        lucas = Usuario('Lucas')
        lance_do_lucas = Lance(lucas, 100.0)

        self.leilao.propoe(lance_do_lucas)
        self.leilao.propoe(self.lance_da_edyane)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(ValueError):
            lucas = Usuario('Lucas')
            lance_do_lucas = Lance(lucas, 100.0)

            self.leilao.propoe(self.lance_da_edyane)
            self.leilao.propoe(lance_do_lucas)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_da_edyane)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        lucas = Usuario('Lucas')
        lance_do_lucas = Lance(lucas, 100.0)
        klovis = Usuario('Klovis')

        lance_do_klovis = Lance(klovis, 200.0)

        self.leilao.propoe(lance_do_lucas)
        self.leilao.propoe(self.lance_da_edyane)
        self.leilao.propoe(lance_do_klovis)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_da_edyane)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        lucas = Usuario('Lucas')
        lance_do_lucas = Lance(lucas, 200.0)

        self.leilao.propoe(self.lance_da_edyane)
        self.leilao.propoe(lance_do_lucas)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_da_edyane_02 = Lance(self.edyane, 200.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_da_edyane)
            self.leilao.propoe(lance_da_edyane_02)

# #Deve importar unittest para que apareça o teste no prompt do Visual Studio Code
if __name__ == "__main__":
    unittest.main()
