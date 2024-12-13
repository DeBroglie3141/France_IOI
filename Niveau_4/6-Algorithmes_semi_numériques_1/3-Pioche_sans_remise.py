N, a = int(input()), int(input())
b, c = N, N-a
for i in range(1, N):
   b *= i
for i in range(1, N-a):
   c *= i
print(b//c if c!=0 else b)