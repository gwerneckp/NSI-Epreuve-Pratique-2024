from unittest import TestCase, main


def fusion(tab1: list[int], tab2: list[int]) -> list[int]:
    return sorted(tab1 + tab2)


romains = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def traduire_romain(nombre: str) -> int:
    """Renvoie l'écriture décimale du nombre donné en chiffres
    romains"""
    if len(nombre) == 1:
        return romains[nombre[0]]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]


class TestSujet30(TestCase):
    def test_fusion_case_1(self) -> None:
        self.assertEqual(fusion([3, 5], [2, 5]), [2, 3, 5, 5])

    def test_fusion_case_2(self) -> None:
        self.assertEqual(fusion([-2, 4], [-3, 5, 10]), [-3, -2, 4, 5, 10])

    def test_fusion_case_3(self) -> None:
        self.assertEqual(fusion([4], [2, 6]), [2, 4, 6])

    def test_fusion_case_4(self) -> None:
        self.assertEqual(fusion([], []), [])

    def test_fusion_case_5(self) -> None:
        self.assertEqual(fusion([1, 2, 3], []), [1, 2, 3])

    def test_traduire_romain_case_1(self) -> None:
        self.assertEqual(traduire_romain("XIV"), 14)

    def test_traduire_romain_case_2(self) -> None:
        self.assertEqual(traduire_romain("CXLII"), 142)

    def test_traduire_romain_case_3(self) -> None:
        self.assertEqual(traduire_romain("MMXXIV"), 2024)


if __name__ == "__main__":
    main()
