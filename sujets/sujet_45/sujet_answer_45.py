from typing import Any
from unittest import TestCase, main


def compte_occurrences(x: Any, tab: list) -> int:
    count = 0
    for v in tab:
        if v == x:
            count += 1
    return count


pieces = [1, 2, 5, 10, 20, 50, 100, 200]


def rendu_monnaie(somme_due: int, somme_versee: int) -> list[int]:
    """Renvoie la liste des pièces à rendre pour rendre la monnaie
    lorsqu'on doit rendre somme_versee - somme_due"""
    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0:
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(pieces[i])
        a_rendre = a_rendre - pieces[i]
    return rendu


class TestSujet45(TestCase):
    def test_compte_occurrences_case_1(self) -> None:
        self.assertEqual(compte_occurrences(5, []), 0)

    def test_compte_occurrences_case_2(self) -> None:
        self.assertEqual(compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]), 1)

    def test_compte_occurrences_case_3(self) -> None:
        self.assertEqual(
            compte_occurrences("a", ["a", "b", "c", "a", "d", "e", "a"]), 3
        )

    def test_rendu_monnaie_case_1(self) -> None:
        self.assertEqual(rendu_monnaie(700, 700), [])

    def test_rendu_monnaie_case_2(self) -> None:
        self.assertEqual(rendu_monnaie(102, 500), [200, 100, 50, 20, 20, 5, 2, 1])


if __name__ == "__main__":
    main()
