import sys

def main():
   N, R = map(int, sys.stdin.readline().split())
   periodes = [0] * (N + 1)
   somme = 0
   for j, n in enumerate(sys.stdin.readline().split(), 1):
      somme += int(n)
      periodes[j] = somme
   
   for i in range(R):
      D, F = map(int, sys.stdin.readline().split())
      sys.stdout.write(str(periodes[F] - periodes[D - 1]) + "\n")
main()