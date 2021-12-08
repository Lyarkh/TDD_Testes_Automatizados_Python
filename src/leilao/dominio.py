import sys

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if valor > self.__carteira:
            raise ValueError ("Não é possivel propor lance com valor maior que o da carteira")
        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor
        
    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max
        self.__lances = []

    def propoe(self, lance: Lance):
        if not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
                
            self.__lances.append(lance)
            
        else:
            raise ValueError('Erro ao propor lance.')

    @property
    def lances(self):
        return self.__lances[:]



