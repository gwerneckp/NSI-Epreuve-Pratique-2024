from unittest import TestCase, main

>>> recherche([2, 3, 4, 5, 6], 5)
3
>>> recherche([2, 3, 4, 6, 7], 5) # renvoie None

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for ... in message: 
        if 'A' <= c and c <= 'Z':
            indice = (...) % 26 
            resultat = resultat + alphabet[indice]
        else:
            resultat = ... 
    return resultat

class TestSujet46(TestCase):
    def test_cesar_case_1(self) -> None:
        self.assertEqual(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4), 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !')

    def test_cesar_case_2(self) -> None:
        self.assertEqual(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5), 'BONJOUR A TOUS. VIVE LA MATIERE NSI !')

if __name__ == "__main__":
    main()