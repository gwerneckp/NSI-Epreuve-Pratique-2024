from typing import TypedDict
from unittest import TestCase, main


MinMax = TypedDict("MinMax", {"min": int, "max": int})


def min_et_max(tab: list[int]) -> MinMax:
    min_v, max_v = tab[0], tab[0]
    for v in tab:
        if v > max_v:
            max_v = v
            continue
        if v < min_v:
            min_v = v

    return {"min": min_v, "max": max_v}


class Carte:
    def __init__(self, c: int, v: int):
        """Initialise les attributs couleur (entre 1 et 4), et valeur (entre 1 et 13)."""
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self) -> str:
        """Renvoie la valeur de la carte : As, 2, ..., 10, Valet, Dame, Roi"""
        valeurs = [
            "As",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Valet",
            "Dame",
            "Roi",
        ]
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self) -> str:
        """Renvoie la couleur de la carte (parmi pique, coeur, carreau, trèfle)."""
        couleurs = ["pique", "coeur", "carreau", "trèfle"]
        return couleurs[self.couleur - 1]


class Paquet_de_cartes:
    def __init__(self) -> None:
        """Initialise l'attribut contenu avec une liste des 52 objets Carte possibles
        rangés par valeurs croissantes en commençant par pique, puis coeur,
        carreau et tréfle."""
        self.contenu: list[Carte] = []
        for c in range(1, 5):
            for v in range(1, 14):
                self.contenu.append(Carte(c, v))

    def recuperer_carte(self, pos: int) -> Carte:
        """Renvoie la carte qui se trouve à la position pos (entier compris entre 0 et 51)."""
        carte = self.contenu[pos]
        return carte


class TestSujet14(TestCase):
    def test_min_max_case_1(self) -> None:
        self.assertDictEqual(
            min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]), {"min": -2, "max": 9}
        )

    def test_min_max_case_2(self) -> None:
        self.assertDictEqual(min_et_max([0, 1, 2, 3]), {"min": 0, "max": 3})

    def test_min_max_case_3(self) -> None:
        self.assertDictEqual(min_et_max([1, 3, 2, 1, 3]), {"min": 1, "max": 3})

    def test_min_max_case_single(self) -> None:
        self.assertDictEqual(min_et_max([3]), {"min": 3, "max": 3})

    def test_min_max_case_same(self) -> None:
        self.assertDictEqual(min_et_max([-1, -1, -1, -1, -1]), {"min": -1, "max": -1})

    def setUp(self) -> None:
        self.jeu = Paquet_de_cartes()

    def test_paquet_8_de_coeur(self) -> None:
        carte1 = self.jeu.recuperer_carte(20)
        self.assertEqual(
            carte1.recuperer_valeur() + " de " + carte1.recuperer_couleur(),
            "8 de coeur",
        )

    def test_paquet_as_de_pique(self) -> None:
        carte2 = self.jeu.recuperer_carte(0)
        self.assertEqual(
            carte2.recuperer_valeur() + " de " + carte2.recuperer_couleur(),
            "As de pique",
        )

    def test_paquet_index_error(self) -> None:
        self.assertRaises(IndexError, self.jeu.recuperer_carte, 52)


if __name__ == "__main__":
    main()
