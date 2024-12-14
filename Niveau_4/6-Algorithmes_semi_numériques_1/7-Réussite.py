def eratosthene(N):
    is_prime = [True] * (N + 1)
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, N + 1, i):
                is_prime[multiple] = False
    return [x for x in range(N + 1) if is_prime[x]]
N = int(input())
primes = eratosthene(N)
for elem in primes:
    print(elem)