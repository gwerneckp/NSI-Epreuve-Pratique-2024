from unittest import TestCase, main


def correspond(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i] and b[i] != "*":
            return False

    return True


def est_cyclique(plan: dict[str, str]) -> bool:
    """Prend en paramètre un dictionnaire `plan` correspondant à
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et
    False sinon."""
    expediteur = "A"
    destinataire = plan[expediteur]
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires += 1

    return nb_destinataires == len(plan)


class TestSujet02(TestCase):
    def test_correspond_true(self) -> None:
        self.assertTrue(correspond("INFORMATIQUE", "INFO*MA*IQUE"))

    def test_correspond_false(self) -> None:
        self.assertFalse(correspond("AUTOMATIQUE", "INFO*MA*IQUE"))

    def test_correspond_not_same_lenght(self) -> None:
        self.assertFalse(correspond("STOP", "S*"))

    def test_cyclique_false(self) -> None:
        self.assertFalse(
            est_cyclique({"A": "E", "F": "A", "C": "D", "E": "B", "B": "F", "D": "C"})
        )

    def test_cyclique_false_2(self) -> None:
        self.assertFalse(
            est_cyclique({"A": "B", "F": "A", "C": "D", "E": "C", "B": "F", "D": "E"})
        )

    def test_cyclique_true(self) -> None:
        self.assertTrue(
            est_cyclique({"A": "E", "F": "C", "C": "D", "E": "B", "B": "F", "D": "A"})
        )

    def test_cyclique_true_2(self) -> None:
        self.assertTrue(
            est_cyclique({"A": "B", "F": "C", "C": "D", "E": "A", "B": "F", "D": "E"})
        )


if __name__ == "__main__":
    main()
