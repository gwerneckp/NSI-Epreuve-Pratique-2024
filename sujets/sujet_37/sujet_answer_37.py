from typing import Literal
from unittest import TestCase, main


def moyenne(tab: list[int]) -> float | None:
    return sum(tab) / len(tab) if len(tab) > 0 else None


def tri(tab: list[Literal[0, 1]]) -> None:
    """tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche"""
    i = 0  # premier indice de la zone non triée
    j = len(tab) - 1  # dernier indice de la zone non triée
    while i < j:
        if tab[i] == 0:
            i = i + 1
        else:
            valeur = tab[j]
            tab[j] = 1
            tab[i] = valeur
            j = j - 1


class TestSujet37(TestCase):
    def test_moyenne_case_1(self) -> None:
        assert (res := moyenne([5, 3, 8])) is not None
        self.assertAlmostEqual(res, 5.333333333333333)

    def test_moyenne_case_2(self) -> None:
        self.assertEqual(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.5)

    def test_moyenne_case_3(self) -> None:
        self.assertIsNone(moyenne([]))

    def test_tri(self) -> None:
        tab: list[Literal[0, 1]] = [0, 1, 0, 1, 0, 1, 0, 1, 0]
        tri(tab)
        self.assertListEqual(tab, [0, 0, 0, 0, 0, 1, 1, 1, 1])


if __name__ == "__main__":
    main()
