from unittest import TestCase, main


def ecriture_binaire_entier_positif(n: int) -> str:
    if n == 0:
        return "0"

    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result


def echange(tab: list, i: int, j: int) -> None:
    """Echange les éléments d'indice i et j dans le tableau tab."""
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def tri_bulles(tab: list[int]) -> list[int]:
    """Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles."""
    n = len(tab)
    for i in range(n):
        for j in range(i):
            if tab[i] < tab[j]:
                echange(tab, j, i)
    return tab


class TestSujet16(TestCase):
    def test_int_to_bin_case_zero(self) -> None:
        self.assertEqual(ecriture_binaire_entier_positif(0), "0")

    def test_int_to_bin_case_base_1(self) -> None:
        self.assertEqual(ecriture_binaire_entier_positif(2), "10")

    def test_int_to_bin_case_base_2(self) -> None:
        self.assertEqual(ecriture_binaire_entier_positif(105), "1101001")

    def test_echange_case_base(self) -> None:
        tab_1 = [1, 2]
        echange(tab_1, 0, 1)
        self.assertListEqual(tab_1, [2, 1])

    def test_echange_case_same(self) -> None:
        tab_2 = [1, 2, 3]
        echange(tab_2, 1, 1)
        self.assertListEqual(tab_2, [1, 2, 3])

    def test_tri_case_base(self) -> None:
        self.assertListEqual(tri_bulles([9, 3, 7, 2, 3, 1, 6]), [1, 2, 3, 3, 6, 7, 9])

    def test_tri_case_empty(self) -> None:
        self.assertListEqual(tri_bulles([]), [])

    def test_tri_case_inverse(self) -> None:
        self.assertListEqual(tri_bulles([9, 7, 4, 3]), [3, 4, 7, 9])


if __name__ == "__main__":
    main()
