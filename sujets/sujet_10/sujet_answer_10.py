from typing import Literal
from unittest import TestCase, main


def moyenne(notes: list[tuple[float, float]]) -> float | None:
    nom, dem = 0.0, 0.0
    for note, coef in notes:
        nom += note * coef
        dem += coef
    return (nom / dem) if dem != 0 else None


Dessin = list[list[Literal[0, 1]]]


def affiche(dessin: Dessin) -> None:
    """affichage d'une grille : les 1 sont représentés par
    des "*" , les 0 par un espace " " """
    for ligne in dessin:
        affichage = ""
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)


def liste_zoom(liste_depart: list, k: int) -> list:
    """renvoie une liste contenant k fois chaque élément de
    liste_depart"""
    liste_zoomee = []
    for elt in liste_depart:
        for _ in range(k):
            liste_zoomee.append(elt)
    return liste_zoomee


def dessin_zoom(grille: Dessin, k: int) -> Dessin:
    """renvoie une grille où les lignes sont zoomées k fois
    ET répétées k fois"""
    grille_zoomee = []
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne, k)
        for i in range(k):
            grille_zoomee.append(ligne_zoomee)
    return grille_zoomee


class TestSujet10(TestCase):
    def test_moyenne_case_1(self) -> None:
        result = moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])
        if result is None:
            self.fail("Moyenne returned None")

        self.assertAlmostEqual(result, 9.142857142857142)

    def test_moyenne_empty(self) -> None:
        self.assertIsNone(moyenne([(3, 0), (5, 0)]))

    def test_liste_zoom(self) -> None:
        self.assertListEqual(liste_zoom([1, 2, 3], 3), [1, 1, 1, 2, 2, 2, 3, 3, 3])

    def test_grille_zoom(self) -> None:
        self.assertListEqual(
            dessin_zoom([[1, 0], [0, 1]], 2),
            [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
        )


print(f"From module: {__name__}")
if __name__ == "__main__":
    coeur: Dessin = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    affiche(coeur)
    affiche(dessin_zoom(coeur, 2))

    main()
