from collections import defaultdict

def analyse(N, A):
    g = defaultdict(list)



N, A = map(int, input().split())
chemins = [tuple(map(int, input().split())) for _ in range(A)]
