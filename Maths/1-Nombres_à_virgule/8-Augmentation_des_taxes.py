t1, t2, prix = map(float, [input() for _ in range(3)])
print(round(prix / (100 + t1) * (100 + t2),2))