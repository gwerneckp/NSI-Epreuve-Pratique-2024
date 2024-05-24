from unittest import TestCase, main


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
    def test_traduire_romain_case_1(self) -> None:
        self.assertEqual(traduire_romain("XIV"), 14)

    def test_traduire_romain_case_2(self) -> None:
        self.assertEqual(traduire_romain("CXLII"), 142)

    def test_traduire_romain_case_3(self) -> None:
        self.assertEqual(traduire_romain("MMXXIV"), 2024)


if __name__ == "__main__":
    main()
