from unittest import TestCase, main


def verifie(tab: list[int]) -> bool:
    min_v = float("-inf")

    for v in tab:
        if v >= min_v:
            min_v = v
            continue
        return False

    return True


def depouille(urne: list[str]) -> dict[str, int]:
    """prend en paramètre une liste de suffrages et renvoie un
    dictionnaire avec le nombre de voix pour chaque candidat"""
    resultat: dict[str, int] = {}
    for bulletin in urne:
        if resultat.get(bulletin):
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat


def vainqueurs(election: dict[str, int]) -> list[str]:
    """prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs"""
    nmax = 0
    for candidat in election:
        if (n := election[candidat]) > nmax:
            nmax = n
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale


class TestSujet05(TestCase):
    def test_verifie_true(self) -> None:
        self.assertTrue(verifie([0, 5, 8, 8, 9]))

    def test_verifie_false(self) -> None:
        self.assertFalse(verifie([8, 12, 4]))

    def test_verifie_true_negative(self) -> None:
        self.assertTrue(verifie([-1, 4]))

    def test_verifie_empty_list(self) -> None:
        self.assertTrue(verifie([]))

    def test_verifie_single_element(self) -> None:
        self.assertTrue(verifie([5]))

    def test_depouille_case1(self) -> None:
        self.assertDictEqual(depouille(["A", "B", "A"]), {"A": 2, "B": 1})

    def test_depouille_empty(self) -> None:
        self.assertDictEqual(depouille([]), {})

    def test_depouille_case3(self) -> None:
        self.assertDictEqual(
            depouille(["A", "A", "A", "B", "C", "B", "C", "B", "C", "B"]),
            {"A": 3, "B": 4, "C": 3},
        )

    def test_vainqueurs_case1(self) -> None:
        self.assertListEqual(vainqueurs({"A": 3, "B": 4, "C": 3}), ["B"])

    def test_vainqueurs_case2(self) -> None:
        self.assertListEqual(vainqueurs({"A": 2, "B": 2, "C": 1}), ["A", "B"])


if __name__ == "__main__":
    main()
