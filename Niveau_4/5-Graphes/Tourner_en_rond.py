from collections import defaultdict, deque

def analyse(N, A, sentiers):
    g = defaultdict(list)
    for a, b in sentiers:
        g[a].append(b)

    truc = [False] * (N+1)

    def bfs(s):
        q = deque([s])
        truc[s] = True
        while q:
            n = q.popleft()
            if n == s:
                return True
            for voisin in g[n]:
                if not truc[voisin]:
                    truc[voisin] = True
                    q.append(voisin)
        return False
    
    for i in range(1, N+1):
        if bfs(i):
            return 'OUI'
    return 'NON'



N, A = map(int, input().split())
sentiers = [tuple(map(int, input().split())) for _ in range(A)]
print(analyse(N, A, sentiers))