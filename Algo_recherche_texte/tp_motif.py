#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP : recherche de motif
"""

#%% Exercice 1

#%% Exo1 Q1
def premiere_occurrence_naif_slicing(motif, texte):
    """
    Paramètres : motif et texte deux chaînes de caractères
    Précondition :  0 < len(motif) <= len(texte)
    Valeur renvoyée : un entier
    Postcondition : renvoie l'index de la première occurrence de motif dans texte
    ou -1 s'il n'y a pas d'occurrence
    """
    p = len(motif)
    n = len(texte)
    assert 0 <= p <= n  # précondition
    for i in range(0, n - p + 1):
        # remplacer le slicing
        if texte[i : i + p] == motif:
            return i
    return -1


def test_premiere_occurrence_naif_slicing():
    """Tests unitaires pour la fonction premiere_occurrence_naif_slicing"""
    assert premiere_occurrence_naif_slicing("ada", "abracadabra") == 5
    assert premiere_occurrence_naif_slicing("b", "abracadabra") == 1
    assert premiere_occurrence_naif_slicing("e", "abracadabra") == -1
    # à compléter avec d'autres cas de tests pertinents
    print("Tests réussis")


#%% Exo1 Q2 Partie 1
def recherche_motif_pos(motif, texte, pos):
    """
    Paramètre : motif et texte deux chaînes de caractères et pos un entier
    Préconditions :
        0 <= len(motif) <= len(texte) et  0 <= pos + len(motif) <= len(texte)
    Valeur renvoyée : un booléen
    Postcondition : détermine si motif == texte[pos:pos+len(motif)] sans slicing
    """
    # précondition
    assert (0 <= len(motif) <= len(texte)) and (
        0 <= pos + len(motif) <= len(texte)
    )
    p = len(motif)
    # à compléter

def test_recherche_motif_pos():
    """Tests unitaires pour recherche_motif_pos"""
    assert recherche_motif_pos("abb", "ababaabba", 5)
    assert not recherche_motif_pos("abb", "ababaabba", 2)
    print("Tests réussis")


#%% Exo1 Q2 Partie 2
def premiere_occurrence_naif(motif, texte):
    """
    Paramètres : motif et texte deux chaînes de caractères
    Précondition :  0 < len(motif) <= len(texte)
    Valeur renvoyée : un entier
    Postcondition : renvoie l'index de la première occurrence de motif dans texte
    ou -1 s'il n'y a pas d'occurrence
    """
    p = len(motif)
    n = len(texte)
    assert 0 <= p <= n  # précondition
    for i in range(0, n - p + 1):
        "on remplace le slicing"
        # à compléter
    return -1


def test_premiere_occurrence_naif():
    """Tests unitaires pour premiere_occurrence_naif"""
    assert premiere_occurrence_naif("abb", "ababaabba") == 5
    assert premiere_occurrence_naif("aba", "ababaabba") == 0
    assert premiere_occurrence_naif("bba", "ababaabba") == 6
    assert premiere_occurrence_naif("bbc", "ababaabba") == -1


#%% Exo1 Q3


def recherche_motif_pos_trace(motif, texte, pos):
    """
    Paramètre : motif et texte deux chaînes de caractères et pos un entier
    Précondition :  0 < len(motif) < len(texte) et  0 <= pos + len(motif) <= len(texte)
    Valeur renvoyée : un  tuple (booléen, entier)
    Postcondition : détermine si motif == texte[i:i+len(motif)] sans slicing
    et renvoie le nombre de comparaisons effectuées
    """
    # à compléter


def premiere_occurrence_naif_trace(motif, texte, debug=False):
    n = len(texte)
    p = len(motif)
    assert 0 <= p <= n  # précondition
    nb_comparaisons = 0
    for i in range(0, n - p + 1):
        if debug:
            print("Position dans texte : ", i)
            print("Texte : ", texte)
            print("Motif : ", " " * i + motif + " " * (n - (i + p)))
            print("-" * 60)
        trouve, c = recherche_motif_pos_trace(motif, texte, i)
        nb_comparaisons += c
        if trouve:
            return (i, nb_comparaisons)
    return (-1, nb_comparaisons)


def test_premiere_occurrence_naif_trace():
    """Test unitaire pour premiere_occurrence_naif_trace"""
    # Test unitaire
    assert premiere_occurrence_naif_trace("aaabbba", "aabaaabaabcaaabbba") == (
        11,
        31,
    )
    print("Tests réussis")


#%% Exo1 Q5


def nombre_occurrence(motif, texte):
    """
    Paramètres : motif et texte deux chaînes de caractères
    Précondition :  0 < len(motif) <= len(texte)
    Valeur renvoyée : un entier
    Postcondition : renvoie le nombre d'occurrences de motif dans texte
    """
    p = len(motif)
    n = len(texte)
    assert 0 < p <= n  # précondition
    # à compléter
    return c


#%% Test sur le texte du "Rouge et le Noir"


def test_recherche_naive_rouge_noir():
    """Recherches naives de motifs dans le texte intégral du roman 'Le rouge et le noir'"""
    f = open("LeRougeEtLeNoir.txt", encoding="utf-8")
    texte = f.read()
    f.close()
    for m in ["Julien", "Mme de Rênal", "Mathilde"]:
        print(
            f"Première occurrence du motif  '{m}' dans 'LeRougeEtLeNoir.txt' :",
            premiere_occurrence_naif(m, texte),
        )
        print(
            f"Nombre d'occurrences du mot '{m}' dans 'LeRougeEtLeNoir.txt' :",
            nombre_occurrence(m, texte),
        )


#%% Exercice 2


#%% Exo 2 Q3


def calcul_decalage(motif):
    """Paramètre : motif une chaîne de caractères
    Précondition : motif non vide
    Valeur renvoyée : un dictionnaire avec clef de type str et valeur de type int
    Postcondition : associe à chaque caractère de motif (sauf au dernier) le décalage
    de sa dernière occurrence par rapport au dernier caractère du motif
    """
    assert len(motif) > 0
    p = len(motif)
    decalage = {}
    decalage[motif[-1]] = p
    for j in range(len(motif) - 1):
        "à compléter"
    return decalage


def test_calcul_decalage():
    """
    Tests unitaires pour calcul_decalage
    """
    assert calcul_decalage("nouille") == {
        "e": 7,
        "n": 6,
        "o": 5,
        "u": 4,
        "i": 3,
        "l": 1,
    }
    assert calcul_decalage("GATTACA") == {"A": 2, "G": 6, "T": 3, "C": 1}
    print("Tests réussis")


#%% Exo 2 Q4


def premiere_occurrence_bmh(motif, texte):
    """
    Recherche de motif dans texte avec l'algorithme de Boyer-Moore-Horspool
    (première version)
    Paramètre : motif et texte deux chaînes de caractères
    Précondition : 0 < len(motif) <= len(texte)
    Valeur renvoyée : tuple d'entiers
    Postcondition : renvoie (index première occurrence de motif dans texte, nombre de comparaisons)
    avec index = -1 si pas d'occurrence de motif dans texte
    """
    n = len(texte)
    p = len(motif)
    assert 0 < p <= n  # précondition
    # =============================================================================
    #     Précalcul du dictionnaire de décalages
    # =============================================================================
    decalage = calcul_decalage(motif)
    i = 0
    nb_comparaisons = 0  # Comparaisons de caractères
    # =============================================================================
    # Boucle de comparaison fenetre sur le texte et motif
    # =============================================================================
    while i <= n - p:
        j = p - 1
        nb_comparaisons += 1
        # =============================================================================
        #  A compléter boucle de comparaison  de la fenêtre et  du motif
        #  en comparant caractère par caractère de droite à gauche
        # =============================================================================
        # =============================================================================
        # CAS 1 : le motif est trouvé  avec la fenêtre en position i
        # =============================================================================
        if j < 0:
            "à compléter : cas où le motif a été trouvé"
            return (i, nb_comparaisons)
        # =============================================================================
        # CAS 2 :  le motif n'est pas trouvé  avec la fenêtre en position i
        # =============================================================================
        dernier_caractere = texte[i + p - 1]
        # =============================================================================
        # CAS 2.1 : le dernier caractère de la fenêtre courante
        # a une dernière occurrence à droite  dans le motif distincte de la dernière position
        # on peut décaler la fenêtre vers la droite
        # pour faire correspondre la dernière occurrence à droite du dernier caractère dans le motif
        # avec le dernier caractère de la fenêtre courante
        # =============================================================================
        if dernier_caractere in decalage:
            "à compléter"
        # =============================================================================
        #  CAS 2.2  le dernier caractère de la fenêtre courante
        #          n'a pas d'autre occurrence dans le motif
        #        on peut décaler la fenêtre vers la droite de la longueur p du motif
        # =============================================================================
        else:
            "à compléter"
    # =============================================================================
    # CAS 3 : le motif n'a été trouvé pour aucune position dans le texte
    # =============================================================================
    return (-1, nb_comparaisons)


def test_premiere_occurrence_bmh():
    assert premiere_occurrence_bmh("aabaac", "aabaabaac") == (3, 8)
    assert premiere_occurrence_bmh("babbb", "bbabbcabbabbabbb") == (11, 16)
    assert premiere_occurrence_bmh("babbb", "bbabbcabbabbabb") == (-1, 10)
    print("Tests réussis")



#%% Exo 2 Q5


def test_bmh_rouge_noir():
    """Comparaison en nombre de comparaisons
    des algorithmes de recherche naive et de boyer-moore-horspool
    sur le texte du roman 'Le Rouge et le Noir'"""
    f = open("LeRougeEtLeNoir.txt", "r", encoding="utf-8")
    texte = f.read()
    f.close()
    motif = "Julien tremblait"
    print(len(texte))
    print(
        f"Recherche de la première occcurrence de {motif} avec la méthode find"
    )
    print(texte.find(motif))
    print(
        f"Recherche de la première occcurrence de {motif} et du nombre de comparaisons avec l'algorithme naif"
    )
    print(premiere_occurrence_naif_trace(motif, texte))
    print(
        f"Recherche de la première occcurrence de {motif} et du nombre de comparaisons  avec l'algorithme de BoyerMoore-Horspool"
    )
    print(premiere_occurrence_bmh(motif, texte))


#%% Exo 2 Q6



#%% Exercice 3 : Boyer-Moore version complète


def construire_table(motif, alphabet):
    """
    Renvoie un tableau de dictionnaires tel que table[i][c]
    est le plus grand k tel que 0 <= k < j et motif[k] == c
    ou -1 si k n'existe pas

    Parameters
    ----------
    motif : chaine de caractères
    alphabet : chaine de caractères

    Returns
    -------
    table : tableau de dictionnaires

    """
    table = [{c: -1 for c in alphabet} for i in range(len(motif))]
    for i in range(len(motif)):
        "à compléter"
    return table


def test_construire_table():
    assert construire_table("abbbb", "ab") == [
        {"a": -1, "b": -1},
        {"a": 0, "b": -1},
        {"a": 0, "b": 1},
        {"a": 0, "b": 2},
        {"a": 0, "b": 3},
    ]
    assert construire_table("bonbon", "bon") == [
        {"b": -1, "o": -1, "n": -1},
        {"b": 0, "o": -1, "n": -1},
        {"b": 0, "o": 1, "n": -1},
        {"b": 0, "o": 1, "n": 2},
        {"b": 3, "o": 1, "n": 2},
        {"b": 3, "o": 4, "n": 2},
    ]
    print("tests réussis")


def premiere_occurrence_boyer_moore(motif, texte, alphabet):
    """
    Renvoie l'index de la première occurrence de motif dans texte et le nombre
    de comparaisons effectuées

    Parameters
    ----------
    motif : chaine de caractères de longueur p
    texte : chaine de caractères de longueur n
    alphabet : chaine de caractères

    Returns
    -------
    couple (position de la première occurrence de motif dans texte, nombre de comparaisons de caractères)
    renvoie (-1, nombre de comparaisons) si le motif ne se trouve pas dans texte
    """
    n = len(texte)
    p = len(motif)
    nb_comparaisons = 0
    table = construire_table(motif, alphabet)
    i = 0  # position dans le texte
    while i <= n - p:
        j = p - 1  # position dans le motif
        nb_comparaisons += 1
        # à compléter : boucle de droite à gauche dans la fenêtre glissant
        # on compare motif[j] avec  texte[i + j] en décrémentant j jusqu'à 0
        # à chaque itération on incrémente nb_comparaisons
        if j < 0:  # cas où on a trouvé le motif en position i
            return (i, nb_comparaisons)
        else:  # sinon on utilise table pour décaler i
            "à compléter"
    return (-1, nb_comparaisons)


def test_premiere_occurrence_boyer_moore():
    assert premiere_occurrence_boyer_moore_trace(
        "abbbb", "abaabbababaabbbb", "ab"
    ) == (11, 15)
    assert premiere_occurrence_boyer_moore_trace(
        "mille", "milliardemillesabord", "abdeillmors"
    ) == (9, 9)
    print("tests réussis")


