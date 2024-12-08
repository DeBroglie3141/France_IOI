N = 1000

def truc(N):
    liste = [n for n in range(2, N) if all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
    return liste

for elem in truc(N) :
    print(elem)