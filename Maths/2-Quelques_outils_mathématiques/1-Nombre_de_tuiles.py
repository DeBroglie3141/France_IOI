F, L, H, h = map(float, [input() for _ in range(4)])
print(2 * L * ((H - h)**2 + (F/2)**2 )**0.5)