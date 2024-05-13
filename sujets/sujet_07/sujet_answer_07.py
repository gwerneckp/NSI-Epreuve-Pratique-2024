from unittest import TestCase, main

# tab = [True, False, True, False, False, True, True]


def gb_vers_entier(tab: list[bool]) -> int:
    result = 0
    for i in range(len(tab)):
        result += 2 ** (len(tab) - 1 - i) * tab[i]

    return result


# def tri_insertion(tab):
#     """Trie le tableau tab par ordre croissant
#     en appliquant l'algorithme de tri par insertion"""
#     n = len(tab)
#     for i in range(1, n):
#         valeur_insertion = ...
#         # la variable j sert à déterminer
#         # où placer la valeur à ranger
#         j = ...
#         # tant qu'on n'a pas trouvé la place de l'élément à
#         # insérer on décale les valeurs du tableau vers la droite
#         while j > ... and valeur_insertion < tab[...]:
#             tab[j] = tab[j - 1]
#             j = ...
#         tab[j] = ...
#     return tab


class TestSujet06(TestCase):
    def test_gb_vers_entier_empty(self) -> None:
        self.assertEqual(gb_vers_entier([]), 0)

    def test_gb_vers_entier_case2(self) -> None:
        self.assertEqual(gb_vers_entier([True]), 1)

    # 1 0 1 0 0 1 1
    # 64 0 16 0 0 2 1
    # 83
    def test_gb_vers_entier_case3(self) -> None:
        self.assertEqual(
            gb_vers_entier([True, False, True, False, False, True, True]), 83
        )

    # 1 0 0 0 0 0 1 0
    # 128 0 0 0 0 0 2 0
    # 130
    def test_gb_vers_entier_case4(self) -> None:
        self.assertEqual(
            gb_vers_entier([True, False, False, False, False, False, True, False]), 130
        )


if __name__ == "__main__":
    main()
