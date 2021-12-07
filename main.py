from src.leilao.dominio import Usuario, Leilao, Lance

edyane = Usuario("Edyane")
lucas = Usuario("Lucas")

lance_edyane = Lance(edyane, 100.0)
lance_lucas =  Lance(lucas, 150.0)

leilao = Leilao("Computador")

leilao.lances.append(lance_edyane)
leilao.lances.append(lance_lucas)

for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} fez um lance de {lance.valor}.")


