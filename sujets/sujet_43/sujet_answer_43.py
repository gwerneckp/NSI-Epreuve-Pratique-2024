from unittest import TestCase, main


def a_doublon(tab: list[int]) -> bool:
    curr = float("nan")
    for v in tab:
        if v == curr:
            return True
        curr = v
    return False


def voisinage(n: int, ligne: int, colonne: int) -> list[tuple[int, int]]:
    """Renvoie la liste des coordonnées des voisins de la case
    (ligne, colonne) en gérant les cases sur les bords."""
    voisins = []
    for lig in range(max(0, ligne - 1), min(n, ligne + 2)):
        for col in range(max(0, colonne - 1), min(n, colonne + 2)):
            if (lig, col) != (ligne, colonne):
                voisins.append((lig, col))
    return voisins


def incremente_voisins(grille: list[list[int]], ligne: int, colonne: int) -> None:
    """Incrémente de 1 toutes les cases voisines d'une bombe."""
    voisins = voisinage(len(grille), ligne, colonne)
    for lig, col in voisins:
        if grille[lig][col] != -1:  # si ce n'est pas une bombe
            grille[lig][col] += 1  # on ajoute 1 à sa valeur


def genere_grille(bombes: list[tuple[int, int]]) -> list[list[int]]:
    """Renvoie une grille de démineur de taille nxn où n est
    le nombre de bombes, en plaçant les bombes à l'aide de
    la liste bombes de coordonnées (tuples) passée en
    paramètre."""
    n = len(bombes)
    # Initialisation d'une grille nxn remplie de 0
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    # Place les bombes et calcule les valeurs des autres cases
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1  # place la bombe
        incremente_voisins(grille, ligne, colonne)

    return grille


class TestSujet43(TestCase):
    def test_a_doublon_case_1(self) -> None:
        self.assertFalse(a_doublon([]))

    def test_a_doublon_case_2(self) -> None:
        self.assertFalse(a_doublon([1]))

    def test_a_doublon_case_3(self) -> None:
        self.assertTrue(a_doublon([1, 2, 4, 6, 6]))

    def test_a_doublon_case_4(self) -> None:
        self.assertTrue(a_doublon([2, 5, 7, 7, 7, 9]))

    def test_a_doublon_case_5(self) -> None:
        self.assertFalse(a_doublon([0, 2, 3]))

    def test_genre_grille(self) -> None:
        self.assertEqual(
            genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]),
            [
                [1, 1, 1, 0, 0],
                [1, -1, 1, 1, 1],
                [2, 2, 3, 2, -1],
                [1, -1, 2, -1, 3],
                [1, 1, 2, 2, -1],
            ],
        )


if __name__ == "__main__":
    main()
