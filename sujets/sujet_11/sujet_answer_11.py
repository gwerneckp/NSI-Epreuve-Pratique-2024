from unittest import TestCase, main
from re import findall


def nombre_de_mots(phrase: str) -> int:
    phrase_l = phrase.split(" ")
    if phrase_l[-1] in ["!", "?"]:
        return len(phrase_l) - 1
    return len(phrase_l)
    # return len(findall(r"(\w+)", phrase))


class Noeud:
    def __init__(self, etiquette: int):
        """Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée."""
        self.etiquette = etiquette
        self.gauche: Noeud | None = None
        self.droit: Noeud | None = None

    def inserer(self, cle: int) -> None:
        """Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure."""
        if cle < self.etiquette:
            if self.gauche is not None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        else:
            if self.droit is not None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)


arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)


class TestSujet11(TestCase):

    def test_nombre_de_mots_simple_phrase(self) -> None:
        self.assertEqual(nombre_de_mots("Cet exercice est simple."), 4)

    def test_nombre_de_mots_with_exclamation(self) -> None:
        self.assertEqual(nombre_de_mots("Le point d exclamation est séparé !"), 6)

    def test_nombre_de_mots_long_phrase(self) -> None:
        self.assertEqual(
            nombre_de_mots("Combien de mots y a t il dans cette phrase ?"), 10
        )

    def test_nombre_de_mots_single_word(self) -> None:
        self.assertEqual(nombre_de_mots("Fin."), 1)

    def setUp(self) -> None:
        self.arbre = Noeud(7)
        for cle in (3, 9, 1, 6):
            self.arbre.inserer(cle)

    def test_insertion_gauche(self) -> None:
        self.assertIsNotNone(self.arbre.gauche)
        self.assertEqual(self.arbre.gauche.etiquette, 3)

    def test_insertion_droit(self) -> None:
        self.assertIsNotNone(self.arbre.droit)
        self.assertEqual(self.arbre.droit.etiquette, 9)

    def test_insertion_gauche_gauche(self) -> None:
        self.assertIsNotNone(self.arbre.gauche.gauche)
        self.assertEqual(self.arbre.gauche.gauche.etiquette, 1)

    def test_insertion_gauche_droit(self) -> None:
        self.assertIsNotNone(self.arbre.gauche.droit)
        self.assertEqual(self.arbre.gauche.droit.etiquette, 6)


if __name__ == "__main__":
    main()
