from unittest import TestCase, main


def liste_puissances(a: int, n: int) -> list[int]:
    return [a ** (i + 1) for i in range(n)]


def liste_puissances_borne(a: int, borne: int) -> list[int]:
    res = []
    n = 1
    while (calc := a**n) < borne:
        res.append(calc)
        n += 1
    return res


dico = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


def codes_parfait(mot: str) -> tuple[int, int, bool]:
    """Renvoie un triplet
    (code_additionne, code_concatene, mot_est_parfait) où :
    - code_additionne est la somme des codes des lettres du mot ;
    - code_concatene est le code des lettres du mot concaténées ;
    - mot_est_parfait est un booléen indiquant si le mot est parfait."""
    code_concatene: str | int = ""
    code_additionne = 0
    for c in mot:
        code_concatene = str(code_concatene) + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    mot_est_parfait = not (code_concatene % code_additionne)
    return code_additionne, code_concatene, mot_est_parfait


class TestSujet19(TestCase):
    def test_liste_puissance_case_1(self) -> None:
        self.assertListEqual(liste_puissances(3, 5), [3, 9, 27, 81, 243])

    def test_liste_puissance_case_2(self) -> None:
        self.assertListEqual(liste_puissances(-2, 4), [-2, 4, -8, 16])

    def test_liste_puissance_case_3(self) -> None:
        self.assertListEqual(liste_puissances_borne(2, 16), [2, 4, 8])

    def test_liste_puissance_case_4(self) -> None:
        self.assertListEqual(liste_puissances_borne(2, 17), [2, 4, 8, 16])

    def test_liste_puissance_case_5(self) -> None:
        self.assertListEqual(liste_puissances_borne(5, 5), [])

    def test_codes_parfait_case_1(self) -> None:
        self.assertTupleEqual(codes_parfait("PAUL"), (50, 1612112, False))

    def test_codes_parfait_case_2(self) -> None:
        self.assertTupleEqual(codes_parfait("ALAIN"), (37, 1121914, True))


if __name__ == "__main__":
    main()
