from unittest import TestCase, main


def indices_maxi(tab: list[int]) -> tuple[int, list[int]]:
    maxv = tab[0]
    indices: list[int] = [0]
    for i in range(1, len(tab)):
        if tab[i] == maxv:
            indices.append(i)
            continue

        if tab[i] > maxv:
            maxv = tab[i]
            indices = [i]

    return (maxv, indices)


def renverse(pile: list) -> list:
    """renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile."""
    pile_inverse = []
    while pile != []:
        pile_inverse.append(pile.pop())
    return pile_inverse


def positifs(pile: list[int]) -> list[int]:
    """renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile."""
    pile_positifs = []
    while pile != []:
        value = pile.pop()
        if value >= 0:
            pile_positifs.append(value)
    return renverse(pile_positifs)


class TestSujet38(TestCase):
    def test_indices_maxi_case_1(self) -> None:
        self.assertEqual(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]), (9, [3, 8]))

    def test_indices_maxi_case_2(self) -> None:
        self.assertEqual(indices_maxi([7]), (7, [0]))

    def test_pile_inverse_case_1(self) -> None:
        self.assertEqual(renverse([1, 2, 3]), [3, 2, 1])

    def test_renverse_case_1(self) -> None:
        self.assertEqual(renverse([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_renverse_case_empty(self) -> None:
        self.assertEqual(renverse([]), [])

    def test_renverse_case_2(self) -> None:
        self.assertEqual(positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]), [0, 5, 4, 10, 9])

    def test_renverse_case_3(self) -> None:
        self.assertEqual(positifs([-2]), [])


if __name__ == "__main__":
    main()
