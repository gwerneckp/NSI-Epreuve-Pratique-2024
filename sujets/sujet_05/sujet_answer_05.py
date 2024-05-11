from unittest import TestCase, main


def max_et_indice(tab: list[int]) -> tuple[int, int]:
    max_i, max_v = 0, tab[0]

    for i, v in enumerate(tab):
        if v > max_v:
            max_i, max_v = i, v

    return (max_v, max_i)


def est_un_ordre(tab: list[int]) -> bool:
    """
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinonRefactor max_et_indice function and add unit tests
    """
    n = len(tab)
    # les entiers vus lors du parcours
    vus = []

    for x in tab:
        if x < 1 or x > n or x in vus:
            return False
        vus.append(x)
    return True


def nombre_points_rupture(ordre: list[int]) -> int:
    """
    Renvoie le nombre de point de rupture de ordre qui représente
    un ordre de gènes de chromosome
    """
    # on vérifie que ordre est un ordre de gènes
    n = len(ordre)
    nb = 0
    if ordre[0] != 1:  # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < n - 1:
        if ordre[i] - ordre[i + 1] not in [-1, 1]:  # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[i] != n:  # le dernier n'est pas n
        nb = nb + 1
    return nb


class TestSujet05(TestCase):
    def test_max_et_indice_case1(self) -> None:
        self.assertEqual(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]), (9, 3))

    def test_max_et_indice_case2(self) -> None:
        self.assertEqual(max_et_indice([-2]), (-2, 0))

    def test_max_et_indice_case3(self) -> None:
        self.assertEqual(max_et_indice([-1, -1, 3, 3, 3]), (3, 2))

    def test_max_et_indice_case4(self) -> None:
        self.assertEqual(max_et_indice([1, 1, 1, 1]), (1, 0))

    def test_est_un_ordre_case1(self) -> None:
        self.assertEqual(est_un_ordre([1, 6, 2, 8, 3, 7]), False)

    def test_est_un_ordre_case2(self) -> None:
        self.assertEqual(est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]), True)

    def test_nombre_points_rupture_case1(self) -> None:
        self.assertEqual(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]), 4)

    def test_nombre_points_rupture_case2(self) -> None:
        self.assertEqual(nombre_points_rupture([1, 2, 3, 4, 5]), 0)

    def test_nombre_points_rupture_case3(self) -> None:
        self.assertEqual(nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]), 7)

    def test_nombre_points_rupture_case4(self) -> None:
        self.assertEqual(nombre_points_rupture([2, 1, 3, 4]), 2)


if __name__ == "__main__":
    main()
