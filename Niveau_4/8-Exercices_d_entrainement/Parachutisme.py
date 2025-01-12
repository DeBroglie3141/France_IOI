D, L, N = map(int, input().split())
lacs = []
for _ in range(L):
    y_min, x_min, y_max, x_max = map(int, input().split())
    lacs.append((y_min, x_min, y_max, x_max))

def test_point():
    for lac in lacs:
        y_min, x_min, y_max, x_max = lac
        if (y_min <= y <= y_max) and (x_min <= x <= x_max):
            return 1
    return 0

for _ in range(N):
    y, x = map(int, input().split())
    print(test_point())

