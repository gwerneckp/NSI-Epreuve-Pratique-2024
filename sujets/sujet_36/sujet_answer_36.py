from unittest import TestCase, main

valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return ...
    v = valeurs[rang]
    if v <= ... :
        return ... + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, ...)

>>>rendu_glouton(67, 0)
[50, 10, 5, 2]
>>>rendu_glouton(291, 0)
[100, 100, 50, 20, 20, 1]
>>> rendu_glouton(291,1) # si on ne dispose pas de billets de 100
[50, 50, 50, 50, 50, 20, 20, 1]

class TestSujet36(TestCase):
    def test_occurrences_case_1(self) -> None:
        self.assertEqual(occurrences('e', "sciences"), 2)

    def test_occurrences_case_2(self) -> None:
        self.assertEqual(occurrences('i',"mississippi"), 4)

    def test_occurrences_case_3(self) -> None:
        self.assertEqual(occurrences('a',"mississippi"), 0)

if __name__ == "__main__":
    main()