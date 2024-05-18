class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = ... 
    tab_ins[...] = ... 
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = ... 
    return tab_ins

