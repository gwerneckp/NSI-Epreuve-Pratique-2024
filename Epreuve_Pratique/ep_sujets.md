# Sujet_1

## s_1.1

Dans cet exercice, un arbre binaire de caractères est stocké sous la forme d’un
dictionnaire où les clefs sont les caractères des nœuds de l’arbre et les valeurs, pour
chaque clef, la liste des caractères des fils gauche et droit du nœud.

On utilise la valeur `''` pour représenter un fils vide.

Par exemple, l’arbre

![alt text](image.png)


est stocké dans

```python
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}

# Votre code
def taille(dictionnaire):
    pass
```

Écrire une fonction récursive `taille` prenant en paramètres un arbre binaire `arbre` non vide
sous la forme d’un dictionnaire et un caractère `lettre` qui est la valeur du sommet de
l’arbre, et qui renvoie la taille de l’arbre à savoir le nombre total de nœuds.

On observe que, par exemple, `arbre[lettre][0]`, respectivement
`arbre[lettre][1]`, permet d’atteindre la clé du sous-arbre gauche, respectivement
droit, de l’arbre `arbre` de sommet `lettre`.

Exemple :
```python
assert taille(a, 'F')==9
assert taille(a, 'B')==5
assert taille(a, 'I')==2
```

## s_1.2

On considère l'algorithme de tri de tableau suivant : à chaque étape, on parcourt le sous-
tableau des éléments non rangés et on place le plus petit élément en première position de
ce sous-tableau.

Exemple avec le tableau : ```t = [41, 55, 21, 18, 12, 6, 25]``` 

- Étape 1 : on parcourt tous les éléments du tableau, on permute le plus petit élément avec
le premier. Le tableau devient `t = [6, 55, 21, 18, 12, 41, 25]`

- Étape 2 : on parcourt tous les éléments **sauf le premier**, on permute le plus petit élément
trouvé avec le second.  
Le tableau devient : ```t = [6, 12, 21, 18, 55, 41, 25]``` 

Et ainsi de suite. 

Le programme ci-dessous implémente cet algorithme.


```python
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = ... 
    tab[i] = ... 
    tab[j] = ... 

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(...): 
        imin = ... 
        for i in range(..., N): 
            if tab[i] < ...: 
                imin = i
        echange(tab, ..., ...)
    return tab
```

Compléter le code de cette fonction de façon à obtenir :

```python
assert tri_selection([41, 55, 21, 18, 12, 6, 25])==[6, 12, 18, 21, 25, 41, 55]
```

## s_2.2

On considère des chaînes de caractères contenant uniquement des majuscules et des carac-
tères `*` appelées *mots à trous*.

Par exemple `INFO*MA*IQUE`, `***I***E**` et
`*S*` sont des mots à trous.

Programmer une fonction `correspond` qui :

- prend en paramètres deux chaînes de caractères `mot` et `mot_a_trous` où
`mot_a_trous` est un mot à trous comme indiqué ci-dessus, 
- renvoie :
    - `True` si on peut obtenir `mot` en remplaçant convenablement les caractères
`'*'` de `mot_a_trous`.
    - `False` sinon.

