from unittest import TestCase, main

class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = ... 
    tab_ins[...] = ... 
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = ... 
    return tab_ins

class TestSujet41(TestCase):
    def test_hauteur_case_1(self) -> None:
        self.assertEqual(hauteur(a), 2)

    def test_hauteur_case_2(self) -> None:
        self.assertEqual(taille(a), 4)

    def test_hauteur_case_3(self) -> None:
        self.assertEqual(hauteur(None), -1)

    def test_hauteur_case_4(self) -> None:
        self.assertEqual(taille(None), 0)

    def test_hauteur_case_5(self) -> None:
        self.assertEqual(hauteur(Noeud(1, None, None)), 0)

    def test_hauteur_case_6(self) -> None:
        self.assertEqual(taille(Noeud(1, None, None)), 1)

    def test_ajoute_case_1(self) -> None:
        self.assertEqual(ajoute(1, 4, [7, 8, 9]), [7, 4, 8, 9])

    def test_ajoute_case_2(self) -> None:
        self.assertEqual(ajoute(3, 4, [7, 8, 9]), [7, 8, 9, 4])

    def test_ajoute_case_3(self) -> None:
        self.assertEqual(ajoute(0, 4, [7, 8, 9]), [4, 7, 8, 9])

if __name__ == "__main__":
    main()