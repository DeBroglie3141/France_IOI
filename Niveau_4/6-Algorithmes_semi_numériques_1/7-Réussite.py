N = int(input())

def is_prime(n):
    if all(n%i != 0 for i in range(2,int(n**0.5)+1)):
        return str(n) + '\n'
    else:
        return ''

for n in range(N):
    print(is_prime(n), end='')