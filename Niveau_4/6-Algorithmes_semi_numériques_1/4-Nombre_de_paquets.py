N, P = int(input()), int(input())

def factorielle(n):
    return 1 if n==0 else n*factorielle(n-1)

def binome(a, b):
    return factorielle(a)//(factorielle(b)*factorielle(a-b))

print(binome(N, P))