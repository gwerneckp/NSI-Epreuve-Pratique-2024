from unittest import TestCase, main
from typing import Any

# from functools import reduce


def maximum_tableau(tab: list[int]) -> int:
    # return reduce(lambda new, acc: new if new > acc else acc, tab, float("-inf"))
    max_v = tab[0]
    for v in tab[1::]:
        if v > max_v:
            max_v = v

    return max_v


class Pile:
    """Classe définissant une structure de pile."""

    def __init__(self) -> None:
        self.contenu: list[Any] = []

    def est_vide(self) -> bool:
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v: Any) -> None:
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self) -> Any:
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n'est pas vide. Produit une erreur sinon.
        """
        return self.contenu.pop()


def bon_parenthesage(ch: str) -> bool:
    """Renvoie un booléen indiquant si la chaîne ch
    est bien parenthésée"""
    p = Pile()
    for c in ch:
        if c == "(":
            p.empiler(c)
        elif c == ")":
            if p.est_vide():
                return False
            p.depiler()
    return p.est_vide()


class TestSujet03(TestCase):
    def test_maximum_tableau_1(self) -> None:
        self.assertEqual(maximum_tableau([98, 12, 104, 23, 131, 9]), 131)

    def test_maximum_tableau_2(self) -> None:
        self.assertEqual(maximum_tableau([-27, 24, -3, 15]), 24)

    def test_parenthesis_check_1(self) -> None:
        self.assertTrue(bon_parenthesage("((()())(()))"))

    def test_parenthesis_check_2(self) -> None:
        self.assertFalse(bon_parenthesage("())(()"))

    def test_parentesis_check_3(self) -> None:
        self.assertFalse(bon_parenthesage("(())(()"))


if __name__ == "__main__":
    main()
