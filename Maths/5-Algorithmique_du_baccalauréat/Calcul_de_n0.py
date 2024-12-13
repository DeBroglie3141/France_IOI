p = int(input())
n = 0
def u(n):
    return 3**n + n - 1
while u(n) < 10**p:
    n += 1
print(n)