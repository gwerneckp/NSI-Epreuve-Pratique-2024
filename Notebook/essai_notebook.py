#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math

print("Enter the radius of the circle: ")


# # exercice entrainement
# 
# Finir cette fonction
# 
# ![Graphe](290g.png)
# 

# In[4]:


def fonctions(r):
    area = math.pi * r**2
    return area

r = 10
print(fonctions(r))

