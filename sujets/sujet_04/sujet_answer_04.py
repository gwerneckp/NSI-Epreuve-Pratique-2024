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


def distance_carre(point1: tuple[int, int], point2: tuple[int, int]):
    """Calcule et renvoie la distance au carre entre
    deux points."""

    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


def point_le_plus_proche(
    depart: tuple[int, int], tab: list[tuple[int, int]]
) -> tuple[int, int]:
    """Renvoie les coordonnées du premier point du tableau tab se
    trouvant à la plus courte distance du point depart."""
    min_point = tab[0]
    min_dist = distance_carre(depart, min_point)
    for i in range(1, len(tab)):
        if (dist := distance_carre(tab[i], depart)) < min_dist:
            min_point = tab[i]
            min_dist = dist
    return min_point


class TestSujet04(TestCase):
    def test_recherche_none(self):
        self.assertIsNone(recherche([5, 3], 1))

    def test_recherche_i_0(self):
        self.assertEqual(recherche([2, 4], 2), 0)

    def test_recherche_i_3(self):
        self.assertEqual(recherche([2, 3, 5, 2, 4], 2), 3)

    def test_distance_1(self):
        self.assertEqual(distance_carre((1, 0), (5, 3)), 25)

    def test_distance_2(self):
        self.assertEqual(distance_carre((1, 0), (0, 1)), 2)

    def test_point_plus_proche_1(self):
        self.assertTupleEqual(
            point_le_plus_proche((0, 0), [(7, 9), (2, 5), (5, 2)]), (2, 5)
        )

    def test_point_plus_proche_2(self):
        self.assertTupleEqual(
            point_le_plus_proche((5, 2), [(7, 9), (2, 5), (5, 2)]), (5, 2)
        )


if __name__ == "__main__":
    main()
