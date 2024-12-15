B, len_N1, len_N2 = map(int, input().split())
chiffres_N1  = list(map(int, input().split()))
chiffres_N2  = list(map(int, input().split()))
chiffres_N1.reverse()
chiffres_N2.reverse()
somme = []

if len_N1 <= len_N2 :
    liste_max = chiffres_N2
    len_min = len_N1
    len_max = len_N2
else:
    liste_max = chiffres_N1
    len_min = len_N2
    len_max = len_N1

reste = 0

for i in range(len_min):
    n = (chiffres_N1[i] + chiffres_N2[i])%B + reste
    somme.append(n%B)
    reste = (chiffres_N1[i] + chiffres_N2[i] + reste)//B

for i in range(len_min, len_max):
    n = liste_max[i]%B + reste
    somme.append(n%B)
    reste = (liste_max[i] + reste)//B

while reste != 0:
    n = reste%B
    somme.append(n)
    reste = reste//B

somme.reverse()

print(*somme)