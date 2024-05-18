def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage en haut
        colore_comp1(M, i-1, j, val)
    if ... < len(M): # propage en bas
        colore_comp1(M, ..., j, val) 
    if ...: # propage à gauche 
        colore_comp1(M, ..., ..., val) 
    if ...: # propage à droite 
        ...

>>> M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
>>> colore_comp1(M, 2, 1, 3)
>>> M
[[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]

