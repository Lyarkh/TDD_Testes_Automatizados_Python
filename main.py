from dominio import Usuario, Leilao, Lance, Avaliador

edyane = Usuario("Edyane")
lucas = Usuario("Lucas")

lance_edyane = Lance(edyane, 100.0)
lance_lucas =  Lance(lucas, 200.0)

leilao = Leilao("Computador")

leilao.lances.append(lance_edyane)
leilao.lances.append(lance_lucas)

for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} fez um lance de {lance.valor}.\n")

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f"O menor lance foi {avaliador.menor_valor} e o maior lance fou {avaliador.maior_valor}")
