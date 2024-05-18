# Sujet 42

## Exercice 1

Écrire une fonction `moyenne` qui prend en paramètre un tableau d'entiers non vide et qui
renvoie un nombre flottant donnant la moyenne de ces entiers.

**Attention** : il est interdit d'utiliser la fonction `sum` ou la fonction `mean` (module `statistics`) de Python.

Exemples :

```python
>>> moyenne([1])
1.0
>>> moyenne([1, 2, 3, 4, 5, 6, 7])
4.0
>>> moyenne([1, 2])
1.5
```

## Exercice 2

Le but de l'exercice est de compléter une fonction qui détermine si une valeur est présente
dans un tableau de valeurs triées dans l'ordre croissant.

Compléter l'algorithme de dichotomie donné ci-après.

```python 
def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""

    debut = 0
    fin = ... 
    while debut <= fin:
        m = ... 
        if x == tab[m]:
            return ... 
        if x > tab[m]:
            debut = ... 
        else:
            fin = ... 
    return False




```

Exemples :

```python
>>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28)
True
>>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27)
False
>>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1)
False
>>> dichotomie([], 28)
False
```