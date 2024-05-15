from unittest import TestCase, main


def recherche_indices_classement(
    elt: int, tab: list[int]
) -> tuple[list[int], list[int], list[int]]:
    lt = []
    e = []
    gt = []
    for i in range(len(tab)):
        if tab[i] < elt:
            lt.append(i)
            continue
        if tab[i] > elt:
            gt.append(i)
            continue
        e.append(i)
    return (lt, e, gt)


Resultat = dict[str, dict[str, list[float]]]


def moyenne(nom: str, resultats: Resultat) -> float | None:
    """Renvoie la moyenne de l'élève nom, selon le dictionnaire
    resultats. Si nom n'est pas dans le dictionnaire,
    la fonction renvoie None."""
    if nom in resultats:
        notes = resultats[nom]
        if len(notes) <= 0:  # pas de notes
            return 0
        total_points = 0.0
        total_coefficients = 0.0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points / total_coefficients, 1)
    else:
        return None


class TestFunctions(TestCase):

    def setUp(self) -> None:
        self.resultats: Resultat = {
            "Dupont": {
                "DS1": [15.5, 4],
                "DM1": [14.5, 1],
                "DS2": [13, 4],
                "PROJET1": [16, 3],
                "DS3": [14, 4],
            },
            "Durand": {
                "DS1": [6, 4],
                "DS2": [8, 4],
                "PROJET1": [9, 3],
                "IE1": [7, 2],
                "DS3": [12, 4],
            },
        }

    def test_recherche_indices_classement_case1(self) -> None:
        self.assertEqual(
            recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]),
            ([0, 3, 7], [1, 6], [2, 4, 5]),
        )

    def test_recherche_indices_classement_case2(self) -> None:
        self.assertEqual(
            recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]),
            ([0, 2, 5], [], [1, 3, 4]),
        )

    def test_recherche_indices_classement_case3(self) -> None:
        self.assertEqual(
            recherche_indices_classement(3, [1, 1, 1, 1]), ([0, 1, 2, 3], [], [])
        )

    def test_recherche_indices_classement_case4(self) -> None:
        self.assertEqual(recherche_indices_classement(3, []), ([], [], []))

    def test_moyenne_dupont(self) -> None:
        self.assertEqual(moyenne("Dupont", self.resultats), 14.5)

    def test_moyenne_durand(self) -> None:
        self.assertEqual(moyenne("Durand", self.resultats), 8.5)


if __name__ == "__main__":
    main()
