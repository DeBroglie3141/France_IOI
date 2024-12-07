truc = float(input())

if truc == 0 :
   print(0)
elif truc == 60 :
   print(45)
else :
   print(int(truc // 60 + 1) * 45)