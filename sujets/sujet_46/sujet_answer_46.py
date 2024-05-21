from unittest import TestCase, main


def recherche(tab: list[int], n: int) -> int | None:
    i, j = 0, len(tab) - 1

    while i <= j:
        m = (i + j) // 2
        if tab[m] == n:
            return m

        if tab[m] > n:
            j = m - 1

        i = m + 1

    return None


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def position_alphabet(lettre: str) -> int:
    """Renvoie la position de la lettre dans l'alphabet"""
    return ord(lettre) - ord("A")


def cesar(message: str, decalage: int) -> str:
    """Renvoie le message codé par la méthode de César
    pour le decalage donné"""
    resultat = ""
    for c in message:
        if "A" <= c and c <= "Z":
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c
    return resultat


class TestSujet46(TestCase):
    def test_recherche_case_1(self) -> None:
        self.assertEqual(recherche([2, 3, 4, 5, 6], 5), 3)

    def test_recherche_case_2(self) -> None:
        self.assertEqual(recherche([1, 3, 5, 7, 9], 5), 2)

    def test_recherche_case_none(self) -> None:
        self.assertIsNone(recherche([2, 3, 4, 6, 7], 5))

    def test_cesar_case_1(self) -> None:
        self.assertEqual(
            cesar("BONJOUR A TOUS. VIVE LA MATIERE NSI !", 4),
            "FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !",
        )

    def test_cesar_case_2(self) -> None:
        self.assertEqual(
            cesar("GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !", -5),
            "BONJOUR A TOUS. VIVE LA MATIERE NSI !",
        )


if __name__ == "__main__":
    main()
