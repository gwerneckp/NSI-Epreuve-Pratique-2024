from unittest import TestCase, main

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = ... 
    for caractere in chaine:
        resultat = ... 
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return ... 

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
    chaine = ... 
    return est_palindrome(chaine)

class TestSujet35(TestCase):
    def test_annee_temperature_minimale_case_1(self) -> None:
        self.assertEqual(annee_temperature_minimale(t_moy, annees), (12.5, 2016))

    def test_inverse_chaine_case_1(self) -> None:
        self.assertEqual(inverse_chaine('bac'), 'cab')

    def test_inverse_chaine_case_2(self) -> None:
        self.assertFalse(est_palindrome('NSI'))

    def test_inverse_chaine_case_3(self) -> None:
        self.assertTrue(est_palindrome('ISN-NSI'))

    def test_inverse_chaine_case_4(self) -> None:
        self.assertFalse(est_nbre_palindrome(214312))

    def test_inverse_chaine_case_5(self) -> None:
        self.assertTrue(est_nbre_palindrome(213312))

if __name__ == "__main__":
    main()