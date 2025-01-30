alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = int(input())
lignes = [[char for char in ligne] for ligne in [input() for _ in range(N)]]
mot = ''

for ligne in lignes:
    n = ligne.count('O')
    for _ in range(n):
        index = ligne.index('O')
        ligne[index] = 'X'
        mot += alphabet[index]

print(mot)