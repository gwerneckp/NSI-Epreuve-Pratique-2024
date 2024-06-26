# Sujet 37

## Exercice 1

Programmer la fonction `moyenne` prenant en paramètre un tableau d'entiers `tab` (de type `list`) qui renvoie la moyenne de ses éléments si le tableau est non vide. Proposer une
façon de traiter le cas où le tableau passé en paramètre est vide.

Dans cet exercice, on s'interdira d'utiliser la fonction Python `sum`.

Exemples :

```python
>>> moyenne([5,3,8])
5.333333333333333
>>> moyenne([1,2,3,4,5,6,7,8,9,10])
5.5
>>> moyenne([])
# Comportement différent suivant le traitement proposé.
```

## Exercice 2

On considère un tableau d'entiers `tab` (de type `list`) dont les éléments sont des `0` ou des `1`). On se propose de trier ce tableau selon l'algorithme suivant : à chaque étape du tri, le tableau est constitué de trois zones consécutives, la première ne contenant que des `0`,
la seconde n'étant pas triée et la dernière ne contenant que des `1`.
Au départ, les zones ne contenant que des `0` et des `1` sont vides.

<table>
<tr>
<td>Zone de 0</td><td>Zone non triée</td><td>Zone de 1</td>
</tr>
</table>

Tant que la zone non triée n'est pas réduite à un seul élément, on regarde son premier
élément :

- si cet élément vaut 0, on considère qu'il appartient désormais à la zone ne contenant
  que des 0 ;
- si cet élément vaut 1, il est échangé avec le dernier élément de la zone non triée et on
  considère alors qu'il appartient à la zone ne contenant que des 1.

Dans tous les cas, la longueur de la zone non triée diminue de 1.

Compléter la fonction `tri` suivante :

```python
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

```

Exemple :

```python
>>> tab = [0,1,0,1,0,1,0,1,0]
>>> tri(tab)
>>> tab
[0, 0, 0, 0, 0, 1, 1, 1, 1]
```
