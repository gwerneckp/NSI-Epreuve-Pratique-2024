  
import unittest
import ep_sujets

class TestEpSujets(unittest.TestCase):

    def test_taille(self):
        a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
            'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
            'H':['','']}
        self.assertEqual(ep_sujets.taille(a, 'F'),9)
        self.assertEqual(ep_sujets.taille(a, 'B'),5)
        self.assertEqual(ep_sujets.taille(a, 'I'),2)
    
    def test_tri_selection(self):
        self.assertEqual(ep_sujets.tri_selection([41, 55, 21, 18, 12, 6, 25]), [6, 12, 18, 21, 25, 41, 55])
        self.assertEqual(ep_sujets.tri_selection([5, 3, 4, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(ep_sujets.tri_selection([]), [])
        self.assertEqual(ep_sujets.tri_selection([1]), [1])

if __name__ == '__main__':
    unittest.main()