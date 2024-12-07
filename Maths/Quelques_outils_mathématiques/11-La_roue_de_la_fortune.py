nb_zone = int(input())
print(nb_zone%24 if nb_zone >= 0 else 24 - ((-nb_zone)%24))