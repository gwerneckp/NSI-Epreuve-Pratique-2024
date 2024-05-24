from unittest import TestCase, main
from random import randint


def tri_selection(tab: list[int]) -> list[int]:
    for i in range(len(tab)):
        min_pos = i
        for j in range(i, len(tab)):
            if tab[j] < tab[min_pos]:
                min_pos = j
        tab[i], tab[min_pos] = tab[min_pos], tab[i]

    return tab


def plus_ou_moins() -> None:
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0

    while nb_mystere != nb_test and compteur < 11.0:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre était ", nb_mystere)


class TestSujet12(TestCase):
    def test_tri_selection_case_1(self) -> None:
        self.assertListEqual(tri_selection([1, 52, 6, -9, 12]), [-9, 1, 6, 12, 52])

    def test_tri_selection_case_2(self) -> None:
        self.assertListEqual(tri_selection([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_tri_selection_empty_list(self) -> None:
        self.assertListEqual(tri_selection([]), [])


if __name__ == "__main__":
    plus_ou_moins()
    main()
