from unittest import TestCase, main

def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [...] 
    for i in range(...): 
        ligne_suiv.append(...) 
    ligne_suiv.append(...) 
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(...): 
        ligne_k = ... 
        triangle.append(ligne_k)
    return triangle

class TestSujet29(TestCase):
    def test_ligne_suivante_case_1(self) -> None:
        self.assertEqual(ligne_suivante([1, 3, 3, 1]), [1, 4, 6, 4, 1])

    def test_ligne_suivante_case_2(self) -> None:
        self.assertEqual(pascal(2), [[1], [1, 1], [1, 2, 1]])

    def test_ligne_suivante_case_3(self) -> None:
        self.assertEqual(pascal(3), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

if __name__ == "__main__":
    main()