N, n = int(input()), 0
for _ in range(N):
    truc = input()
    if truc == "++X" or truc == "X++":
        n += 1
    else:
        n -= 1
print(n)