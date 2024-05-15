from unittest import TestCase, main


def multiplication(a: int, b: int) -> int:
    res = 0
    n, inc = (a, b) if a >= 0 else (-a, -b)

    for _ in range(n):
        res += inc

    return res


def chercher(tab: list[int], x: int, i: int, j: int) -> int | None:
    """Renvoie l'indice de x dans tab, si x est dans tab,
    None sinon.
    On suppose que tab est trié dans l'ordre croissant."""
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x:
        return chercher(tab, x, m + 1, j)
    elif tab[m] > x:
        return chercher(tab, x, i, m - 1)
    else:
        return m


class TestSujet18(TestCase):
    def test_multiplication_case_1(self) -> None:
        self.assertEqual(multiplication(3, 5), 15)

    def test_multiplication_case_2(self) -> None:
        self.assertEqual(multiplication(-4, -8), 32)

    def test_multiplication_case_3(self) -> None:
        self.assertEqual(multiplication(-2, 6), -12)

    def test_multiplication_case_4(self) -> None:
        self.assertEqual(multiplication(-2, 0), 0)

    def test_chercher_case_base_1(self) -> None:
        self.assertEqual(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5), 4)

    def test_chercher_case_base_2(self) -> None:
        self.assertEqual(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5), 2)

    def test_chercher_case_null_1(self) -> None:
        self.assertIsNone(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))

    def test_chercher_case_null_2(self) -> None:
        self.assertIsNone(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))


if __name__ == "__main__":
    # chercher([1, 2, 3], 1, 0, 2)
    # chercher([1, 2, 3], 1, 0, 2)
    chercher([1, 5, 6, 6, 9, 12], 7, 0, 5)
    main()
