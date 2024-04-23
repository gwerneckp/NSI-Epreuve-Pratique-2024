#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

print("Enter the radius of the circle: ")


# Enter the radius of the circle: 
# 
# 
# # exercice entrainement
# 
# Finir cette fonction
# 
# ![Graphe](Pasted_image.png)

# In[ ]:


def fonctions(r):
    area = math.pi * r**2
    return area

r = 10
print(fonctions(r))


# ## Tri Fusion - Diviser pour régner
# 
# 1. **Introduction**
# 
# Le diviser pour régner est une méthode algorithmique basée sur le principe suivant :
# 
# On prend un problème (généralement complexe à résoudre), on divise ce problème en une multitude de petits problèmes, l'idée étant que les "petits problèmes" seront plus simples à résoudre que le problème original. Une fois les petits problèmes résolus, on recombine les "petits problèmes résolus" afin d'obtenir la solution du problème de départ.
# 
# Le paradigme "diviser pour régner" repose donc sur 3 étapes :
# 
# - **DIVISER :** le problème d'origine est divisé en un certain nombre de sous-problèmes
# - **RÉGNER :** on résout les sous-problèmes (les sous-problèmes sont plus faciles à résoudre que le problème d'origine)
# - **COMBINER :** les solutions des sous-problèmes sont combinées afin d'obtenir la solution du problème d'origine.
# 
# > [!Note] Titre. 
# > test
