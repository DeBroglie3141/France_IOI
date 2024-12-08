h, l = int(input()), int(input())

for i in range(h):
    for j in range(l):
        print('O' if (j+i)%2 == 0 else 'X', end='')
    print()

