from unittest import TestCase, main


def moyenne(notes: list[tuple[float, int]]) -> float:
    total: float = 0
    coefficient: int = 0
    for note, coefficient in notes:
        total += note * coefficient
        coefficient += coefficient
    return total / coefficient


def ligne_suivante(ligne: list[int]) -> list[int]:
    """Renvoie la ligne suivant ligne du triangle de Pascal"""
    ligne_suiv = [1]
    for i in range(len(ligne) - 1):
        ligne_suiv.append(ligne[i + 1] + ligne[i])
    ligne_suiv.append(1)

    return ligne_suiv


def pascal(n: int) -> list[list[int]]:
    """Renvoie le triangle de Pascal de hauteur n"""
    triangle = [[1]]
    for k in range(n):
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)
    return triangle


class TestSujet29(TestCase):
    def test_moyenne_case_1(self) -> None:
        self.assertEqual(moyenne([(15.0, 2), (9.0, 1), (12.0, 3)]), 12.5)

    def test_ligne_suivante_case_1(self) -> None:
        self.assertEqual(ligne_suivante([1, 3, 3, 1]), [1, 4, 6, 4, 1])

    def test_ligne_suivante_case_2(self) -> None:
        self.assertEqual(pascal(2), [[1], [1, 1], [1, 2, 1]])

    def test_ligne_suivante_case_3(self) -> None:
        self.assertEqual(pascal(3), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])


if __name__ == "__main__":
    main()
