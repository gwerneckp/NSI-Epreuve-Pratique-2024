from random import randint
from unittest import TestCase, main


def lancer(n: int) -> list[int]:
    return [randint(1, 6) for _ in range(n)]


def paire_6(tab: list[int]) -> bool:
    return tab.count(6) >= 2


def nombre_lignes(image: list[list[int]]) -> int:
    """renvoie le nombre de lignes de l'image"""
    return len(image)


def nombre_colonnes(image: list[list[int]]) -> int:
    """renvoie la largeur de l'image"""
    return len(image[0])


def negatif(image: list[list[int]]) -> list[list[int]]:
    """renvoie le negatif de l'image sous la forme
    d'une liste de listes"""
    # on cree une image de 0 aux memes dimensions
    # que le parametre image
    
    # nouvelle_image = [
    #     [0 for k in range(nombre_colonnes(image))] for i in range(nombre_lignes(image))
    # ]

    # for i in range(nombre_lignes(image)):
    #     for j in range(nombre_colonnes(image)):
    #         nouvelle_image[i][j] = 255 - image[i][j]
    # return nouvelle_image

    return [
        [255 - image[i][j] for j in range(nombre_colonnes(image))]
        for i in range(nombre_lignes(image))
    ]


def binaire(image: list[list[int]], seuil: int) -> list[list[int]]:
    """renvoie une image binarisee de l'image sous la forme
    d'une liste de listes contenant des 0 si la valeur
    du pixel est strictement inferieure au seuil et 1 sinon"""
    # nouvelle_image = [[0] * nombre_colonnes(image) for i in range(nombre_lignes(image))]

    # for i in range(nombre_lignes(image)):
    #     for j in range(nombre_colonnes(image)):
    #         if image[i][j] < seuil:
    #             nouvelle_image[i][j] = 0
    #         else:
    #             nouvelle_image[i][j] = 1
    # return nouvelle_image

    return [
        [0 if image[i][j] < seuil else 1 for j in range(nombre_colonnes(image))]
        for i in range(nombre_lignes(image))
    ]


class TestSujet20(TestCase):
    def test_lancer(self) -> None:
        n = 200
        result = lancer(n)
        self.assertEqual(len(result), n)
        for v in result:
            self.assertGreaterEqual(v, 1)
            self.assertLessEqual(v, 6)

    def test_paire_6_case1(self) -> None:
        lancer1 = [5, 6, 6, 2, 2]
        self.assertEqual(paire_6(lancer1), True)

    def test_paire_6_case2(self) -> None:
        lancer2 = [6, 5, 1, 6, 6]
        self.assertEqual(paire_6(lancer2), True)

    def test_paire_6_case3(self) -> None:
        lancer3 = [2, 2, 6]
        self.assertEqual(paire_6(lancer3), False)

    def test_paire_6_case4(self) -> None:
        lancer4: list[int] = []
        self.assertEqual(paire_6(lancer4), False)

    def test_nombre_lignes(self) -> None:
        img = [
            [20, 34, 254, 145, 6],
            [23, 124, 237, 225, 69],
            [197, 174, 207, 25, 87],
            [255, 0, 24, 197, 189],
        ]
        self.assertEqual(nombre_lignes(img), 4)

    def test_nombre_colonnes(self) -> None:
        img = [
            [20, 34, 254, 145, 6],
            [23, 124, 237, 225, 69],
            [197, 174, 207, 25, 87],
            [255, 0, 24, 197, 189],
        ]
        self.assertEqual(nombre_colonnes(img), 5)

    def test_negatif(self) -> None:
        img = [
            [20, 34, 254, 145, 6],
            [23, 124, 237, 225, 69],
            [197, 174, 207, 25, 87],
            [255, 0, 24, 197, 189],
        ]
        self.assertEqual(
            negatif(img),
            [
                [235, 221, 1, 110, 249],
                [232, 131, 18, 30, 186],
                [58, 81, 48, 230, 168],
                [0, 255, 231, 58, 66],
            ],
        )

    def test_binaire(self) -> None:
        img = [
            [20, 34, 254, 145, 6],
            [23, 124, 237, 225, 69],
            [197, 174, 207, 25, 87],
            [255, 0, 24, 197, 189],
        ]
        self.assertEqual(
            binaire(img, 120),
            [[0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 1]],
        )


if __name__ == "__main__":
    main()
