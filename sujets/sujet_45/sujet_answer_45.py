from unittest import TestCase, main

def rendu_monnaie(somme_due, somme_versee):
    '''Renvoie la liste des pièces à rendre pour rendre la monnaie
    lorsqu'on doit rendre somme_versee - somme_due'''
    rendu = ... 
    a_rendre = ... 
    i = len(pieces) - 1
    while a_rendre > ...: 
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(...) 
        a_rendre = ... 
    return rendu

class TestSujet45(TestCase):
    def test_compte_occurrences_case_1(self) -> None:
        self.assertEqual(compte_occurrences(5, []), 0)

    def test_compte_occurrences_case_2(self) -> None:
        self.assertEqual(compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]), 1)

    def test_compte_occurrences_case_3(self) -> None:
        self.assertEqual(compte_occurrences('a', ['a','b','c','a','d','e','a']), 3)

    def test_rendu_monnaie_case_1(self) -> None:
        self.assertEqual(rendu_monnaie(700, 700), [])

    def test_rendu_monnaie_case_2(self) -> None:
        self.assertEqual(rendu_monnaie(102, 500), [200, 100, 50, 20, 20, 5, 2, 1])

if __name__ == "__main__":
    main()