#!/bin/bash
repertoire_notebook="Epreuve_Pratique"
nom_fichier_notebook="sujet_06.ipynb"
repertoire_destination="."
chemin_notebook="${repertoire_destination}/${repertoire_notebook}/${nom_fichier_notebook}"
chemin_python="${repertoire_destination}/${repertoire_notebook}/${nom_fichier_notebook%.*}.py"

# Installation de pytest et autre
pip install --upgrade pip
pip install pytest
pip install notebook nbconvert

jupyter nbconvert --to python "${chemin_notebook}"
pytest "${repertoire_destination}/tests/sujet_06_test.py"