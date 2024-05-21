# Sujet 28

## Exercice 1

On s'intéresse à la suite d'entiers définie par :

- les deux premières valeurs sont égales à 1 ;
- ensuite, chaque valeur est obtenue en faisant la somme des deux valeurs qui la précè-
  dent.

La troisième valeur est donc $1+1 = 2$, la quatrième est $1+2 = 3$, la cinquième est $2+3 = 5$,
la sixième est $3 + 5 = 8$, et ainsi de suite.

Cette suite d'entiers est connue sous le nom de suite de Fibonacci.

Écrire en Python une fonction `fibonacci` qui prend en paramètre un entier `n` supposé
strictement positif et qui renvoie le terme d'indice `n` de cette suite.

Exemples :

```python
>>> fibonacci(1)
1
>>> fibonacci(2)
1
>>> fibonacci(25)
75025
```

## Exercice 2

On considère la fonction `eleves_du_mois` prenant en paramètres `eleves` et `notes` deux
tableaux de même longueur, le premier contenant le nom des élèves et le second, des
entiers positifs désignant leur note à un contrôle de sorte que `eleves[i]` a obtenu la
note `notes[i]`.

Cette fonction renvoie le couple constitué de la note maximale attribuée et des noms
des élèves ayant obtenu cette note regroupés dans un tableau.

Ainsi, l'instruction `eleves_du_mois(['a', 'b', 'c', 'd'], [15, 18, 12, 18])` renvoie
le couple `(18, ['b', 'd'])`.

```python
def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves =  ...

    for i in range(...) :
        if notes[i] == ... :
            meilleurs_eleves.append(...)
        elif notes[i] > note_maxi:
            note_maxi = ...
            meilleurs_eleves = [...]

    return (note_maxi,meilleurs_eleves)
```

Compléter ce code.

Exemples :

```python
>>> eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
>>> notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
>>> eleves_du_mois(eleves_nsi, notes_nsi)
(80, ['c', 'f', 'h'])
>>> eleves_du_mois([],[])
(0, [])
```
