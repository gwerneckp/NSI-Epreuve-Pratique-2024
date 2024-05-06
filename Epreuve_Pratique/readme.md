# Consignes pour faire les exercices de l'epreuve pratique

## Réaliser les exercices dans le fichier Notebook

A vous de jouer

- Faire les exercices demandés
- Tester avec les cellules d' Assert

Puis charger votre travail sur le github `remote`

- git add .
- commit -m "exercices fait"
- git push


## Convertion d'un fichier Markdown en Notebook
- pip install --upgrade pip
- pip install notedown
- cd Epreuve_Pratique
- notedown ep_sujets.md > ep_sujets.ipynb

## Conversion d'un fichier Notebook en Script Python
- pip install nbconvert
- cd Epreuve_Pratique
- jupyter nbconvert --to python ep_sujets.ipynb