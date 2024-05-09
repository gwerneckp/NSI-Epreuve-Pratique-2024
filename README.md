# Bac_entrainement

# Premiere_entrainement

Espace d'entrainement  
NSI Premiere

# Réaliser les exercices dans le fichier Notebook
A vous de jouer

Faire les exercices demandés
Tester avec les cellules d'Assert
Puis charger votre travail sur le github remote

# Environnement virtuel
Travailler dans un environnement virtuel permet de garder en memoire toutes les dependances que vous installez
- python3 -m venv myenv
- source myenv/bin/activate

Pour desactiver

- source deactivate

# Soumettre son travail : Add - Commit - push
- git add .
- commit -m "Mon commentaire - exercices fait"
- git push

# Convertion d'un fichier Markdown en Notebook
- pip install --upgrade pip
- pip install notedown
- cd Epreuve_Pratique
- notedown nom_input.md > nom_output.ipynb

# Conversion d'un fichier Notebook en Script Python

## nbconvert
- pip install nbconvert
- cd Epreuve_Pratique
- jupyter nbconvert --to python nom_input.ipynb

## jupytext
- pip install jupytext
- cd Epreuve_Pratique
- jupytext --to py ./Epreuve_Pratique/sujet_06.ipynb --output ./Epreuve_Pratique/sujet_06.py

# Conflit update upstream
- git fetch upstream
- git rebase upstream/main
    - Accepter les modifications souhaitees une par une
    - git add .
    - git rebase --continue
- Une fois qu'on retrouve la branche `main`
- git push

# Retard de la branche locale sur le Remote
- git pull ou (git pull origin main)
    - Si cela ne fonctionne pas on fait :
	- `git config pull.rebase false`
- git pull
- git push (si necessaire)



