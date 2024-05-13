# Sujet 04

## Exercice 1

Programmer la fonction `recherche`, prenant en paramètres un tableau non vide `tab` (type `list`) d'entiers et un entier `n`, et qui renvoie l'indice de la **dernière** occurrence de l'élément cherché. Si l'élément n'est pas présent, la fonction renvoie `None`.

```python
def recherche(a):
    pass
```

Exemples

```python
assert recherche([5, 3], 1) == None  # renvoie None
assert recherche([2, 4], 2) == 0
assert recherche([2, 3, 5, 2, 4], 2) == 3
```

## Exercice 2

On souhaite programmer une fonction donnant la distance la plus courte entre un point
de départ et une liste de points. Les points sont tous à coordonnées entières.
Les points sont donnés sous la forme d'un tuple de deux entiers.
La liste des points à traiter est donc un tableau de tuples.

On rappelle que la distance entre deux points du plan de coordonnées $(x;y)$ et $(x';y')$
vérifie la formule :

$$d^2=(x-x')^2+(y-y')^2$$

Compléter le code des fonctions `distance_carre` et `point_le_plus_proche` fournies ci-dessous pour qu'elles répondent à leurs spécifications.

```python
def distance_carre(point1, point2):
    """Calcule et renvoie la distance au carre entre
    deux points."""
    return (...) ** 2 + (...) ** 2


def point_le_plus_proche(depart, tab):
    """Renvoie les coordonnées du premier point du tableau tab se
    trouvant à la plus courte distance du point depart."""
    min_point = tab[0]
    min_dist = ...
    for i in range(1, len(tab)):
        if distance_carre(tab[i], depart) < ...:
            min_point = ...
            min_dist = ...
    return min_point
```

Exemples :

```python
assert distance_carre((1, 0), (5, 3)) == 25
assert distance_carre((1, 0), (0, 1)) == 2
assert point_le_plus_proche((0, 0), [(7, 9), (2, 5), (5, 2)]) == (2, 5)
assert point_le_plus_proche((5, 2), [(7, 9), (2, 5), (5, 2)]) == (5, 2)
```
