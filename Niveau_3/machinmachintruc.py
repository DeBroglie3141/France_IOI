import sys

def reconstituer_operations(nbCartons, relations):
    operations = []
    
    def dfs(carton):
        for dessus in relations[carton]:
            operations.append("A {}".format(dessus))
            dfs(dessus)
            operations.append("R {}".format(dessus))
    
    for carton in relations[0]:  # On commence à partir du sol (carton 0) prcq... jsp
        operations.append("A {}".format(carton))
        dfs(carton)
        operations.append("R {}".format(carton))
    
    return operations

if __name__ == "__main__":
    nbCartons = int(sys.stdin.readline().strip())
    relations = {i: [] for i in range(nbCartons + 1)}
    
    for i in range(nbCartons + 1):
        ligne = list(map(int, sys.stdin.readline().strip().split()))
        if ligne[0] > 0:
            relations[i] = ligne[1:]
    
    resultat = reconstituer_operations(nbCartons, relations)
    print("\n".join(resultat))
