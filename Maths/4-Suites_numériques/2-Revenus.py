capital, bénéfice_mensuel, nb_mois = map(int, [input() for _ in range(3)])

for _ in range(nb_mois):
    print(capital)
    capital += bénéfice_mensuel