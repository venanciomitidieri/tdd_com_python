from src.dominio import Usuario, Lance, Leilao

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_yuri = Lance(yuri, 100.00)
lance_do_gui = Lance(gui, 150.00)


leilao = Leilao('Celular')

leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_yuri)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

print(f'O menor lance foi de {menor_lance} e o maior lance foi de {maior_lance}')