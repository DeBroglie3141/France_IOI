nbCibles, gains = int(input()), list(map(int, input().split()))
nbLots, valeurs = int(input()), list(map(int, input().split()))
valeurs.append(float("inf"))

def truc(valeurs, valeur_prec):
    valeur_lot = valeurs[0]
    if gain >= valeur_lot:
        return truc(valeurs[1:], valeur_lot)
    else:
        return valeur_prec

min_lot = 0
for gain in gains:
    max_lot = truc(valeurs, min_lot)
    print(max_lot, end=" ")
    min_lot = max_lot