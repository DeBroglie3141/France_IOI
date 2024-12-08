nb_élèves, nb_classes = int(input()), int(input())

classes = [0] * nb_classes

for i in range(nb_élèves):
    classes[i%nb_classes] += 1

for classe in classes :
    print(classe)