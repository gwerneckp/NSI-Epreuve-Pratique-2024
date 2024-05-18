from unittest import TestCase, main

def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = ... 
    while pile != []:
        ... .append(...) 
    return ... 


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = ... 
    while pile != []:
        ... = pile.pop() 
        if ... >= 0: 
            ...
    return ...

class TestSujet38(TestCase):
    def test_indices_maxi_case_1(self) -> None:
        self.assertEqual(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]), (9, [3, 8]))

    def test_indices_maxi_case_2(self) -> None:
        self.assertEqual(indices_maxi([7]), (7, [0]))

    def test_renverse_case_1(self) -> None:
        self.assertEqual(renverse([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_renverse_case_2(self) -> None:
        self.assertEqual(positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]), [0, 5, 4, 10, 9])

    def test_renverse_case_3(self) -> None:
        self.assertEqual(positifs([-2]), [])

if __name__ == "__main__":
    main()