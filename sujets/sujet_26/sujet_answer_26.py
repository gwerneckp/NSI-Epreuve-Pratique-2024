from unittest import TestCase, main
from random import randint, seed


def ajoute_dictionnaires(d1: dict[int, int], d2: dict[int, int]) -> dict[int, int]:
    d_res: dict[int, int] = {}
    for d in [d1, d2]:
        for k in d.keys():
            d_res[k] = d1.get(k, 0) + d2.get(k, 0)

    return d_res


def nombre_coups() -> int:
    """Simule un jeu de plateau avec 12 cases et renvoie le nombre
    minimal de coups pour visiter toutes les cases."""
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [False] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = 0
    while nombre_cases_vues < nombre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % 12
        if not cases_vues[case_en_cours]:
            cases_vues[case_en_cours] = True
            nombre_cases_vues += 1
        n += 1

    return n


class TestSujet26(TestCase):

    def test_ajoute_dictionnaires_case_1(self) -> None:
        self.assertEqual(
            ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}), {1: 5, 2: 16, 3: 11}
        )

    def test_ajoute_dictionnaires_case_2(self) -> None:
        self.assertEqual(ajoute_dictionnaires({}, {2: 9, 3: 11}), {2: 9, 3: 11})

    def test_ajoute_dictionnaires_case_3(self) -> None:
        self.assertEqual(ajoute_dictionnaires({1: 5, 2: 7}, {}), {1: 5, 2: 7})

    def test_nombre_coups_case_1(self) -> None:
        seed(0)
        self.assertEqual(nombre_coups(), 34)

    def test_nombre_coups_case_2(self) -> None:
        seed(1)
        self.assertEqual(nombre_coups(), 22)

    def test_nombre_coups_other(self) -> None:
        seed()
        for i in range(10000):
            self.assertGreaterEqual(nombre_coups(), 11)


if __name__ == "__main__":
    main()
