from unittest import TestCase, main

a = {
    "F": ["B", "G"],
    "B": ["A", "D"],
    "A": ["", ""],
    "D": ["C", "E"],
    "C": ["", ""],
    "E": ["", ""],
    "G": ["", "I"],
    "I": ["", "H"],
    "H": ["", ""],
}


# Votre code
def taille(arbre: dict[list[str]], lettre: str):
    if not arbre[lettre][0] and not arbre[lettre][1]:
        return 1
    if not arbre[lettre][0]:
        return 1 + taille(arbre, arbre[lettre][1])
    if not arbre[lettre][1]:
        return 1 + taille(arbre, arbre[lettre][0])
    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])


def echange(tab: list, i: int, j: int) -> None:
    """Echange les éléments d'indice i et j dans le tableau tab."""
    # temp = tab[i]
    # tab[i] = tab[j]
    # tab[j] = temp
    tab[i], tab[j] = tab[j], tab[i]


def tri_selection(tab: list[int]) -> list[int]:
    """Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection."""
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(k, N):
            if tab[i] < tab[imin]:
                imin = i
        echange(tab, imin, k)
    return tab


class TestSujet01(TestCase):
    def test_taille(self):
        self.assertEqual(taille(a, "F"), 9)
        self.assertEqual(taille(a, "B"), 5)
        self.assertEqual(taille(a, "I"), 2)

    def test_echange(self):
        a = [1, 2, 3]
        echange(a, 0, 2)
        self.assertEqual([3, 2, 1], a)

    def test_sort(self):
        b = [324, 1, 6, 0, 1]
        self.assertEqual(sorted(b), tri_selection(b))

    def test_sort_empty_list(self):
        self.assertEqual([], tri_selection([]))


if __name__ == "__main__":
    main()