```python
def correspond(a,b):
    pass
````


Exemple :

```python
assert correspond('INFORMATIQUE', 'INFO*MA*IQUE')==True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE')==False
assert correspond('STOP', 'S*')==False
assert correspond('AUTO', '*UT*')==True
```

## s_2.2

On considère au plus 26 personnes A, B, C, D, E, F ... qui peuvent s'envoyer des messages
avec deux règles à respecter :

- chaque personne ne peut envoyer des messages qu'à une seule personne
(éventuellement elle-même),
- chaque personne ne peut recevoir des messages qu'en provenance d'une seule
personne (éventuellement elle-même).


Voici un exemple - avec 6 personnes - de « plan d'envoi des messages » qui respecte les
règles ci-dessus, puisque chaque personne est présente une seule fois dans chaque
colonne :

- A envoie ses messages à E
- E envoie ses messages à B
- B envoie ses messages à F
- F envoie ses messages à A
- C envoie ses messages à D
- D envoie ses messages à C

Et le dictionnaire correspondant à ce plan d'envoi est le suivant :

`plan_a = {'A':'E', 'B':'F', 'C':'D', 'D':'C', 'E':'B', 'F':'A'}`

Un cycle est une suite de personnes dans laquelle la dernière est la même que la
première.

Sur le plan d'envoi `plan_a` des messages ci-dessus, il y a deux cycles distincts : un premier
cycle avec A, E, B, F et un second cycle avec C et D.

En revanche, le plan d’envoi `plan_b` ci-dessous :

`plan_b = {'A':'C', 'B':'F', 'C':'E', 'D':'A', 'E':'B', 'F':'D'}`

comporte un unique cycle : A, C, E, B, F, D. Dans ce cas, lorsqu’un plan d’envoi comporte un
*unique cycle*, on dit que le plan d’envoi est *cyclique*.

Pour savoir si un plan d'envoi de messages comportant N personnes est cyclique, on peut
utiliser l'algorithme ci-dessous :


- on part d’un expéditeur (ici A) et on inspecte son destinataire dans le plan d'envoi,
- chaque destinataire devient à son tour expéditeur, selon le plan d’envoi, tant
qu’on ne « retombe » pas sur l’expéditeur initial,
- le plan d’envoi est cyclique si on l’a parcouru en entier.


Compléter la fonction `est_cyclique` en respectant la spécification.

On rappelle que la fonction Python `len` permet d'obtenir la longueur d'un dictionnaire.


```python
def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[...] 
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = ... 
        nb_destinataires = ... 

    return nb_destinataires == ...
```

Exemples :

```python
assert est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'})==False
assert est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'})==True
assert est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'})==True
assert est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'})==False
```

## S_3.1

Écrire la fonction `maximum_tableau`, prenant en paramètre un tableau non vide de nombres `tab` (de type
`list`) et renvoyant le plus grand élément de ce tableau.

```python
def maximum_tableau(a):
    pass
````


Exemples :

```python
assert maximum_tableau([98, 12, 104, 23, 131, 9])==131
assert maximum_tableau([-27, 24, -3, 15])==24
```

## S_3.2

On dispose de chaînes de caractères contenant uniquement des parenthèses ouvrantes et
fermantes. 

Un parenthésage est correct si :

- le nombre de parenthèses ouvrantes de la chaîne est égal au nombre de parenthèses
fermantes.
- en parcourant la chaîne de gauche à droite, le nombre de parenthèses déjà ouvertes doit
être, à tout moment, supérieur ou égal au nombre de parenthèses déjà fermées.


Ainsi, `((()())(()))` est un parenthésage correct. 

Les parenthésages `())(()` et `(())(()` sont, eux, incorrects.


On dispose du code de la classe `Pile` suivant :

```python
class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()
```

On souhaite programmer une fonction bon_parenthesage qui prend en paramètre une chaîne de caractères ch formée de parenthèses et renvoie True si la chaîne est bien parenthésée et False sinon.

Cette fonction utilise une pile et suit le principe suivant : en parcourant la chaîne de gauche à droite, si on trouve une parenthèse ouvrante, on l’empile au sommet de la pile et si on trouve une parenthèse fermante, on dépile (si possible) la parenthèse ouvrante stockée au sommet de la pile.

La chaîne est alors bien parenthésée si, à la fin du parcours, la pile est vide.

Elle est, par contre, mal parenthésée :

si dans le parcours, on trouve une parenthèse fermante, alors que la pile est vide ;
ou si, à la fin du parcours, la pile n’est pas vide.
Compléter le code de la fonction bon_parenthesage ci-dessous:

```python
def bon_parenthesage(ch):
    """Renvoie un booléen indiquant si la chaîne ch 
    est bien parenthésée"""
    p = Pile()
    for c in ch:
        if c == ...: 
            p.empiler(c)
        elif c == ...: 
            if p.est_vide():
                ...
            else:
                ...
    return ...
```

Exemples :

```python
assert bon_parenthesage("((()())(()))")==True
assert bon_parenthesage("())(()")==False
assert bon_parenthesage("(())(()")==False
```

## S_4.1

Programmer la fonction `recherche`, prenant en paramètres un tableau non vide `tab` (type `list`) d'entiers et un entier `n`, et qui renvoie l'indice de la **dernière** occurrence de l'élément cherché. Si l'élément n'est pas présent, la fonction renvoie `None`.

