def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = ... # premier indice de la zone non triée 
    j = ... # dernier indice de la zone non triée 
    while i < j:
        if tab[i] == 0:
            i = ... 
        else:
            valeur = ... 
            tab[j] = ... 
            ...
            j = ...

>>> tab = [0,1,0,1,0,1,0,1,0]
>>> tri(tab)
>>> tab
[0, 0, 0, 0, 0, 1, 1, 1, 1]
