from unittest import TestCase, main

Node = tuple["Node", int, "Node"] | None


def parcours_largeur(noeud: Node) -> list[int]:
    if not noeud:
        return []

    visited = [noeud[1]]
    to_visit = []

    if noeud[0]:
        to_visit.append(noeud[0])

    if noeud[2]:
        to_visit.append(noeud[2])

    while to_visit:
        noeud = to_visit.pop(0)
        visited.append(noeud[1])

        if noeud[0]:
            to_visit.append(noeud[0])

        if noeud[2]:
            to_visit.append(noeud[2])

    return visited


def somme_max(tab: list[int]) -> int:
    n = len(tab)
    sommes_max = [0] * n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1, n):
        if (somme := sommes_max[i - 1] + tab[i]) > tab[i]:
            sommes_max[i] = somme
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum]:
            maximum = i

    return sommes_max[maximum]


class TestSujet23(TestCase):
    def test_parcours_largeur(self) -> None:
        arbre = (
            ((None, 1, None), 2, (None, 3, None)),
            4,
            ((None, 5, None), 6, (None, 7, None)),
        )
        self.assertEqual(parcours_largeur(arbre), [4, 2, 6, 1, 3, 5, 7])

    def test_parcours_largeur_empty_tree(self) -> None:
        arbre = None
        self.assertEqual(parcours_largeur(arbre), [])

    def test_parcours_largeur_single_node(self) -> None:
        arbre = (None, 1, None)
        self.assertEqual(parcours_largeur(arbre), [1])

    def test_parcours_largeur_left_children(self) -> None:
        arbre = (((((None, 1, None), 2, None), 3, None), 4, None), 5, None)
        self.assertEqual(parcours_largeur(arbre), [5, 4, 3, 2, 1])

    def test_parcours_largeur_right_children(self) -> None:
        arbre = (None, 1, (None, 2, (None, 3, (None, 4, (None, 5, None)))))
        self.assertEqual(parcours_largeur(arbre), [1, 2, 3, 4, 5])

    def test_parcours_largeur_complex_tree(self) -> None:
        arbre = (
            ((None, 1, (None, 6, None)), 2, (None, 3, None)),
            4,
            ((None, 5, None), 6, ((None, 7, None), 8, (None, 9, None))),
        )
        self.assertEqual(parcours_largeur(arbre), [4, 2, 6, 1, 3, 5, 8, 6, 7, 9])

    def test_somme_max_case1(self) -> None:
        self.assertEqual(somme_max([1, 2, 3, 4, 5]), 15)

    def test_somme_max_case2(self) -> None:
        self.assertEqual(somme_max([1, 2, -3, 4, 5]), 9)

    def test_somme_max_case3(self) -> None:
        self.assertEqual(somme_max([1, 2, -2, 4, 5]), 10)

    def test_somme_max_case4(self) -> None:
        self.assertEqual(somme_max([1, -2, 3, 10, -4, 7, 2, -5]), 18)


if __name__ == "__main__":
    somme_max([1, -2, 3, 10, -4, 7, 2, -5])
    main()
