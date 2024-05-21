from typing import Any, Literal
from unittest import TestCase, main


def max_dico(dico: dict[str, int]) -> tuple[str, int]:
    nom_max, like_max = "", -1

    for nom, like in dico.items():
        if like > like_max:
            nom_max, like_max = nom, like

    return (nom_max, like_max)


class Pile:
    """Classe définissant une structure de pile."""

    def __init__(self) -> None:
        self.contenu: list[Any] = []

    def est_vide(self) -> bool:
        """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v: Any) -> None:
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self) -> Any:
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n'est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()


def eval_expression(tab: list[int | Literal["*", "+"]]) -> int:
    p = Pile()
    for element in tab:
        if element != "+" and element != "*":
            p.empiler(element)
        else:
            resultat: int
            if element == "+":
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()


class TestSujet47(TestCase):
    def test_max_dico_case_1(self) -> None:
        self.assertEqual(
            max_dico({"Bob": 102, "Ada": 201, "Alice": 103, "Tim": 50}), ("Ada", 201)
        )

    def test_max_dico_case_2(self) -> None:
        self.assertEqual(
            max_dico({"Alan": 222, "Ada": 201, "Eve": 220, "Tim": 50}), ("Alan", 222)
        )

    def test_eval_expression_case_1(self) -> None:
        self.assertEqual(eval_expression([2, 3, "+", 5, "*"]), 25)

    def test_eval_expression_case_2(self) -> None:
        self.assertEqual(eval_expression([1, 2, "+", 3, "*"]), 9)

    def test_eval_expression_case_3(self) -> None:
        self.assertEqual(eval_expression([1, 2, 3, "+", "*"]), 5)


if __name__ == "__main__":
    main()
