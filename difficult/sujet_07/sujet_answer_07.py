from unittest import TestCase, main


def tri_insertion(tab: list[int]) -> list[int]:
    """Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion"""
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à déterminer
        # où placer la valeur à ranger
        j = i
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j - 1]:
            tab[j] = tab[j - 1]
            j = j - 1
        tab[j] = valeur_insertion
    return tab


class TestSujet07(TestCase):
    def test_tri_insertion(self) -> None:
        self.assertListEqual(
            tri_insertion([98, 12, 104, 23, 131, 9]), [9, 12, 23, 98, 104, 131]
        )

    def test_tri_insertion_already_sorted(self) -> None:
        self.assertListEqual(tri_insertion([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_tri_insertion_vide(self) -> None:
        self.assertListEqual(tri_insertion([]), [])


if __name__ == "__main__":
    main()
