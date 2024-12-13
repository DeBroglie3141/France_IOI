A = int(input())
N = 1
liste = []
while N <= A**0.5:
   if (A%N == 0):
      if N not in liste:
        print(N)
        liste.append(N)
      if A//N not in liste :
         print(A//N)
         liste.append(A//N)
   N += 1