```python
def recherche(a):
    pass
````


Exemples
```python
assert recherche([5, 3], 1)==None # renvoie None
assert recherche([2, 4], 2)==0
assert recherche([2, 3, 5, 2, 4], 2)==3
```

## S_4.2

On souhaite programmer une fonction donnant la distance la plus courte entre un point
de départ et une liste de points. Les points sont tous à coordonnées entières.
Les points sont donnés sous la forme d'un tuple de deux entiers.
La liste des points à traiter est donc un tableau de tuples.

On rappelle que la distance entre deux points du plan de coordonnées $(x;y)$ et $(x';y')$
vérifie la formule :

$$d^2=(x-x')^2+(y-y')^2$$



Compléter le code des fonctions `distance_carre` et `point_le_plus_proche` fournies ci-dessous pour qu’elles répondent à leurs spécifications.

```python
def distance_carre(point1, point2):
    """ Calcule et renvoie la distance au carre entre 
    deux points."""
    return (...)**2 + (...)**2 

def point_le_plus_proche(depart, tab):
    """ Renvoie les coordonnées du premier point du tableau tab se 
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
assert distance_carre((1, 0), (5, 3))==25
assert distance_carre((1, 0), (0, 1))==2
assert point_le_plus_proche((0, 0), [(7, 9), (2, 5), (5, 2)])==(2, 5)
assert point_le_plus_proche((5, 2), [(7, 9), (2, 5), (5, 2)])==(5, 2)
```

## S_5.1

Écrire une fonction `max_et_indice` qui prend en paramètre un tableau non vide `tab` de
nombres entiers et qui renvoie la valeur du plus grand élément de ce tableau ainsi que
l’indice de sa première apparition dans ce tableau.

L’utilisation de la fonction native `max` n’est pas autorisée.

```python
def max_et_indice(a):
    pass
```

Exemples :

```python
assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])==(9, 3)
assert max_et_indice([-2])==(-2, 0)
assert max_et_indice([-1, -1, 3, 3, 3])==(3, 2)
assert max_et_indice([1, 1, 1, 1])==(1, 0)
```

## S_5.2

L’ordre des gènes sur un chromosome est représenté par un tableau `ordre` de `n` cases
d’entiers distincts deux à deux et compris entre 1 et `n`.

Par exemple, `ordre = [5, 4, 3, 6, 7, 2, 1, 8, 9]` dans le cas `n = 9`.

On dit qu’il y a un point de rupture dans `ordre` dans chacune des situations suivantes :

- la première valeur de `ordre` n’est pas 1 ;
- l’écart entre deux gènes consécutifs n’est pas égal à 1 ;
- la dernière valeur de `ordre` n’est pas n.

Par exemple, si `ordre = [5, 4, 3, 6, 7, 2, 1, 8, 9]` avec `n = 9`, on a

- un point de rupture au début car 5 est différent de 1
- un point de rupture entre 3 et 6 (l’écart est de 3)
- un point de rupture entre 7 et 2 (l’écart est de 5)
- un point de rupture entre 1 et 8 (l’écart est de 7)

Il y a donc 4 points de rupture.

Compléter les fonctions Python `est_un_ordre` et `nombre_points_rupture`
proposées à la page suivante pour que :


- la fonction `est_un_ordre` renvoie `True` si le tableau passé en paramètre
représente bien un ordre de gènes de chromosome et `False` sinon ;

- la fonction `nombre_points_rupture` renvoie le nombre de points de rupture
d’un tableau passé en paramètre représentant l’ordre de gènes d’un
chromosome.

```python
def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = ... 

    for x in tab:
        if x < ... or x >... or ...: 
            return False
        ... .append(...) 
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente 
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert ... 
    n = len(ordre)
    nb = 0
    if ordre[...] != 1: # le premier n'est pas 1 
        nb = nb + 1
    i = 0
    while i < ...: 
        if ... not in [-1, 1]: # l'écart n'est pas 1 
            nb = nb + 1
        i = i + 1
    if ordre[i] != ...: # le dernier n'est pas n 
        nb = nb + 1
    return nb
```

Exemples :

```python
assert est_un_ordre([1, 6, 2, 8, 3, 7])==False
assert est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9])==True
assert nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9])==4
assert nombre_points_rupture([1, 2, 3, 4, 5])==0
assert nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5])==7
assert nombre_points_rupture([2, 1, 3, 4])==2
```


## S_6.1

Écrire une fonction `verifie` qui prend en paramètre un tableau de valeurs numériques et qui renvoie `True` si ce tableau est trié dans l’ordre croissant, `False` sinon.

Un tableau vide est considéré comme trié.

```python
def verifie(a):
    pass
```


Exemples :

```python
Exemples :
assert verifie([0, 5, 8, 8, 9])==True
assert verifie([8, 12, 4])==False
assert verifie([-1, 4])==True
assert verifie([])==True
assert verifie([5])==True
```

## S_6.2

On considère dans cet exercice l’élection d’un vainqueur à l’issue d’un vote. Les résultats
du vote sont stockés dans un tableau : chaque vote exprimé est le nom d’un ou d’une
candidate.  
Par exemple, les résultats pourraient correspondre au tableau :

```python
urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
```

indiquant que 3 candidats ont obtenu au moins un vote chacun : A, B et C.

On cherche à déterminer le ou les candidats ayant obtenu le plus de suffrages. Pour cela, on propose d’écrire deux fonctions :

- La fonction depouille doit permettre de compter le nombre de votes exprimés pour chaque artiste. Elle prend en paramètre un tableau et renvoie le résultat dans un dictionnaire dont les clés sont les noms des issues et les valeurs le nombre de votes en leur faveur.
- La fonction vainqueurs doit désigner le nom du ou des gagnants. Elle prend en paramètre un dictionnaire non vide dont la structure est celle du dictionnaire renvoyé par la fonction depouille et renvoie un tableau. Ce tableau peut donc contenir plusieurs éléments s’il y a des artistes ex- aequo. Compléter les fonctions depouille et vainqueurs ci-après pour qu’elles renvoient les résultats attendus.

```python
def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = ... 
    for bulletin in urne:
        if ...: 
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            ...
    return resultat

def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if ... > ... : 
            nmax = ... 
    liste_finale = [ nom for nom in election if ... ] 
    return ...
```

Exemples d’utilisation :

```python
assert depouille([ 'A', 'B', 'A' ])=={'A': 2, 'B': 1}
assert depouille([])=={}
assert depouille(['A', 'A', 'A', 'B', 'C','B', 'C', 'B', 'C', 'B'])=={'A': 3, 'B': 4, 'C': 3}
assert vainqueurs({'A': 3, 'B': 4, 'C': 3})==['B']
assert vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1})==['A', 'B']
```

## S_7.1

On considère dans cet exercice une représentation binaire d’un entier non signé en tant que
tableau de booléens.
Si

```python
tab = [True, False, True, False, False, True, True]
```

est un tel tableau, alors l’entier qu’il représente est $2^6 +2^4 + 2^1 + 2^0 = 83$. Cette représentation consistant à placer en premier le booléen indiquant la puissance la plus élevée de 2
est dite *big-endian* ou grand-boutiste.

Écrire une fonction `gb_vers_entier` qui prend en paramètre un tel tableau et renvoie
l’entier qu’il représente.

```python
def gb_vers_entier(a):
    pass
````


Exemple :

```python
assert gb_vers_entier([])==0
assert gb_vers_entier([True])==1
assert gb_vers_entier([True, False, True, False, False, True, True])==83
assert gb_vers_entier([True, False, False, False, False, False, True, False])==130
```

## S_7.2

La fonction `tri_insertion` suivante prend en argument un tableau `tab` et trie ce tableau en
utilisant la méthode du tri par insertion. Compléter cette fonction pour qu'elle réponde à la
spécification demandée.

On rappelle le principe du tri par insertion : on considère les éléments à trier un par un,
le premier élément constituant, à lui tout seul, un tableau trié de longueur 1. On range
ensuite le second élément pour constituer un tableau trié de longueur 2, puis on range le
troisième élément pour avoir un tableau trié de longueur 3 et ainsi de suite...

A chaque étape, le premier élément du sous-tableau non trié est placé dans le sous-tableau
des éléments déjà triés de sorte que ce sous-tableau demeure trié.

Le principe du tri par insertion est donc d'insérer à la n-ième itération, le n-ième élément
à la bonne place.


```python
def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = ... 
        # la variable j sert à déterminer 
        # où placer la valeur à ranger
        j = ... 
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        while j > ... and valeur_insertion < tab[...]: 
            tab[j] = tab[j-1]
            j = ... 
        tab[j] = ...
    return tab
```

Exemples :

```python
assert tri_insertion([98, 12, 104, 23, 131, 9])==[9, 12, 23, 98, 104, 131]
```

