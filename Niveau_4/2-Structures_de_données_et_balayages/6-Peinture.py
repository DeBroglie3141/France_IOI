nbQuantites, N = map(int, input().split())
quantites = list(map(int, input().split()))

N = N // 2

def main():
    for quantite in quantites:
        if N == quantite:
            return 'OUI'
    return 'NON'            
        
print(main())