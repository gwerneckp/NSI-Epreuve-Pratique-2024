from unittest import TestCase, main


def renverse(mot: str) -> str:
    return mot[::-1]


def crible(n: int) -> list[int]:
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = 2 * i
            while multiple < n:
                tab[multiple] = False
                multiple += i
    return premiers


class TestSujet33(TestCase):
    def test_renverse_case_1(self) -> None:
        self.assertEqual(renverse(""), "")

    def test_renverse_case_2(self) -> None:
        self.assertEqual(renverse("abc"), "cba")

    def test_renverse_case_3(self) -> None:
        self.assertEqual(renverse("informatique"), "euqitamrofni")

    def test_crible_case_1(self) -> None:
        self.assertEqual(crible(40), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])

    def test_crible_case_2(self) -> None:
        self.assertEqual(crible(5), [2, 3])


if __name__ == "__main__":
    main()
