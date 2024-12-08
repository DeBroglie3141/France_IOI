nbCrapauds, nbCouleuvres, nbAnnees = map(int, [input() for _ in range(3)])

for _ in range(nbAnnees):
    print(nbCrapauds, nbCouleuvres)
    nbCrapauds, nbCouleuvres = nbCrapauds*3 - 2*nbCouleuvres, nbCrapauds - nbCouleuvres