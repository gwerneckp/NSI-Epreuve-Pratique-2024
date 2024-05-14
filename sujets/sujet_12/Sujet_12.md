# Sujet 12

## Exercice 1

Écrire une fonction `tri_selection` qui prend en paramètre un tableau `tab` de nombres
entiers (type `list`) et qui le modifie afin qu'il soit trié par ordre croissant.

On utilisera l'algorithme suivant :

- on recherche le plus petit élément du tableau, en le parcourant du rang 0 au dernier rang, et on l'échange avec l'élément d'indice 0 ;
- on recherche ensuite le plus petit élément du tableau restreint du rang 1 au dernier rang, et on l'échange avec l'élément d'indice 1 ;
- on continue de cette façon jusqu'à ce que le tableau soit entièrement trié.

```python
def tri_selection(a):
    pass
```

Exemple :

```python
tab = [1, 52, 6, -9, 12]
assert tri_selection(tab) == [-9, 1, 6, 12, 52]
```

## Exercice 2

Le jeu du « plus ou moins » consiste à deviner un nombre entier choisi entre 1 et 99.

Une élève de NSI décide de le coder en langage Python de la manière suivante :

- le programme génère un nombre entier aléatoire compris entre 1 et 99 ;
- si la proposition de l'utilisatrice est plus petite que le nombre cherché, l'utilisatrice en est avertie. Elle peut alors en tester un autre ;
- si la proposition de l'utilisatrice est plus grande que le nombre cherché, l'utilisatrice en est avertie. Elle peut alors en tester un autre ;
- si l'utilisatrice trouve le bon nombre en 10 essais ou moins, elle gagne ;
- si l'utilisatrice a fait plus de 10 essais sans trouver le bon nombre, elle perd.

La fonction `randint` est utilisée.  
Si a et b sont des entiers tels que `a <= b`, `randint(a,b)` renvoie un
nombre entier compris entre `a` et `b`.

Compléter le code ci-dessous et le tester :

```python
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1,...)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = ...

    while nb_mystere != ... and compteur < ... :
        compteur = compteur + ...
        if nb_mystere ... nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ",...)
        print("Nombre d'essais: ",...)
    else:
        print ("Perdu ! Le nombre était ",...)
```
