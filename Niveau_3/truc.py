nA = int(input())
listeA = list(map(int, input().split()))
nB = int(input())
listeB = list(map(int, input().split()))
truc = 0
listeB.sort()
n = 0

while 2**truc < nB:
    truc += 1
truc += 1
def dicho(a):
    i = nB 
    j = 0
    for _ in range(truc):  
        machin = (i+j) // 2
        if listeB[machin] > a:
            i = machin
        elif listeB[machin] < a:
            j = machin
        else:
            return True
    return False


for a in listeA:
    if dicho(a):
        n += 1

print(n)