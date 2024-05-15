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


# def codes_parfait(mot):
#     """Renvoie un triplet
#     (code_additionne, code_concatene, mot_est_parfait) où :
#     - code_additionne est la somme des codes des lettres du mot ;
#     - code_concatene est le code des lettres du mot concaténées ;
#     - mot_est_parfait est un booléen indiquant si le mot est parfait."""
#     code_concatene = ""
#     code_additionne = ...
#     for c in mot:
#         code_concatene = code_concatene + ...
#         code_additionne = code_additionne + ...
#     code_concatene = int(code_concatene)
#     mot_est_parfait = ...
#     return code_additionne, code_concatene, mot_est_parfait


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


if __name__ == "__main__":
    main()
