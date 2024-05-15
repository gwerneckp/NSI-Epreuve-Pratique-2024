def recherche_indices_classement(a, b):
    pass

def moyenne(nom, resultats):
    '''Renvoie la moyenne de l'élève nom, selon le dictionnaire
    resultats. Si nom n'est pas dans le dictionnaire,
    la fonction renvoie None.'''
    if nom in ...:
        notes = resultats[nom]
        if ...: # pas de notes
            return 0
        total_points = ...
        total_coefficients = ...
        for ...  in notes.values():
            note, coefficient = valeurs
            total_points = total_points + ... * coefficient
            ... = ... + coefficient
        return round( ... / total_coefficients, 1 )
    else:
        return None