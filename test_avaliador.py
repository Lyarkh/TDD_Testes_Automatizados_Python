import unittest
from unittest import TestCase
from dominio import Lance, Usuario, Leilao, Avaliador


class TestAvaliador(TestCase):
    
    def test_avalia(self):
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


if __name__ == "__main__":
    unittest.main()
