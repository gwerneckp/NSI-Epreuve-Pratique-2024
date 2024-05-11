# Sujet_13
## S_13.1

Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre entier et `tab`
un tableau de nombres entiers (type `list`), et qui renvoie l'indice de la première occurrence de `elt` dans `tab` si `elt` est dans `tab` et `None` sinon.

L'objectif de cet exercice est de parcourir un tableau, il est interdit d'utiliser la méthode
`index` des listes Python.

```python
def recherche(elt, tab):
    pass
```


Exemples :
```python
assert recherche(1, [2, 3, 4]) == None  # renvoie None
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(50, [1, 50, 1]) == 1
assert recherche(15, [8, 9, 10, 15]) == 3
```


## S_13.2

On considère la fonction `insere` ci-dessous qui prend en argument un tableau `tab` d'en-
tiers triés par ordre croissant et un entier `a`. 

Cette fonction crée et renvoie un nouveau tableau à partir de celui fourni en paramètre en y
insérant la valeur `a` de sorte que le tableau renvoyé soit encore trié par ordre croissant. Les
tableaux seront représentés sous la forme de listes Python.

```python
def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [a] + tab  # nouveau tableau contenant a
    # suivi des éléments de tab
    i = 0
    while i < ... and a > ...:
        tab_a[i] = ...
        tab_a[i + 1] = a
        i = ...
    return tab_a
```

Compléter la fonction insere ci-dessus.

Exemples :

```python
assert insere([1, 2, 4, 5], 3) == [1, 2, 3, 4, 5]
assert insere([1, 2, 7, 12, 14, 25], 30) == [1, 2, 7, 12, 14, 25, 30]
assert insere([2, 3, 4], 1) == [1, 2, 3, 4]
assert insere([], 1) == [1]
```

