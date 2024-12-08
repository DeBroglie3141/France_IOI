capacité, nb_élèves = int(input()), int(input())
print(nb_élèves//capacité if nb_élèves%capacité == 0 else nb_élèves//capacité + 1)