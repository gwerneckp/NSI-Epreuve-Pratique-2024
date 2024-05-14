from unittest import TestCase, main


def moyenne(notes: list[tuple[float, float]]) -> float | None:
    nom, dem = 0.0, 0.0
    for note, coef in notes:
        nom += note * coef
        dem += coef
    return (nom / dem) if dem != 0 else None


# def affiche(dessin):
#     """affichage d'une grille : les 1 sont représentés par
#     des "*" , les 0 par un espace " " """
#     for ligne in dessin:
#         affichage = ""
#         for col in ligne:
#             if col == 1:
#                 affichage = affichage + "*"
#             else:
#                 affichage = affichage + " "
#         print(affichage)


# def liste_zoom(liste_depart, k):
#     """renvoie une liste contenant k fois chaque élément de
#     liste_depart"""
#     liste_zoomee = ...
#     for elt in ...:
#         for i in range(k):
#             ...
#     return liste_zoomee


# def dessin_zoom(grille, k):
#     """renvoie une grille où les lignes sont zoomées k fois
#     ET répétées k fois"""
#     grille_zoomee = []
#     for ligne in grille:
#         ligne_zoomee = ...
#         for i in range(k):
#             ....append(...)
#     return grille_zoomee


class TestSujet10(TestCase):
    def test_moyenne_case_1(self) -> None:
        result = moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])
        if result is None:
            self.fail("Moyenne returned None")

        self.assertAlmostEqual(result, 9.142857142857142)

    def test_moyenne_empty(self) -> None:
        self.assertIsNone(moyenne([(3, 0), (5, 0)]))


if __name__ == "__main__":
    main()
