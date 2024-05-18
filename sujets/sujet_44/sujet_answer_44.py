from unittest import TestCase, main

class Noeud:
    """Classe représentant un noeud d'un arbre binaire"""
    def __init__(self, etiquette, gauche, droit):
        """Crée un noeud de valeur etiquette avec 
        gauche et droit comme fils."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

def parcours(arbre, liste):
    """parcours récursivement l'arbre en ajoutant les étiquettes
    de ses noeuds à la liste passée en argument en ordre infixe."""
    if arbre != None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste

def insere(arbre, cle):
    """insere la cle dans l'arbre binaire de recherche
    représenté par arbre.
    Retourne l'arbre modifié."""
    if arbre == None:
        return Noeud(cle, None, None) # creation d'une feuille
    else:
        if ...: 
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = ... 
        return arbre

class TestSujet44(TestCase):
    def test_enumere_case_1(self) -> None:
        self.assertEqual(enumere([]), {})

    def test_enumere_case_2(self) -> None:
        self.assertEqual(enumere([1, 2, 3]), {1: [0], 2: [1], 3: [2]})

    def test_enumere_case_3(self) -> None:
        self.assertEqual(enumere([1, 1, 2, 3, 2, 1]), {1: [0, 1, 5], 2: [2, 4], 3: [3]})

if __name__ == "__main__":
    main()