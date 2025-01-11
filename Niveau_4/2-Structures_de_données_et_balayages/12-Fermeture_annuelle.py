def calcul_temps_libre_max():
    
    nbUnités, nbFestivals = map(int, input().split())
    festivals = []

    for _ in range(nbFestivals):
        D, F = map(int, input().split())
        if D > F:
            festivals.append((D, nbUnités))
            festivals.append((0, F))
        else: 
            festivals.append((D, F))
    
    festivals.sort()

    festivals_finaux = [festivals[0]]
    for festival in festivals:
        if festival[0] <= festivals_finaux[-1][1]:
            festivals_finaux[-1] = (min(festival[0], festivals_finaux[-1][0]), max(festival[1], festivals_finaux[-1][1]))
        else:
            festivals_finaux.append(festival)

    trou_max = 0

    fin_truc_prec = festivals_finaux[-1][1] - nbUnités
    for i in range(len(festivals_finaux)):
        D, F = festivals_finaux[i]
        trou = (D - fin_truc_prec)
        if trou > trou_max:
            trou_max = trou
        fin_truc_prec = F
    
    return trou_max

print(calcul_temps_libre_max())