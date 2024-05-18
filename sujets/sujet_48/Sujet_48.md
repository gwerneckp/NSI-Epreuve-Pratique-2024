# Sujet 48

## Exercice 1

On considère dans cet exercice un graphe orienté représenté sous forme de listes d'adjacence.

On suppose que les sommets sont numérotés de `0` à `n-1`.

Par exemple, le graphe suivant :

![image](data2024/graph2.png){: .center}

est représenté par la liste d'adjacence suivante :

```python
adj = [[1, 2], [2], [0], [0]]
```

Écrire une fonction `voisins_entrants(adj, x)` qui prend en paramètre le graphe
donné sous forme de liste d'adjacence et qui renvoie une liste contenant les voisins entrants
du sommet `x`, c'est-à-dire les sommets `y` tels qu'il existe une arête de `y` vers `x`.

Exemples :

```python
>>> voisins_entrants([[1, 2], [2], [0], [0]], 0)
[2, 3]
>>> voisins_entrants([[1, 2], [2], [0], [0]], 1)
[0]
```


## Exercice 2

On considère dans cet exercice la suite de nombre suivante : 1, 11, 21, 1211, 111221, ...

Cette suite est construite ainsi : pour passer d'une valeur à la suivante, on la lit et on l'écrit sous la forme d'un nombre. Ainsi, pour 1211 :

- on lit *un 1, un 2, deux 1* ;
- on écrit donc en nombre *1 1, 1 2, 2 1* ;
- puis on concatène *111221*.

Compléter la fonction `nombre_suivant` qui prend en entrée un nombre sous forme de
chaine de caractères et qui renvoie le nombre suivant par ce procédé, encore sous forme de
chaîne de caractères.

```python 
def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(...): 
        if s[i] == chiffre:
            compte = ... 
        else:
            resultat += ... + ... 
            chiffre = ... 
            ...
    lecture_... = ... + ... 
    resultat += lecture_chiffre
    return resultat

```

Exemples :

```python
>>> nombre_suivant('1211')
'111221'
>>> nombre_suivant('311')
'1321'
```