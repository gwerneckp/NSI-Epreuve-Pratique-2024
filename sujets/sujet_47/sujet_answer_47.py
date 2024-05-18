from unittest import TestCase, main

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n'est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for ... in tab:
        if element != '+' ... element != '*':
            p.empiler(...)
        else:
            if element == ...:
                resultat = ... + ...
            else:
                resultat = ...
            p.empiler(...)
    return ...

class TestSujet47(TestCase):
    def test_max_dico_case_1(self) -> None:
        self.assertEqual(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}), ('Ada', 201))

    def test_max_dico_case_2(self) -> None:
        self.assertEqual(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}), ('Alan', 222))

    def test_eval_expression_case_1(self) -> None:
        self.assertEqual(eval_expression([2, 3, '+', 5, '*']), 25)

    def test_eval_expression_case_2(self) -> None:
        self.assertEqual(eval_expression([1, 2, '+', 3, '*']), 9)

    def test_eval_expression_case_3(self) -> None:
        self.assertEqual(eval_expression([1, 2, 3, '+', '*']), 5)

if __name__ == "__main__":
    main()