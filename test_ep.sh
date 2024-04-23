#!/bin/bash

# Chemin vers le répertoire contenant les fichiers notebook
repertoire_notebook="Epreuve_Pratique"

# Nom du fichier notebook à convertir en script Python
nom_fichier_notebook="sujet_06.ipynb"

# Chemin vers le répertoire de destination pour le fichier Python généré
repertoire_destination="."

# Chemin vers le fichier notebook
chemin_notebook="${repertoire_destination}/${repertoire_notebook}/${nom_fichier_notebook}"

# Chemin vers le fichier Python généré
chemin_python="${repertoire_destination}/${repertoire_notebook}/${nom_fichier_notebook%.*}.py"


# Conversion du notebook en script Python
jupyter nbconvert --to script "${chemin_notebook}"

# Exécution du test unitaire sur le script Python généré
pytest "${repertoire_destination}/${repertoire_notebook}/sujet_06_test.py"