N = int(input())
produit = 1

for _ in range(N):
    nombre = int(input()) % 10000
    produit = (produit * nombre) % 10000

print("{:04d}".format(produit))