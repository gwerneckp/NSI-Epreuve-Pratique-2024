from unittest import TestCase, main

from random import randint


def ajoute_dictionnaires(d1, d2):
    pass


def nombre_coups():
    """Simule un jeu de plateau avec 12 cases et renvoie le nombre
    minimal de coups pour visiter toutes les cases."""
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [False] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = ...
    while ... < ...:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + ...) % ...
        if ...:
            cases_vues[case_en_cours] = True
            nombre_cases_vues = ...
        n = ...
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


if __name__ == "__main__":
    main()
