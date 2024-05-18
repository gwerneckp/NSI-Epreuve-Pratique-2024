from unittest import TestCase, main

adj = [[1, 2], [2], [0], [0]]

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(...): 
        if s[i] == chiffre:
            compte = ... 
        else:
            resultat += ... + ... 
            chiffre = ... 
            ...
    lecture_... = ... + ... 
    resultat += lecture_chiffre
    return resultat

class TestSujet48(TestCase):
    def test_voisins_entrants_case_1(self) -> None:
        self.assertEqual(voisins_entrants([[1, 2], [2], [0], [0]], 0), [2, 3])

    def test_voisins_entrants_case_2(self) -> None:
        self.assertEqual(voisins_entrants([[1, 2], [2], [0], [0]], 1), [0])

    def test_nombre_suivant_case_1(self) -> None:
        self.assertEqual(nombre_suivant('1211'), '111221')

    def test_nombre_suivant_case_2(self) -> None:
        self.assertEqual(nombre_suivant('311'), '1321')

if __name__ == "__main__":
    main()