from unittest import TestCase, main


def multiplication(n1: int, n2: int) -> float:
    n1, n2 = (-n1, -n2) if n1 < 0 else (n1, n2)
    res: int = 0
    for _ in range(n1):
        res += n2
    return res


def dichotomie(tab: list[int], x: int) -> bool:
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False


class TestSujet31(TestCase):
    def test_multiplication_case_1(self) -> None:
        self.assertEqual(multiplication(3, 5), 15)

    def test_multiplication_case_2(self) -> None:
        self.assertEqual(multiplication(-4, -8), 32)

    def test_multiplication_case_3(self) -> None:
        self.assertEqual(multiplication(-2, 6), -12)

    def test_multiplication_case_4(self) -> None:
        self.assertEqual(multiplication(-2, 0), 0)

    def test_dichotomie_case_1(self) -> None:
        self.assertTrue(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))

    def test_dichotomie_case_2(self) -> None:
        self.assertFalse(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))


if __name__ == "__main__":
    main()
