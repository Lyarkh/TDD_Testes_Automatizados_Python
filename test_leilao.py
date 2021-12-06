import unittest
from unittest import TestCase
from dominio import Lance, Usuario, Leilao


class TestLeilao(TestCase):
    
    def setUp(self):
        self.edyane = Usuario("Edyane")
        self.lance_edyane = Lance(self.edyane, 100.0)
        self.leilao = Leilao("Computador")

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        lucas = Usuario("Lucas")
        self.lance_lucas =  Lance(lucas, 150.0)

        self.leilao.propoe(self.lance_edyane)
        self.leilao.propoe(self.lance_lucas)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        lucas = Usuario("Lucas")
        self.lance_lucas =  Lance(lucas, 150.0)

        self.leilao.propoe(self.lance_lucas)
        self.leilao.propoe(self.lance_edyane)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    
    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_edyane)

        menor_valor_esperado = maior_valor_esperado = 100.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        klovis = Usuario("Klovis")
        lucas = Usuario("Lucas")

        lance_klovis = Lance(klovis, 200.0)
        self.lance_lucas =  Lance(lucas, 150.0)

        self.leilao.propoe(self.lance_lucas)
        self.leilao.propoe(self.lance_edyane)
        self.leilao.propoe(lance_klovis)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_não_tenha_lances(self):
        self.leilao.propoe(self.lance_edyane)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        lucas = Usuario("Lucas")
        lance_lucas = Lance (lucas, 200.0)
        
        self.leilao.propoe(self.lance_edyane)
        self.leilao.propoe(lance_lucas)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_se_o_usuario_for_o_mesmo(self):
        lance_edyane_02 = Lance(self.edyane, 345.0)

        self.leilao.propoe(self.lance_edyane)
        self.leilao.propoe(lance_edyane_02)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

        

#Deve importar unittest para que apareça o teste no prompt do Visual Studio Code
if __name__ == "__main__":
    unittest.main()
