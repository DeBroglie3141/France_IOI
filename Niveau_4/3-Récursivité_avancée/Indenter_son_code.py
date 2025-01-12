truc = input()
import sys
sys.setrecursionlimit(1000000)
def machin(truc, nb_tabulations):
    if truc == "":
        return
    if truc[0] == '{':
        print('\t' * nb_tabulations + '{')
        machin(truc[1:], nb_tabulations + 1)
    else:
        print('\t' * (nb_tabulations - 1) + '}')
        machin(truc[1:], nb_tabulations - 1)

nb_tabulations = 0
machin(truc, nb_tabulations)