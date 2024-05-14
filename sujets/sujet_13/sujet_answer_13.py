from unittest import TestCase, main


def recherche(elt: int, tab: list[int]) -> int | None:
    for i in range(len(tab)):
        if tab[i] == elt:
            return i

    return None


def insere(tab: list[int], a: int) -> list[int]:
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [a] + tab  # nouveau tableau contenant a
    # suivi des éléments de tab
    i = 0
    # while i < len(tab_a) - 1 ce qui revient a len(tab)
    while i < len(tab) and a > tab_a[i + 1]:
        tab_a[i] = tab_a[i + 1]
        tab_a[i + 1] = a
        i = i + 1
    return tab_a


class TestSujet13(TestCase):
    def test_recherche_case_simple(self) -> None:
        self.assertEqual(recherche(1, [10, 12, 1, 56]), 2)

    def test_recherche_case_double(self) -> None:
        self.assertEqual(recherche(50, [1, 50, 1]), 1)

    def test_recherche_case_last(self) -> None:
        self.assertEqual(recherche(15, [8, 9, 10, 15]), 3)

    def test_recherche_case_none(self) -> None:
        self.assertIsNone(recherche(1, [2, 3, 4]))

    def test_insere_case_base(self) -> None:
        self.assertListEqual(insere([1, 2, 4, 5], 3), [1, 2, 3, 4, 5])

    def test_insere_case_last(self) -> None:
        self.assertListEqual(
            insere([1, 2, 7, 12, 14, 25], 30), [1, 2, 7, 12, 14, 25, 30]
        )

    def test_insere_case_first(self) -> None:
        self.assertListEqual(insere([2, 3, 4], 1), [1, 2, 3, 4])

    def test_insere_case_empty(self) -> None:
        self.assertListEqual(insere([], 1), [1])


if __name__ == "__main__":
    main()
