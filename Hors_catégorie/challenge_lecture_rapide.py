import sys

# Lire toutes les entrées en une seule fois
inputs = sys.stdin.read().splitlines()

# Convertir les entrées en entiers et calculer la somme
s = sum(map(int, inputs[1:]))

print(s)
