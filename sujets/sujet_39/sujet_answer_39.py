from typing import Optional
from unittest import TestCase, main


def recherche(elt: int, tab: list[int]) -> int | None:
    last_i: int | None = None
    for i in range(len(tab)):
        if tab[i] == elt:
            last_i = i
    return last_i


class AdresseIP:
    def __init__(self, adresse: str):
        self.adresse = adresse

    def liste_octets(self) -> list[int]:
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split découpe la chaine de caractères
        # en fonction du séparateur
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self) -> bool:
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        reservees = ["192.168.0.0", "192.168.0.255"]
        return self.adresse in reservees

    def adresse_suivante(self) -> Optional["AdresseIP"]:
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = self.liste_octets()
        if octets[-1] == 254:
            return None
        octet_nouveau = octets[-1] + 1
        return AdresseIP("192.168.0." + str(octet_nouveau))


class TestSujet39(TestCase):
    def test_recherche_case_none(self) -> None:
        self.assertIsNone(recherche(1, [2, 3, 4]))

    def test_recherche_case_1(self) -> None:
        self.assertEqual(recherche(1, [10, 12, 1, 56]), 2)

    def test_recherche_case_2(self) -> None:
        self.assertEqual(recherche(1, [1, 0, 42, 7]), 0)

    def test_recherche_case_3(self) -> None:
        self.assertEqual(recherche(1, [1, 50, 1]), 2)

    def test_recherche_case_4(self) -> None:
        self.assertEqual(recherche(1, [8, 1, 10, 1, 7, 1, 8]), 5)

    def setUp(self) -> None:
        self.adresse1 = AdresseIP("192.168.0.1")
        self.adresse2 = AdresseIP("192.168.0.2")
        self.adresse3 = AdresseIP("192.168.0.0")
        return super().setUp()

    def test_adresse1_liste_octets_case_1(self) -> None:
        self.assertEqual(self.adresse1.liste_octets(), [192, 168, 0, 1])

    def test_adresse1_liste_octets_case_2(self) -> None:
        self.assertFalse(self.adresse1.est_reservee())

    def test_adresse1_liste_octets_case_3(self) -> None:
        self.assertTrue(self.adresse3.est_reservee())

    def test_adresse1_liste_octets_case_4(self) -> None:
        assert (adresseSuiv := self.adresse2.adresse_suivante()) is not None
        self.assertEqual(adresseSuiv.adresse, "192.168.0.3")


if __name__ == "__main__":
    main()
