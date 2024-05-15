from unittest import TestCase, main


def moyenne(tab: list[float]) -> float:
    return sum(tab) / len(tab)


def binaire(n: int) -> str:
    """convertit un nombre entier a en sa representation
    binaire sous forme de chaine de caractères."""
    if n == 0:
        return "0"
    bin_a = ""
    while n > 0:
        bin_a = str(n % 2) + bin_a
        n = n // 2
    return bin_a


class TestSujet15(TestCase):
    def test_moyenne_case_base(self) -> None:
        self.assertAlmostEqual(moyenne([1.0, 2.0, 4.0]), 2.3333333333333335)

    def test_moyenne_case_single(self) -> None:
        self.assertAlmostEqual(moyenne([1.0]), 1.0)

    def test_binnaire_case_base(self) -> None:
        self.assertEqual(binaire(83), "1010011")

    def test_binnaire_case_7bit(self) -> None:
        self.assertEqual(binaire(127), "1111111")

    def test_binnaire_case_zero(self) -> None:
        self.assertEqual(binaire(0), "0")


if __name__ == "__main__":
    main()
