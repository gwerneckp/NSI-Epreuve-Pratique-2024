from unittest import TestCase, main


def couples_consecutifs(tab: list[int]) -> list[tuple[int, int]]:
    res = []
    for i in range(len(tab) - 1):
        if tab[i] == tab[i + 1] - 1:
            res.append((tab[i], tab[i + 1]))

    return res


def colore_comp1(M: list[list[int]], i: int, j: int, val: int) -> None:
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i - 1 >= 0:  # propage en haut
        colore_comp1(M, i - 1, j, val)
    if i + 1 < len(M):  # propage en bas
        colore_comp1(M, i + 1, j, val)
    if j - 1 >= 0:  # propage à gauche
        colore_comp1(M, i, j - 1, val)
    if j + 1 < len(M[0]):  # propage à droite
        colore_comp1(M, i, j + 1, val)


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

    def test_colore_comp1(self) -> None:
        M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
        colore_comp1(M, 2, 1, 3)
        self.assertEqual(M, [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]])


if __name__ == "__main__":
    main()
