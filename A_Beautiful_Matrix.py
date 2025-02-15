matrice = [list(map(int, input().split())) for _ in range(5)]
    
def truc():    
    for i in range(5):
        for j in range(5):
            if matrice[i][j] == 1:
                return i, j
            
i, j = truc()

print(abs(2-i) + abs(2 - j))