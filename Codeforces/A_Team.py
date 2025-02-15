N = int(input())
n = 0
for _ in range(N):
    a = list(map(int, input().split()))
    if sum(a) >= 2:
        n += 1
print(n)