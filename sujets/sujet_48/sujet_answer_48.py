from unittest import TestCase, main


def voisins_entrants(adj: list[list[int]], x: int) -> list[int]:
    res: list[int] = []
    for i in range(len(adj)):
        if x in adj[i]:
            res.append(i)

    return res


def nombre_suivant(s: str) -> str:
    """Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture."""
    resultat = ""
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)):
        if s[i] == chiffre:
            compte = compte + 1
        else:
            resultat += str(compte) + chiffre
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + chiffre
    resultat += lecture_chiffre
    return resultat


class TestSujet48(TestCase):
    def test_voisins_entrants_case_1(self) -> None:
        self.assertEqual(voisins_entrants([[1, 2], [2], [0], [0]], 0), [2, 3])

    def test_voisins_entrants_case_2(self) -> None:
        self.assertEqual(voisins_entrants([[1, 2], [2], [0], [0]], 1), [0])

    def test_nombre_suivant_case_1(self) -> None:
        self.assertEqual(nombre_suivant("1211"), "111221")

    def test_nombre_suivant_case_2(self) -> None:
        self.assertEqual(nombre_suivant("311"), "1321")


if __name__ == "__main__":
    main()
