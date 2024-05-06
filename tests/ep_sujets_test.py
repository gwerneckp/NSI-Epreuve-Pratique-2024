  
import unittest
from Epreuve_Pratique import ep_sujets

class TestEpSujets(unittest.TestCase):

    def test_taille_1_1(self):
        a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
            'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
            'H':['','']}
        self.assertEqual(ep_sujets.taille(a, 'F'),9)
        self.assertEqual(ep_sujets.taille(a, 'B'),5)
        self.assertEqual(ep_sujets.taille(a, 'I'),2)
    
    def test_tri_selection_1_2(self):
        self.assertEqual(ep_sujets.tri_selection([41, 55, 21, 18, 12, 6, 25]), [6, 12, 18, 21, 25, 41, 55])
        self.assertEqual(ep_sujets.tri_selection([5, 3, 4, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(ep_sujets.tri_selection([]), [])
        self.assertEqual(ep_sujets.tri_selection([1]), [1])

    def test_correspond_2_1(self):
        self.assertEqual(ep_sujets.correspond('INFORMATIQUE', 'INFO*MA*IQUE'), True)
        self.assertEqual(ep_sujets.correspond('AUTOMATIQUE', 'INFO*MA*IQUE'), False)
        self.assertEqual(ep_sujets.correspond('STOP', 'S*'), False)
        self.assertEqual(ep_sujets.correspond('AUTO', '*UT*'), True)

    def test_est_cyclique_2_2(self):
        self.assertEqual(ep_sujets.est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}), False)
        self.assertEqual(ep_sujets.est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'}), True)
        self.assertEqual(ep_sujets.est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'}), True)
        self.assertEqual(ep_sujets.est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'}), False)

    def test_maximum_tableau_3_1(self):
        self.assertEqual(ep_sujets.maximum_tableau([98, 12, 104, 23, 131, 9]), 131)
        self.assertEqual(ep_sujets.maximum_tableau([-27, 24, -3, 15]), 24)

    def test_bon_parenthesage_3_2(self):
        self.assertEqual(ep_sujets.bon_parenthesage("((()())(()))"), True)
        self.assertEqual(ep_sujets.bon_parenthesage("())(()"), False)
        self.assertEqual(ep_sujets.bon_parenthesage("(())(()"), False)

    def test_recherche_4_1(self):
        self.assertEqual(ep_sujets.recherche([5, 3], 1), None)
        self.assertEqual(ep_sujets.recherche([2, 4], 2), 0)
        self.assertEqual(ep_sujets.recherche([2, 3, 5, 2, 4], 2), 3)

    def test_distance_carre_4_2(self):
        self.assertEqual(ep_sujets.distance_carre((1, 0), (5, 3)), 25)
        self.assertEqual(ep_sujets.distance_carre((1, 0), (0, 1)), 2)

    def test_point_le_plus_proche_4_2(self):
        self.assertEqual(ep_sujets.point_le_plus_proche((0, 0), [(7, 9), (2, 5), (5, 2)]), (2, 5))
        self.assertEqual(ep_sujets.point_le_plus_proche((5, 2), [(7, 9), (2, 5), (5, 2)]), (5, 2))

    def test_max_et_indice_5_1(self):
        self.assertEqual(ep_sujets.max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]), (9, 3))
        self.assertEqual(ep_sujets.max_et_indice([-2]), (-2, 0))
        self.assertEqual(ep_sujets.max_et_indice([-1, -1, 3, 3, 3]), (3, 2))
        self.assertEqual(ep_sujets.max_et_indice([1, 1, 1, 1]), (1, 0))

    def test_est_un_ordre_5_2(self):
        self.assertEqual(ep_sujets.est_un_ordre([1, 6, 2, 8, 3, 7]), False)
        self.assertEqual(ep_sujets.est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]), True)

    def test_nombre_points_rupture_5_2(self):
        self.assertEqual(ep_sujets.nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]), 4)
        self.assertEqual(ep_sujets.nombre_points_rupture([1, 2, 3, 4, 5]), 0)
        self.assertEqual(ep_sujets.nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]), 7)
        self.assertEqual(ep_sujets.nombre_points_rupture([2, 1, 3, 4]), 2)

    def test_verifie_6_1(self):
        self.assertEqual(ep_sujets.verifie([0, 5, 8, 8, 9]), True)
        self.assertEqual(ep_sujets.verifie([8, 12, 4]), False)
        self.assertEqual(ep_sujets.verifie([-1, 4]), True)
        self.assertEqual(ep_sujets.verifie([]), True)
        self.assertEqual(ep_sujets.verifie([5]), True)

    def test_depouille_6_2(self):
        self.assertEqual(ep_sujets.depouille(['A', 'B', 'A']), {'A': 2, 'B': 1})
        self.assertEqual(ep_sujets.depouille([]), {})
        self.assertEqual(ep_sujets.depouille(['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']), {'A': 3, 'B': 4, 'C': 3})

    def test_vainqueurs_6_2(self):
        self.assertEqual(ep_sujets.vainqueurs({'A': 3, 'B': 4, 'C': 3}), ['B'])
        self.assertEqual(ep_sujets.vainqueurs({'A': 2, 'B': 2, 'C': 1}), ['A', 'B'])

    def test_gb_vers_entier_7_1(self):
        self.assertEqual(ep_sujets.gb_vers_entier([]), 0)
        self.assertEqual(ep_sujets.gb_vers_entier([True]), 1)
        self.assertEqual(ep_sujets.gb_vers_entier([True, False, True, False, False, True, True]), 83)
        self.assertEqual(ep_sujets.gb_vers_entier([True, False, False, False, False, False, True, False]), 130)

    def test_tri_insertion_7_2(self):
        self.assertEqual(ep_sujets.tri_insertion([98, 12, 104, 23, 131, 9]), [9, 12, 23, 98, 104, 131])

    def test_delta_8_1(self):
        self.assertEqual(ep_sujets.delta([1000, 800, 802, 1000, 1003]), [1000, -200, 2, 198, 3])
        self.assertEqual(ep_sujets.delta([42]), [42])

    def test_infixe_8_2(self):
        a = ep_sujets.Expr(ep_sujets.Expr(None, 1, None), '+', ep_sujets.Expr(None, 2, None))
        self.assertEqual(a.infixe(), '(1+2)')
        b = ep_sujets.Expr(ep_sujets.Expr(ep_sujets.Expr(None, 1, None), '+', ep_sujets.Expr(None, 2, None)), '*', ep_sujets.Expr(ep_sujets.Expr(None, 3, None), '+', ep_sujets.Expr(None, 4, None)))
        self.assertEqual(b.infixe(), '((1+2)*(3+4))')
        e = ep_sujets.Expr(ep_sujets.Expr(ep_sujets.Expr(None, 3, None), '*', ep_sujets.Expr(ep_sujets.Expr(None, 8, None), '+', ep_sujets.Expr(None, 7, None))), '-', ep_sujets.Expr(ep_sujets.Expr(None, 2, None), '+', ep_sujets.Expr(None, 1, None)))
        self.assertEqual(e.infixe(), '((3*(8+7))-(2+1))')

    def test_effectif_notes_9_1(self):
        notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
        self.assertEqual(ep_sujets.effectif_notes(notes_eval), [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1])

    def test_notes_triees_9_1(self):
        self.assertEqual(ep_sujets.notes_triees([2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]), [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10])

    def test_dec_to_bin_9_2(self):
        self.assertEqual(ep_sujets.dec_to_bin(25), '11001')

    def test_bin_to_dec_9_2(self):
        self.assertEqual(ep_sujets.bin_to_dec('101010'), 42)

    def test_moyenne_10_1(self):
        self.assertEqual(ep_sujets.moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]), 9.142857142857142)
        self.assertEqual(ep_sujets.moyenne([(3, 0), (5, 0)]), None)

    def test_liste_zoom_10_2(self):
        self.assertEqual(ep_sujets.liste_zoom([1,2,3],3), [1, 1, 1, 2, 2, 2, 3, 3, 3])

    def test_nombre_de_mots_11_1(self):
        self.assertEqual(ep_sujets.nombre_de_mots('Cet exercice est simple.'), 4)
        self.assertEqual(ep_sujets.nombre_de_mots('Le point d exclamation est séparé !'), 6)
        self.assertEqual(ep_sujets.nombre_de_mots('Combien de mots y a t il dans cette phrase ?'), 10)
        self.assertEqual(ep_sujets.nombre_de_mots('Fin.'), 1)

    def test_inserer_11_2(self):
        arbre = ep_sujets.Noeud(7)
        for cle in (3, 9, 1, 6):
            arbre.inserer(cle)
        self.assertEqual(arbre.gauche.etiquette, 3)
        self.assertEqual(arbre.droit.etiquette, 9)
        self.assertEqual(arbre.gauche.gauche.etiquette, 1)
        self.assertEqual(arbre.gauche.droit.etiquette, 6)
    
    def test_tri_selection_12_1(self):
        tab = [1, 52, 6, -9, 12]
        self.assertEqual(ep_sujets.tri_selection(tab), [-9, 1, 6, 12, 52])

    def test_recherche_13_1(self):
        self.assertEqual(ep_sujets.recherche(1, [2, 3, 4]), None)
        self.assertEqual(ep_sujets.recherche(1, [10, 12, 1, 56]), 2)
        self.assertEqual(ep_sujets.recherche(50, [1, 50, 1]), 1)
        self.assertEqual(ep_sujets.recherche(15, [8, 9, 10, 15]), 3)

    def test_insere_13_2(self):
        self.assertEqual(ep_sujets.insere([1, 2, 4, 5], 3), [1, 2, 3, 4, 5])
        self.assertEqual(ep_sujets.insere([1, 2, 7, 12, 14, 25], 30), [1, 2, 7, 12, 14, 25, 30])
        self.assertEqual(ep_sujets.insere([2, 3, 4], 1), [1, 2, 3, 4])
        self.assertEqual(ep_sujets.insere([], 1), [1])


    def test_min_et_max_14_1(self):
        self.assertEqual(ep_sujets.min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]), {'min': -2, 'max': 9})
        self.assertEqual(ep_sujets.min_et_max([0, 1, 2, 3]), {'min': 0, 'max': 3})
        self.assertEqual(ep_sujets.min_et_max([3]), {'min': 3, 'max': 3})
        self.assertEqual(ep_sujets.min_et_max([1, 3, 2, 1, 3]), {'min': 1, 'max': 3})
        self.assertEqual(ep_sujets.min_et_max([-1, -1, -1, -1, -1]), {'min': -1, 'max': -1})

    def test_paquet_de_cartes_14_2(self):
        jeu = ep_sujets.Paquet_de_cartes()
        carte1 = jeu.recuperer_carte(20)
        self.assertEqual(carte1.recuperer_valeur() + " de " + carte1.recuperer_couleur(), "8 de coeur")
        carte2 = jeu.recuperer_carte(0)
        self.assertEqual(carte2.recuperer_valeur() + " de " + carte2.recuperer_couleur(), "As de pique")
        with self.assertRaises(AssertionError):
            carte3 = jeu.recuperer_carte(52)

    def test_moyenne_15_1(self):
        self.assertEqual(ep_sujets.moyenne([1.0]), 1.0)
        self.assertEqual(ep_sujets.moyenne([1.0, 2.0, 4.0]), 2.3333333333333335)

    def test_binaire_15_2(self):
        self.assertEqual(ep_sujets.binaire(83), '1010011')
        self.assertEqual(ep_sujets.binaire(127), '1111111')
        self.assertEqual(ep_sujets.binaire(0), '0')

    def test_ecriture_binaire_entier_positif_16_1(self):
        self.assertEqual(ep_sujets.ecriture_binaire_entier_positif(0), '0')
        self.assertEqual(ep_sujets.ecriture_binaire_entier_positif(2), '10')
        self.assertEqual(ep_sujets.ecriture_binaire_entier_positif(105), '1101001')

    def test_tri_bulles_16_2(self):
        self.assertEqual(ep_sujets.tri_bulles_16_2([]), [])
        self.assertEqual(ep_sujets.tri_bulles([9, 3, 7, 2, 3, 1, 6]), [1, 2, 3, 3, 6, 7, 9])
        self.assertEqual(ep_sujets.tri_bulles([9, 7, 4, 3]), [3, 4, 7, 9])

    def test_nb_repetitions_17_1(self):
        self.assertEqual(ep_sujets.nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]), 3)
        self.assertEqual(ep_sujets.nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']), 2)
        self.assertEqual(ep_sujets.nb_repetitions(12, [1, 3, 7, 21, 36, 44]), 0)

    def test_binaire_17_2(self):
        self.assertEqual(ep_sujets.binaire(0), '0')
        self.assertEqual(ep_sujets.binaire(77), '1001101')

    def test_multiplication_18_1(self):
        self.assertEqual(ep_sujets.multiplication(3,5), 15)
        self.assertEqual(ep_sujets.multiplication(-4,-8), 32)
        self.assertEqual(ep_sujets.multiplication(-2,6), -12)
        self.assertEqual(ep_sujets.multiplication(-2,0), 0)

    def test_chercher_18_2(self):
        self.assertEqual(ep_sujets.chercher([1, 5, 6, 6, 9, 12], 7, 0, 10), None)
        self.assertEqual(ep_sujets.chercher([1, 5, 6, 6, 9, 12], 7, 0, 5), None)
        self.assertEqual(ep_sujets.chercher([1, 5, 6, 6, 9, 12], 9, 0, 5), 4)
        self.assertEqual(ep_sujets.chercher([1, 5, 6, 6, 9, 12], 6, 0, 5), 2)

    def test_liste_puissances_19_1(self):
        self.assertEqual(ep_sujets.liste_puissances(3, 5), [3, 9, 27, 81, 243])
        self.assertEqual(ep_sujets.liste_puissances(-2, 4), [-2, 4, -8, 16])
        self.assertEqual(ep_sujets.liste_puissances_borne(2, 16), [2, 4, 8])
        self.assertEqual(ep_sujets.liste_puissances_borne(2, 17), [2, 4, 8, 16])
        self.assertEqual(ep_sujets.liste_puissances_borne(5, 5), [])

    def test_codes_parfait_19_2(self):
        self.assertEqual(ep_sujets.codes_parfait("PAUL"), (50, 1612112, False))
        self.assertEqual(ep_sujets.codes_parfait("ALAIN"), (37, 1121914, True))

    def test_lancer_20_1(self):
        self.assertEqual(len(ep_sujets.lancer(5)), 5)
        self.assertEqual(len(ep_sujets.lancer(0)), 0)

    def test_paire_6_20_1(self):
        self.assertEqual(ep_sujets.paire_6([5, 6, 6, 2, 2]), True)
        self.assertEqual(ep_sujets.paire_6([6, 5, 1, 6, 6]), True)
        self.assertEqual(ep_sujets.paire_6([2, 2, 6]), False)
        self.assertEqual(ep_sujets.paire_6([]), False)

    def test_nombre_lignes_20_2(self):
        img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69],[197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
        self.assertEqual(ep_sujets.nombre_lignes(img), 4)

    def test_nombre_colonnes_20_2(self):
        img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69],[197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
        self.assertEqual(ep_sujets.nombre_colonnes(img), 5)

    def test_negatif_20_2(self):
        img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69],[197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
        self.assertEqual(ep_sujets.negatif(img), [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186],[58, 81, 48, 230, 168], [0, 255, 231, 58, 66]])

    def test_binaire_20_2(self):
        img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69],[197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
        self.assertEqual(ep_sujets.binaire(img, 120), [[0, 0, 1, 1, 0],[0, 1, 1, 1, 0],[1, 1, 1, 0, 0],[1, 0, 0, 1, 1]])

    def test_recherche_motif_21_1(self):
        self.assertEqual(ep_sujets.recherche_motif("ab", ""), [])
        self.assertEqual(ep_sujets.recherche_motif("ab", "cdcdcdcd"), [])
        self.assertEqual(ep_sujets.recherche_motif("ab", "abracadabra"), [0, 7])
        self.assertEqual(ep_sujets.recherche_motif("ab", "abracadabraab"), [0, 7, 11])

    def test_accessibles_21_2(self):
        self.assertEqual(ep_sujets.accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0), [0, 1, 2, 3])
        self.assertEqual(ep_sujets.accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4), [4, 5])

    def test_recherche_indices_classement_22_1(self):
        self.assertEqual(ep_sujets.recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]), ([0, 3, 7], [1, 6], [2, 4, 5]))
        self.assertEqual(ep_sujets.recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]), ([0, 2, 5], [], [1, 3, 4]))
        self.assertEqual(ep_sujets.recherche_indices_classement(3, [1, 1, 1, 1]), ([0, 1, 2, 3], [], []))
        self.assertEqual(ep_sujets.recherche_indices_classement(3, []), ([], [], []))

    def test_moyenne_22_2(self):
        resultats = {'Dupont': {'DS1': [15.5, 4],'DM1': [14.5, 1],'DS2': [13, 4],'PROJET1': [16, 3],'DS3': [14, 4]},
                     'Durand': {'DS1': [6 , 4],'DS2': [8, 4],'PROJET1': [9, 3],'IE1': [7, 2],'DS3': [12, 4]}}
        self.assertEqual(ep_sujets.moyenne("Dupont", resultats), 14.5)
        self.assertEqual(ep_sujets.moyenne("Durand", resultats), 8.5)

    def test_insertion_abr_23_1(self):
        n0 = (None, 0, None)
        n3 = (None, 3, None)
        n2 = (None, 2, n3)
        abr1 = (n0, 1, n2)
        self.assertEqual(ep_sujets.insertion_abr(abr1, 4), ((None,0,None),1,(None,2,(None,3,(None,4,None)))))
        self.assertEqual(ep_sujets.insertion_abr(abr1, -5), (((None,-5,None),0,None),1,(None,2,(None,3,None))))
        self.assertEqual(ep_sujets.insertion_abr(abr1, 2), ((None,0,None),1,(None,2,(None,3,None))))

    def test_empaqueter_23_2(self):
        self.assertEqual(ep_sujets.empaqueter([1, 2, 3, 4, 5], 10), 2)
        self.assertEqual(ep_sujets.empaqueter([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(ep_sujets.empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11), 5)

    def test_parcours_largeur_24_1(self):
        arbre = ( ( (None, 1, None), 2, (None, 3, None) ), 4, ( (None, 5,None), 6, (None, 7, None) ) )
        self.assertEqual(ep_sujets.parcours_largeur(arbre), [4, 2, 6, 1, 3, 5, 7])

    def test_somme_max_24_2(self):
        self.assertEqual(ep_sujets.somme_max([1, 2, 3, 4, 5]), 15)
        self.assertEqual(ep_sujets.somme_max([1, 2, -3, 4, 5]), 9)
        self.assertEqual(ep_sujets.somme_max([1, 2, -2, 4, 5]), 10)
        self.assertEqual(ep_sujets.somme_max([1, -2, 3, 10, -4, 7, 2, -5]), 18)


if __name__ == '__main__':
    unittest.main()