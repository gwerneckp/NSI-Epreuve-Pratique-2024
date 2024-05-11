from unittest import TestCase, main


def max_et_indice(tab: list[int]) -> tuple[int, int]:
    max_i, max_v = 0, tab[0]

    for i, v in enumerate(tab):
        if v > max_v:
            max_i, max_v = i, v

    return (max_v, max_i)


# def est_un_ordre(tab):
#     """
#     Renvoie True si tab est de longueur n et contient tous les
#     entiers de 1 à n, False sinon
#     """
#     n = len(tab)
#     # les entiers vus lors du parcours
#     vus = ...

#     for x in tab:
#         if x < ... or x > ... or ...:
#             return False
#         ....append(...)
#     return True


# def nombre_points_rupture(ordre):
#     """
#     Renvoie le nombre de point de rupture de ordre qui représente
#     un ordre de gènes de chromosome
#     """
#     # on vérifie que ordre est un ordre de gènes
#     n = len(ordre)
#     nb = 0
#     if ordre[...] != 1:  # le premier n'est pas 1
#         nb = nb + 1
#     i = 0
#     while i < ...:
#         if ... not in [-1, 1]:  # l'écart n'est pas 1
#             nb = nb + 1
#         i = i + 1
#     if ordre[i] != ...:  # le dernier n'est pas n
#         nb = nb + 1
#     return nb


class TestSujet05(TestCase):
    def test_max_et_indice_case1(self):
        self.assertEqual(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]), (9, 3))

    def test_max_et_indice_case2(self):
        self.assertEqual(max_et_indice([-2]), (-2, 0))

    def test_max_et_indice_case3(self):
        self.assertEqual(max_et_indice([-1, -1, 3, 3, 3]), (3, 2))

    def test_max_et_indice_case4(self):
        self.assertEqual(max_et_indice([1, 1, 1, 1]), (1, 0))


if __name__ == "__main__":
    main()
