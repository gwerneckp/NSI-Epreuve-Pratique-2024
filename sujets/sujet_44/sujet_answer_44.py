from typing import Any, Optional
from unittest import TestCase, main


def enumere(tab: list) -> dict[Any, list[int]]:
    d: dict[Any, list[int]] = {}
    for i in range(len(tab)):
        d[tab[i]] = d.get(tab[i], []) + [i]
    return d


class Noeud:
    """Classe représentant un noeud d'un arbre binaire"""

    def __init__(
        self, etiquette: int, gauche: Optional["Noeud"], droit: Optional["Noeud"]
    ):
        """Crée un noeud de valeur etiquette avec
        gauche et droit comme fils."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Noeud):
            raise TypeError(f"Comparaison entre Noeud et {type(value)} non supportée")
        return (
            self.etiquette == value.etiquette
            and self.gauche == value.gauche
            and self.droit == value.droit
        )


def parcours(arbre: Noeud | None, liste: list[int]) -> list[int]:
    """parcours récursivement l'arbre en ajoutant les étiquettes
    de ses noeuds à la liste passée en argument en ordre infixe."""
    if arbre is not None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste


def insere(arbre: Noeud | None, cle: int) -> Noeud:
    """insere la cle dans l'arbre binaire de recherche
    représenté par arbre.
    Retourne l'arbre modifié."""
    if arbre is None:
        return Noeud(cle, None, None)  # creation d'une feuille
    else:
        if arbre.etiquette > cle:
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle)
        return arbre


class TestSujet44(TestCase):
    def test_enumere_case_1(self) -> None:
        self.assertEqual(enumere([]), {})

    def test_enumere_case_2(self) -> None:
        self.assertEqual(enumere([1, 2, 3]), {1: [0], 2: [1], 3: [2]})

    def test_enumere_case_3(self) -> None:
        self.assertEqual(enumere([1, 1, 2, 3, 2, 1]), {1: [0, 1, 5], 2: [2, 4], 3: [3]})

    def test_insere_case_1(self) -> None:
        arbre = Noeud(5, Noeud(2, None, Noeud(3, None, None)), Noeud(7, None, None))
        insere(insere(insere(insere(arbre, 1), 4), 6), 8)
        self.assertEqual(
            arbre,
            Noeud(
                5,
                Noeud(2, Noeud(1, None, None), Noeud(3, None, Noeud(4, None, None))),
                Noeud(7, Noeud(6, None, None), Noeud(8, None, None)),
            ),
        )


if __name__ == "__main__":
    main()
