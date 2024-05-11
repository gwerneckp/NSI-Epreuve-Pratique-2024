from unittest import TestCase, main
from typing import Optional
# from functools import reduce


def recherche(tab: list[int], n: int) -> Optional[int]:
    # return reduce(lambda acc, new: new if tab[new] == n else acc, range(len(tab)), None)
    last_i = None
    for i in range(len(tab)):
        if tab[i] == n:
            last_i = i

    return last_i


# def distance_carre(point1, point2):
#     """Calcule et renvoie la distance au carre entre
#     deux points."""
#     return (...) ** 2 + (...) ** 2


# def point_le_plus_proche(depart, tab):
#     """Renvoie les coordonnées du premier point du tableau tab se
#     trouvant à la plus courte distance du point depart."""
#     min_point = tab[0]
#     min_dist = ...
#     for i in range(1, len(tab)):
#         if distance_carre(tab[i], depart) < ...:
#             min_point = ...
#             min_dist = ...
#     return min_point


class TestSujet04(TestCase):
    def test_recherche_none(self):
        self.assertIsNone(recherche([5, 3], 1))

    def test_recherche_i_0(self):
        self.assertEqual(recherche([2, 4], 2), 0)

    def test_recherche_i_3(self):
        self.assertEqual(recherche([2, 3, 5, 2, 4], 2), 3)


if __name__ == "__main__":
    main()
