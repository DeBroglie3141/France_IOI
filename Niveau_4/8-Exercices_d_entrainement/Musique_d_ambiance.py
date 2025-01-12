N = int(input())
enregistrement = list(map(int, input().split()))
enregistrement.append(0)

n_max = 0
deja_vu = set()

for i in range(N+1):
    if enregistrement[i] == 0:
        n_max = max(n_max, len(deja_vu))
        deja_vu = set()
    else:
        if enregistrement[i] not in deja_vu:
            deja_vu.add(enregistrement[i])
print(n_max)