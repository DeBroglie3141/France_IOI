L, l = map(int, input().split())

def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a%b)
    
print(pgcd(L, l))