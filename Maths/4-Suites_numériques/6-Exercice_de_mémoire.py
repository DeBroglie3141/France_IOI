N = int(input())
a, b = 1, 1

for _ in range(N):
    print(a)
    a, b = b, a + b
