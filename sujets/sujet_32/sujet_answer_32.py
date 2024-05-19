from typing import Literal
from unittest import TestCase, main


def ou_exclusif(tab1: list[Literal[0, 1]], tab2: list[Literal[0, 1]]) -> list[int]:
    return [tab1[i] ^ tab2[i] for i in range(len(tab1))]


class Carre:
    def __init__(self, liste: list[int], n: int) -> None:
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]

    def affiche(self) -> None:
        """Affiche un carré"""
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i: int) -> int:
        """Calcule la somme des valeurs de la ligne i"""
        somme = 0
        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def somme_col(self, j: int) -> int:
        """Calcule la somme des valeurs de la colonne j"""
        somme = 0
        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def est_semimagique(self) -> bool:
        s = self.somme_ligne(0)

        # test de la somme de chaque ligne
        for i in range(self.ordre):
            if self.somme_ligne(i) != s:
                return False

        # test de la somme de chaque colonne
        for j in range(self.ordre):
            if self.somme_col(j) != s:
                return False

        return True


class TestSujet32(TestCase):
    def test_ou_exclusif_case_1(self) -> None:
        self.assertEqual(
            ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]),
            [1, 1, 0, 1, 1, 0, 0, 1],
        )

    def test_ou_exclusif_case_2(self) -> None:
        self.assertEqual(ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]), [1, 1, 1, 0])

    def test_carre_case_1(self) -> None:
        lst_c3 = [3, 4, 5, 4, 4, 4, 5, 4, 3]
        c3 = Carre(lst_c3, 3)
        self.assertTrue(c3.est_semimagique())


if __name__ == "__main__":
    main()
