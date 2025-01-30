def force_max(L, N, points):
    force_max = float("-inf")
    somme_cumulative = [i for i in points]
    for i in range(1,N):
        somme_cumulative[i] += somme_cumulative[i-1]
    
    for i in range(N-L):
        force = somme_cumulative[i+L] - somme_cumulative[i]
        force_max = max(force_max, force)

    return force_max

L, N = map(int, input().split())
points = list(map(int, input().split()))

print(force_max(L, N, points))