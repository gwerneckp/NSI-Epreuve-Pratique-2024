from unittest import TestCase, main


def couples_consecutifs(tab):
    pass


def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i - 1 >= 0:  # propage en haut
        colore_comp1(M, i - 1, j, val)
    if ... < len(M):  # propage en bas
        colore_comp1(M, ..., j, val)
    if ...:  # propage à gauche
        colore_comp1(M, ..., ..., val)
    if ...:  # propage à droite
        ...


class TestSujet27(TestCase):
    def test_couples_consecutifs_case_1(self) -> None:
        self.assertEqual(couples_consecutifs([1, 4, 3, 5]), [])

    def test_couples_consecutifs_case_2(self) -> None:
        self.assertEqual(couples_consecutifs([1, 4, 5, 3]), [(4, 5)])

    def test_couples_consecutifs_case_3(self) -> None:
        self.assertEqual(couples_consecutifs([1, 1, 2, 4]), [(1, 2)])

    def test_couples_consecutifs_case_4(self) -> None:
        self.assertEqual(couples_consecutifs([7, 1, 2, 5, 3, 4]), [(1, 2), (3, 4)])

    def test_couples_consecutifs_case_5(self) -> None:
        self.assertEqual(
            couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]), [(1, 2), (2, 3), (-5, -4)]
        )


if __name__ == "__main__":
    main()
