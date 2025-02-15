_, k = map(int, input().split())
scores = list(map(int, input().split()))
limite = scores[k-1]
n = 0

for score in scores:
    if (score > 0) and (score >= limite):
        n += 1
    else:
        pass
print(n)
