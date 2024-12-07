longueur_max = int(input())
liste = []

for i in range(longueur_max+1):
    for j in range(i):
        for k in range(j):
            if i**2 == j**2 + k**2 :
                l = [i, j, k]
                l.sort()
                liste.append(l)

liste.sort(key=lambda x : x[0])
for l in liste :
    print(*l)