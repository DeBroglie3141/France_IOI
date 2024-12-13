txt = input()
x1, x2 = ord(txt[0]) - ord("A"), ord(txt[1]) - ord("A")
y1, y2 = 11*x1 + 3*x2, 7*x1 + 4*x2
print(chr(y1%26 + ord("A")) + chr(y2%26 + ord("A")))