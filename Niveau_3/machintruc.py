from collections import deque

L, C, D = map(int, input().split())
laby = [list(map(int, input().split())) for _ in range(L)]

mvt = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def trouver_chemin():
    queue = deque([(0, 0)]) 
    chemin = []
    visited = set()
    
    while queue:
        l, c = queue.popleft()
        chemin.append((l, c))
        visited.add((l, c))
        
        for dy, dx in mvt:
            nl, nc = l + dy, c + dx
            if 0 <= nl < L and 0 <= nc < C and laby[nl][nc] == 0 and (nl, nc) not in visited:
                queue.append((nl, nc))
                visited.add((nl, nc)) 

    return chemin

chemin = trouver_chemin()

for i in range(D, len(chemin), D+1):
    print(chemin[i][0], chemin[i][1])
