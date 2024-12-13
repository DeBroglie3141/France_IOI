txt_code = input()
a, b, c, d = map(int, [input() for _ in range(4)])
txt = ''
denominateur = (b*c - a*d)
for i in range(len(txt_code) // 2):
    y1, y2 = ord(txt_code[2*i]) - ord("A"), ord(txt_code[2*i + 1]) - ord("A")
    x1, x2 = ((b*y2 - d*y1)%26) // denominateur, ((c*y1 - a*y2)%26) // denominateur
    print(chr(x1%26 + ord("A")) + chr(x2%26 + ord("A")), end='')


#pas abouti !!