def choisir_limite(S, spectacles):
    spectacles.sort()
    
    meilleure_limite = 0
    meilleure_moyenne = 0
    somme_frequentation = 0
    nombre_spectacles = 0
    
    for i in range(S):
        duree, frequentation = spectacles[i]
        somme_frequentation += frequentation
        nombre_spectacles += 1
        
        moyenne = somme_frequentation / nombre_spectacles
        
        if moyenne > meilleure_moyenne or (moyenne == meilleure_moyenne and duree > meilleure_limite):
            meilleure_moyenne = moyenne
            meilleure_limite = duree
    
    return meilleure_limite

S = int(input())
spectacles = []
for _ in range(S):
    D, F = map(int, input().split())
    spectacles.append((D, F))

print(choisir_limite(S, spectacles))