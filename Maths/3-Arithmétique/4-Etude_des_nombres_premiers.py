N = int(input())

def is_premier(N):
    for i in range(2,N//2 + 1):
        if N%i == 0 :
            return 'Composé'
    return 'Premier'

print(is_premier(N))