from unittest import TestCase, main


Node = tuple["Node", int, "Node"] | None


def insertion_abr(abr: Node, cle: int) -> Node:
    if abr is None:
        return (None, cle, None)
    elif cle > abr[1]:
        return (abr[0], abr[1], insertion_abr(abr[2], cle))
    elif cle < abr[1]:
        return (insertion_abr(abr[0], cle), abr[1], abr[2])
    return abr


def empaqueter(liste_masses: list[int], c: int) -> int:
    """Renvoie le nombre minimal de boîtes nécessaires pour
    empaqueter les objets de la liste liste_masses, sachant
    que chaque boîte peut contenir au maximum c kilogrammes"""
    n = len(liste_masses)
    nb_boites = 0
    boites = [0 for _ in range(n)]
    for masse in liste_masses:
        i = 0
        while i < nb_boites and boites[i] + masse > c:
            i = i + 1
        if i == nb_boites:
            nb_boites += 1
        boites[i] = boites[i] + masse
    return nb_boites


class TestSujet23(TestCase):
    def setUp(self) -> None:
        self.n0 = (None, 0, None)
        self.n3 = (None, 3, None)
        self.n2 = (None, 2, self.n3)
        self.abr1 = (self.n0, 1, self.n2)

    def test_insertion_abr_case_single(self) -> None:
        self.assertEqual(insertion_abr((None, 1, None), 2), (None, 1, (None, 2, None)))

    def test_insertion_abr_case_single_repeated(self) -> None:
        self.assertEqual(insertion_abr((None, 1, None), 1), (None, 1, None))

    def test_insertion_abr_case_left_empty(self) -> None:
        self.assertEqual(
            insertion_abr((None, 3, (None, 4, None)), 2),
            ((None, 2, None), 3, (None, 4, None)),
        )

    def test_insertion_abr_case_left_empty_more(self) -> None:
        self.assertEqual(
            insertion_abr((None, 3, (None, 5, None)), 4),
            (None, 3, ((None, 4, None), 5, None)),
        )

    def test_insertion_abr_case1(self) -> None:
        self.assertEqual(
            insertion_abr(self.abr1, 4),
            ((None, 0, None), 1, (None, 2, (None, 3, (None, 4, None)))),
        )

    def test_insertion_abr_case2(self) -> None:
        self.assertEqual(
            insertion_abr(self.abr1, -5),
            (((None, -5, None), 0, None), 1, (None, 2, (None, 3, None))),
        )

    def test_insertion_abr_case3(self) -> None:
        self.assertEqual(
            insertion_abr(self.abr1, 2),
            ((None, 0, None), 1, (None, 2, (None, 3, None))),
        )

    def test_empaqueter_case_1(self) -> None:
        self.assertEqual(empaqueter([1, 2, 3, 4, 5], 10), 2)

    def test_empaqueter_case_2(self) -> None:
        self.assertEqual(empaqueter([1, 2, 3, 4, 5], 5), 4)

    def test_empaqueter_case_3(self) -> None:
        self.assertEqual(empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11), 5)


if __name__ == "__main__":
    main()
