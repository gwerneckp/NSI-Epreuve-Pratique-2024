from unittest import TestCase, main


def nbr_occurences(chaine: str) -> dict[str, int]:
    res: dict[str, int] = {}
    for c in chaine:
        if res.get(c):
            res[c] = res[c] + 1
            continue
        res[c] = 1
    return res


def fusion(tab1: list[int], tab2: list[int]) -> list[int]:
    """Fusionne deux tableaux triés et renvoie le nouveau tableau trié."""
    n1 = len(tab1)
    n2 = len(tab2)
    tab12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if tab1[i1] < tab2[i2]:
            tab12[i] = tab1[i1]
            i1 += 1
        else:
            tab12[i] = tab2[i2]
            i2 += 1
        i += 1
    while i1 < n1:
        tab12[i] = tab1[i1]
        i1 = i1 + 1
        i += 1
    while i2 < n2:
        tab12[i] = tab2[i2]
        i2 = i2 + 1
        i += 1
    return tab12


class TestSujet34(TestCase):
    def test_count_chars_case_1(self) -> None:
        self.assertEqual(
            nbr_occurences("bonjour"), {"b": 1, "o": 2, "n": 1, "j": 1, "u": 1, "r": 1}
        )

    def test_count_chars_case_2(self) -> None:
        self.assertEqual(nbr_occurences("Bébé"), {"B": 1, "é": 2, "b": 1})

    def test_count_chars_case_3(self) -> None:
        self.assertEqual(
            nbr_occurences("Hello world !"),
            {"H": 1, "e": 1, "l": 3, "o": 2, " ": 2, "w": 1, "r": 1, "d": 1, "!": 1},
        )

    def test_fusion_case_1(self) -> None:
        self.assertEqual(fusion([1, 6, 10], [0, 7, 8, 9]), [0, 1, 6, 7, 8, 9, 10])


if __name__ == "__main__":
    main()
