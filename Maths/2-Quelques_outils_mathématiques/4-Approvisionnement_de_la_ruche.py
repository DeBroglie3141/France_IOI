x, y, N= map(int, [input() for _ in range(3)])
s = 0

for _ in range(N):
    x2, y2 = int(input()), int(input())
    if ((x-x2)**2 + (y-y2)**2)**0.5 < 1000 :
        s += 1

print(s)