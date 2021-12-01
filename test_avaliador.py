import unittest
from unittest import TestCase
from dominio import Lance, Usuario, Leilao, Avaliador


class TestAvaliador(TestCase):
    
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        edyane = Usuario("Edyane")
        lucas = Usuario("Lucas")

        lance_edyane = Lance(edyane, 100.0)
        lance_lucas =  Lance(lucas, 150.0)

        leilao = Leilao("Computador")

        leilao.lances.append(lance_edyane)
        leilao.lances.append(lance_lucas)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        edyane = Usuario("Edyane")
        lucas = Usuario("Lucas")

        lance_edyane = Lance(edyane, 100.0)
        lance_lucas =  Lance(lucas, 150.0)

        leilao = Leilao("Computador")

        leilao.lances.append(lance_lucas)
        leilao.lances.append(lance_edyane)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    
    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        edyane = Usuario("Edyane")
        
        lance_edyane = Lance(edyane, 100.0)
        
        leilao = Leilao("Computador")
        
        leilao.lances.append(lance_edyane)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = maior_valor_esperado = 100.0
       

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        edyane = Usuario("Edyane")
        lucas = Usuario("Lucas")
        klovis = Usuario("Klovis")

        lance_edyane = Lance(edyane, 100.0)
        lance_lucas =  Lance(lucas, 150.0)
        lance_klovis =  Lance(klovis, 200.0)

        leilao = Leilao("Computador")

        leilao.lances.append(lance_lucas)
        leilao.lances.append(lance_edyane)
        leilao.lances.append(lance_klovis)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

#Deve importar unittest para que apareça o teste no prompt do Visual Studio Code
if __name__ == "__main__":
    unittest.main()
