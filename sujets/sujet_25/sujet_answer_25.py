from typing import Literal
from unittest import TestCase, main


def recherche_min(tab: list[int]) -> int:
    min_i, min_v = 0, tab[0]

    for i, v in enumerate(tab):
        if v < min_v:
            min_i, min_v = i, v

    return min_i


def separe(tab: list[Literal[0, 1]]) -> list[Literal[0, 1]]:
    """Separe les 0 et les 1 dans le tableau tab"""
    gauche = 0
    droite = len(tab) - 1
    while gauche < droite:
        if tab[gauche] == 0:
            gauche = gauche + 1
        else:
            tab[gauche] = tab[droite]
            tab[droite] = 1
            droite = droite - 1
    return tab


class TestSujet25(TestCase):
    def test_recherche_min_case_1(self) -> None:
        self.assertEqual(recherche_min([5]), 0)

    def test_recherche_min_case_2(self) -> None:
        self.assertEqual(recherche_min([2, 4, 1]), 2)

    def test_recherche_min_case_3(self) -> None:
        self.assertEqual(recherche_min([5, 3, 2, 2, 4]), 2)

    def test_recherche_min_case_4(self) -> None:
        self.assertEqual(recherche_min([-1, -2, -3, -3]), 2)

    def test_separe_case_1(self) -> None:
        self.assertEqual(separe([1, 0, 1, 0, 1, 0, 1, 0]), [0, 0, 0, 0, 1, 1, 1, 1])

    def test_separe_case_2(self) -> None:
        self.assertEqual(
            separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]),
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        )


if __name__ == "__main__":
    main()
