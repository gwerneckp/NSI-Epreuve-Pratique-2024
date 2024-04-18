#!/bin/bash

# Nom du fichier Python à vérifier
python_file="hello.py"
python_name="hello"

# Vérifier si le fichier existe
if [ -f "$python_file" ]; then
    # Exécuter le fichier Python et stocker la sortie dans une variable
    output=$(python3 -c "import $python_name; print($python_name.hello_world())")
    
    # Vérifier si la sortie correspond à "Hello World!"
    if [ "$output" = "Hello World!" ]; then
        echo "Le fichier $python_file affiche correctement 'Hello World!'"
        exit 0  # Succès
    else
        echo "Le fichier $python_file ne produit pas la sortie attendue."
        echo "Sortie réelle : $output"
        exit 1  # Échec
    fi
else
    echo "Le fichier $python_file n'existe pas."
    exit 1  # Échec
fi
