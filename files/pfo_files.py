"""Module providing some functions to work with files"""

import os

# ! --------------------------------------------------------------------------------------
def list_files_in_directory(folder_path):
    """
    Lister le contenu d un répertoire

    Args:
        folder_path (chain): chemin vers le répertoire
        ex : folder_path = '/Users/pierre/Desktop/images'

    Returns:
        liste avec le contenu du répertoire

    Example:
        
    """

    fichiers = sorted([f for f in os.listdir(folder_path)
                    if os.path.isfile(os.path.join(folder_path, f))
                    and not f.startswith('.')])

    return fichiers

# ! --------------------------------------------------------------------------------------
def list_all_files(folder_path):
    """
    Lister le contenu d un répertoire y compris dans les sous-répertoires

    Args:
        folder_path (chain): chemin vers le répertoire
        ex : folder_path = '/Users/pierre/Desktop/images'

    Returns:
        liste avec le contenu du répertoire et des sous-répertoires

    Example:
        
    """
    # Initialiser la liste
    liste = []

    # initialiser le chemin
    rootdir = folder_path

    # Lister les sous-répertoires
    for subdir, _, files in os.walk(rootdir):
        # Lister les fichiers dans le répertoire
        for file in files:
            # Ajouter le chemin complet du fichier à la liste
            a = os.path.join(subdir, file)
            # Ajouter le chemin à la liste
            liste.append(a)
    
    liste = sorted(liste)

    return liste

# ! --------------------------------------------------------------------------------------
def get_directory_name(item):
    """
    Donner le nom du répertoire qui contient un fichier
    Dans ce code, la fonction get_directory_name utilise la fonction os.path.dirname
    pour obtenir le nom du répertoire qui contient le fichier. 
    Ensuite, elle utilise la méthode split pour séparer le nom du répertoire 
    de la chaîne de chemin d'accès, et elle retourne le dernier élément 
    de la liste, qui est le nom du répertoire.

    Args:
        file (chain): nom du fichier
        ex : ''

    Returns:
        (chain) nom du répertoire 

    Example:
        
    """

    # Obtenir le chemin complet du fichier
    a = os.path.dirname(item)
    
    # Split le chemin complet du fichier par '/'
    a = a.split('/')
    
    # Retourner le dernier élément de la liste, qui est le nom du répertoire
    a = a[-1]
    
    return a




