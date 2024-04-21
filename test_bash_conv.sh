#!/bin/bash

# Chemin vers le répertoire contenant les fichiers notebook
repertoire_notebook="Notebook"

# Nom du fichier notebook à convertir en script Python
nom_fichier_notebook="essai_notebook.ipynb"

# Chemin vers le fichier notebook
chemin_notebook="${repertoire_notebook}/${nom_fichier_notebook}"

# Chemin vers le script Python généré
nom_script_python="essai_notebook.py"
chemin_script_python="${repertoire_notebook}/${nom_script_python}"

# Conversion du notebook en script Python
jupyter nbconvert --to script "${chemin_notebook}" --output "${chemin_script_python}"

# Exécution du test unitaire sur le script Python généré
pytest Notebook/essai_notebook_test.py