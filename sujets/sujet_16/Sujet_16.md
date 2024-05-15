# Sujet 16

## Exercice 1

Écrire une fonction `ecriture_binaire_entier_positif` qui prend en paramètre un
entier positif `n` et renvoie une une chaine de caractère correspondant à l'écriture binaire de `n`.

On rappelle que :

- l'écriture binaire de 25 est 11001 car $25 = 1 \times 2^4 + 1 \times 2^3 + 0 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$ ;
- `n % 2` vaut 0 ou 1 selon que `n` est pair ou impair ;
- `n // 2` donne le quotient de la division euclidienne de `n` par 2.

Il est interdit dans cet exercice d'utiliser la fonction `bin` de Python.

```python
def ecriture_binaire_entier_positif(a):
    pass
```

Exemples :

```python
assert 5 % 2 == 1
assert 5 // 2 == 2
assert ecriture_binaire_entier_positif(0) == "0"
assert ecriture_binaire_entier_positif(2) == "10"
assert ecriture_binaire_entier_positif(105) == "1101001"
```

## Exercice 2

La fonction `tri_bulles` prend en paramètre une liste `tab` d'entiers (type `list`) et le modifie pour le trier par ordre croissant.

Le tri à bulles est un tri en place qui commence par placer le plus grand élément en
dernière position en parcourant le tableau de gauche à droite et en échangeant au passage
les éléments voisins mal ordonnés (si la valeur de l'élément d'indice `i` a une valeur
strictement supérieure à celle de l'indice `i + 1`, ils sont échangés). Le tri place ensuite
en avant-dernière position le plus grand élément du tableau privé de son dernier élément
en procédant encore à des échanges d'éléments voisins. Ce principe est répété jusqu'à
placer le minimum en première position.

Exemple : pour trier le tableau `[7, 9, 4, 3]` :

- première étape : 7 et 9 ne sont pas échangés, puis 9 et 4 sont échangés, puis 9 et 3 sont échangés, le tableau est alors `[7, 4, 3, 9]`
- deuxième étape : 7 et 4 sont échangés, puis 7 et 3 sont échangés, le tableau est alors `[4, 3, 7, 9]`
- troisième étape : 4 et 3 sont échangés, le tableau est alors `[3, 4, 7, 9]`

Compléter le code Python ci-dessous qui implémente la fonction tri_bulles.

```python
def echange(tab, i, j):
    """Echange les éléments d'indice i et j dans le tableau tab."""
    temp = ...
    tab[i] = ...
    tab[j] = ...


def tri_bulles(tab):
    """Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles."""
    n = len(tab)
    for i in range(...):
        for j in range(...):
            if ... > ...:
                echange(tab, j, ...)
    return tab
```

Exemples :

```python
assert tri_bulles([]) == []
assert tri_bulles([9, 3, 7, 2, 3, 1, 6]) == [1, 2, 3, 3, 6, 7, 9]
assert tri_bulles([9, 7, 4, 3]) == [3, 4, 7, 9]
```
