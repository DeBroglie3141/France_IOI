L, l = map(int, input().split())

def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a%b)

def ppcm(a, b):
    return abs(a*b) // pgcd(a, b)

print(ppcm(L, l))