from typing import Any
from unittest import TestCase, main


def nb_repetitions(elm: Any, tab: list) -> int:
    acc = 0
    for v in tab:
        if v == elm:
            acc += 1
    return acc


def binaire(n: int) -> str:
    """convertit un nombre entier a en sa representation
    binaire sous forme de chaine de caractères."""
    if n == 0:
        return "0"
    bin_n = ""
    while n > 0:
        bin_n = str(n % 2) + bin_n
        n = n // 2
    return bin_n


class TestSujet17(TestCase):
    def test_nb_repetitions_case_1(self) -> None:
        self.assertEqual(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]), 3)

    def test_nb_repetitions_case_2(self) -> None:
        self.assertEqual(nb_repetitions("A", ["B", "A", "B", "A", "R"]), 2)

    def test_nb_repetitions_case_3(self) -> None:
        self.assertEqual(nb_repetitions(12, [1, 3, 7, 21, 36, 44]), 0)

    def test_binnaire_case_base(self) -> None:
        self.assertEqual(binaire(83), "1010011")

    def test_binnaire_case_7bit(self) -> None:
        self.assertEqual(binaire(127), "1111111")

    def test_binnaire_case_zero(self) -> None:
        self.assertEqual(binaire(0), "0")


if __name__ == "__main__":
    main()
