def calculer_temps_total(N, intervalles):
    intervalles.sort()
    
    intervalles_fusionnes = []
    
    for intervalle in intervalles:
        if not intervalles_fusionnes:
            intervalles_fusionnes.append(intervalle)
        else:
            dernier_intervalle = intervalles_fusionnes[-1]
            if intervalle[0] <= dernier_intervalle[1]:
                nouveau_debut = dernier_intervalle[0]
                nouveau_fin = max(dernier_intervalle[1], intervalle[1])
                intervalles_fusionnes[-1] = (nouveau_debut, nouveau_fin)
            else:
                intervalles_fusionnes.append(intervalle)
    
    temps_total = 0
    for intervalle in intervalles_fusionnes:
        temps_total += intervalle[1] - intervalle[0]
    
    return temps_total

N = int(input())
intervalles = []
for _ in range(N):
    D, F = map(int, input().split())
    intervalles.append((D, F))

print(calculer_temps_total(N, intervalles))