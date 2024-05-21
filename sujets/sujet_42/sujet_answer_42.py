from unittest import TestCase, main


def moyenne(tab: list[int]) -> float:
    total: int = 0
    for v in tab:
        total += v
    return total / len(tab)


def dichotomie(tab: list[int], x: int) -> bool:
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""

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


class TestSujet42(TestCase):
    def test_moyenne_case_1(self) -> None:
        self.assertEqual(moyenne([1]), 1.0)

    def test_moyenne_case_2(self) -> None:
        self.assertEqual(moyenne([1, 2, 3, 4, 5, 6, 7]), 4.0)

    def test_moyenne_case_3(self) -> None:
        self.assertEqual(moyenne([1, 2]), 1.5)

    def test_dichotomie_case_1(self) -> None:
        self.assertTrue(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))

    def test_dichotomie_case_2(self) -> None:
        self.assertFalse(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))

    def test_dichotomie_case_3(self) -> None:
        self.assertFalse(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1))

    def test_dichotomie_case_4(self) -> None:
        self.assertFalse(dichotomie([], 28))


if __name__ == "__main__":
    main()
