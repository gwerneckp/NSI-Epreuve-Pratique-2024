from unittest import TestCase, main


def verifie(tab: list[int]) -> bool:
    min_v = float("-inf")

    for v in tab:
        if v >= min_v:
            min_v = v
            continue
        return False

    return True


# urne = ["A", "A", "A", "B", "C", "B", "C", "B", "C", "B"]


# def depouille(urne):
#     """prend en paramètre une liste de suffrages et renvoie un
#     dictionnaire avec le nombre de voix pour chaque candidat"""
#     resultat = ...
#     for bulletin in urne:
#         if ...:
#             resultat[bulletin] = resultat[bulletin] + 1
#         else:
#             ...
#     return resultat


# def vainqueurs(election):
#     """prend en paramètre un dictionnaire non vide avec le nombre de voix
#     pour chaque candidat et renvoie la liste des vainqueurs"""
#     nmax = 0
#     for candidat in election:
#         if ... > ...:
#             nmax = ...
#     liste_finale = [nom for nom in election if ...]
#     return ...


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


if __name__ == "__main__":
    main()
