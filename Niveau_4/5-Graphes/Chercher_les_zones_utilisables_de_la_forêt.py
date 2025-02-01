from collections import defaultdict, deque
def analyse(N, A, chemins):
    g = defaultdict(list)
    for u, v, _ in chemins:
        g[u].append(v)
        g[v].append(u)
    
    vis = [False] * (N + 1)
    def bfs(s):
        q = deque([s])
        vis[s] = True
        taille = 0
        while q:
            n = q.popleft()
            taille += 1
            for voisin in g[n]:
                if not vis[voisin]:
                    vis[voisin] = True
                    q.append(voisin)
        return taille
    
    zones = 0
    max_taille = 0
    
    for i in range(1, N + 1):
        if not vis[i]:
            zones += 1
            max_taille = max(max_taille, bfs(i))
    
    return zones, max_taille
N, A = map(int, input().split())
chemins = [tuple(map(int, input().split())) for _ in range(A)]
res = analyse(N, A, chemins)
print(res[0], res[1])