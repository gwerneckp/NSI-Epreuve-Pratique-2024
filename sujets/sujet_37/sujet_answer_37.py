from unittest import TestCase, main

def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = ... # premier indice de la zone non triée 
    j = ... # dernier indice de la zone non triée 
    while i < j:
        if tab[i] == 0:
            i = ... 
        else:
            valeur = ... 
            tab[j] = ... 
            ...
            j = ...

>>> tab = [0,1,0,1,0,1,0,1,0]
>>> tri(tab)
>>> tab
[0, 0, 0, 0, 0, 1, 1, 1, 1]

class TestSujet37(TestCase):
    def test_moyenne_case_1(self) -> None:
        self.assertEqual(moyenne([5,3,8]), 5.333333333333333)

    def test_moyenne_case_2(self) -> None:
        self.assertEqual(moyenne([1,2,3,4,5,6,7,8,9,10]), 5.5)

    def test_moyenne_case_3(self) -> None:
        self.assertEqual(moyenne([]), # Comportement différent suivant le traitement proposé.)

if __name__ == "__main__":
    main()