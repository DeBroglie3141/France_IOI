D = int(input())
mots_dico = [input() for _ in range(D)]
N = int(input())
mots_tapes = [input() for _ in range(N)]

def test_mot(mot_dico):
    for i in range(N):
        if mot_dico[i] not in mots_tapes[i]:
            return False
    return True

for mot_dico in mots_dico:
    if len(mot_dico) != N:
        continue
    if test_mot(mot_dico):
        print(mot_dico)
        break
