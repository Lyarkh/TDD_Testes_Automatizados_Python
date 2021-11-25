from dominio import Usuario, Leilao, Lance, Avaliador

edyane = Usuario("Edyane")
lucas = Usuario("Lucas")

lance_edyane = Lance(edyane, 180.0)
lance_lucas =  Lance(lucas, 150.0)

leilao = Leilao("Computador")

leilao.lances.append(lance_edyane)
leilao.lances.append(lance_lucas)

for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} fez um lance de {lance.valor}.")

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f"O menor lance foi {avaliador.menor_lance} e o maior lance foi {avaliador.maior_lance}")
