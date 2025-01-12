L, C = map(int, input().split())
total = 0

for _ in range(L):
   ligne = input()
   total += ligne.count('#')

print(total)