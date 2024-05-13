from unittest import TestCase, main


def delta(tab: list[int]) -> list[int]:
    return [tab[0]] + [tab[i] - tab[i - 1] for i in range(1, len(tab))]


# class Expr:
#     """Classe implémentant un arbre d'expression."""

#     def __init__(self, g, v, d):
#         """un objet Expr possède 3 attributs :
#         - gauche : la sous-expression gauche ;
#         - valeur : la valeur de l'étiquette, opérande ou nombre ;
#         - droite : la sous-expression droite."""
#         self.gauche = g
#         self.valeur = v
#         self.droite = d

#     def est_une_feuille(self):
#         """renvoie True si et seulement
#         si le noeud est une feuille"""
#         return self.gauche is None and self.droite is None

#     def infixe(self):
#         """renvoie la représentation infixe de l'expression en
#         chaine de caractères"""
#         s = ...
#         if self.gauche is not None:
#             s = "(" + s + ....infixe()
#         s = s + ...
#         if ... is not None:
#             s = s + ... + ...
#         return s


class TestSujet08(TestCase):
    def test_delta_case1(self) -> None:
        self.assertEqual(delta([1000, 800, 802, 1000, 1003]), [1000, -200, 2, 198, 3])

    def test_delta_case2(self) -> None:
        self.assertEqual(delta([42]), [42])

    # def test_infixe_case1(self) -> None:
    #     a = Expr(Expr(None, 1, None), "+", Expr(None, 2, None))
    #     self.assertEqual(a.infixe(), "(1+2)")

    # def test_infixe_case2(self) -> None:
    #     b = Expr(
    #         Expr(Expr(None, 1, None), "+", Expr(None, 2, None)),
    #         "*",
    #         Expr(Expr(None, 3, None), "+", Expr(None, 4, None)),
    #     )
    #     self.assertEqual(b.infixe(), "((1+2)*(3+4))")

    # def test_infixe_case3(self) -> None:
    #     e = Expr(
    #         Expr(
    #             Expr(None, 3, None),
    #             "*",
    #             Expr(Expr(None, 8, None), "+", Expr(None, 7, None)),
    #         ),
    #         "-",
    #         Expr(Expr(None, 2, None), "+", Expr(None, 1, None)),
    #     )
    #     self.assertEqual(e.infixe(), "((3*(8+7))-(2+1))")


if __name__ == "__main__":
    main()
