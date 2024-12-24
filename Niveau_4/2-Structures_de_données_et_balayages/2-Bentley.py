def main():
  N = int(input())
  elements = list(map(int, input().split()))
  somme_actuelle = 0
  somme_max = 0
  for i in range(N):
    somme_actuelle = max(elements[i], somme_actuelle + elements[i])
    somme_max = max(somme_max, somme_actuelle)
  print(somme_max)

main()