from typing import Optional
from unittest import TestCase, main


class Noeud:
    def __init__(
        self, etiquette: int, gauche: Optional["Noeud"], droit: Optional["Noeud"]
    ):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit


def taille(a: Noeud | None) -> int:
    if a is None:
        return 0

    return 1 + taille(a.gauche) + taille(a.droit)


def hauteur(a: Noeud | None) -> int:
    if a is None:
        return -1

    return 1 + max(hauteur(a.gauche), hauteur(a.droit))


a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))


def ajoute(indice: int, element: int, tab: list[int]) -> list[int]:
    """Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab."""
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i]
    tab_ins[indice] = element
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i - 1]
    return tab_ins


class TestSujet41(TestCase):
    def test_hauteur_case_1(self) -> None:
        self.assertEqual(hauteur(a), 2)

    def test_hauteur_case_2(self) -> None:
        self.assertEqual(taille(a), 4)

    def test_hauteur_case_3(self) -> None:
        self.assertEqual(hauteur(None), -1)

    def test_hauteur_case_4(self) -> None:
        self.assertEqual(taille(None), 0)

    def test_hauteur_case_5(self) -> None:
        self.assertEqual(hauteur(Noeud(1, None, None)), 0)

    def test_hauteur_case_6(self) -> None:
        self.assertEqual(taille(Noeud(1, None, None)), 1)

    def test_ajoute_case_1(self) -> None:
        self.assertEqual(ajoute(1, 4, [7, 8, 9]), [7, 4, 8, 9])

    def test_ajoute_case_2(self) -> None:
        self.assertEqual(ajoute(3, 4, [7, 8, 9]), [7, 8, 9, 4])

    def test_ajoute_case_3(self) -> None:
        self.assertEqual(ajoute(0, 4, [7, 8, 9]), [4, 7, 8, 9])


if __name__ == "__main__":
    main()
