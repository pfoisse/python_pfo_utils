"""Module providing some functions to work with files"""

import os

# ! --------------------------------------------------------------------------------------
def list_all_files(folder_path):
    """
    Cette fonction liste les fichiers présents dans un répertoire spécifique 
    ainsi que dans tous les sous-répertoires. 
    Cette fonction ne liste pas les fichés cachés (ceux qui commencent par un point).

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
            if not file.startswith('.'):
                # Ajouter le chemin complet du fichier à la liste
                a = os.path.join(subdir, file)
                # Ajouter le chemin à la liste
                liste.append(a)
    
    liste = sorted(liste)

    return liste

# ! --------------------------------------------------------------------------------------
def list_all_directories(folder_path):
    """
    Cette fonction liste les répertoires présents dans un répertoire spécifique 
    ainsi que dans tous les sous-répertoires. 
    Cette fonction ne liste pas les répertoires cachés (ceux qui commencent par un point).

    Args:
        folder_path (chain): chemin vers le répertoire
        ex : folder_path = '/Users/pierre/Desktop/images'
        
    """
    # Initialiser la liste
    liste = []

    # initialiser le chemin
    rootdir = folder_path

    # Lister les sous-répertoires
    for subdir, _, _ in os.walk(rootdir):
        # Lister les fichiers dans le répertoire
        for file in _:
            if not file.startswith('.'):
                # Ajouter le chemin complet du fichier à la liste
                pass
        # Ajouter les noms des répertoires à la liste
        liste.append(subdir)

    # Remove the first element of the liste_repertoires list
    liste.pop(0)

    return liste


# ! --------------------------------------------------------------------------------------
def get_file_infos(folder_path):
    """
    La fonction get_file_infos prend en entrée un chemin d'accès à un fichier 
    et retourne un dictionnaire contenant les informations suivantes :
        chemin complet : le chemin complet du fichier
        nom du répertoire : le nom du répertoire où se trouve le fichier
        nom du fichier : le nom du fichier sans l'extension
        extension : l'extension du fichier (par exemple, "JPG" ou "PNG")

    La fonction utilise les fonctions os.path.basename() 
    et os.path.splitext() pour séparer le nom du fichier et l'extension. 
    Ensuite, elle utilise la méthode rstrip('/') pour enlever le dernier '/' 
    du chemin complet.

    La fonction retourne ensuite un dictionnaire contenant les informations 
    décrites ci-dessus.
    
    Args:
        folder_path (chain): chemin vers le nom du fichier
        ex : '/Users/pierre/Desktop/images/divers/2019-02-12/IMAG0041.JPG'

    Returns:
        This code will output:
            'chemin complet' :  /Users/pierre/Desktop/images/divers
            'nom du répertoire' :  divers
            'nom du fichier' :  IMAG0041.JPG
            'extension' :  JPG
        """
    
   # Utiliser os.path.basename() pour obtenir le nom du fichier sans le chemin
    nom_fichier_avec_extension = os.path.basename(folder_path)
    #print(f'Nom du fichier avec extension : {nom_fichier_avec_extension}')

    # Utiliser os.path.splitext() pour séparer le nom du fichier et l'extension
    nom_fichier, extension = os.path.splitext(nom_fichier_avec_extension)
    
    # Obtenir le nom du répertoire sans le dernier '/'
    chemin_complet = os.path.dirname(folder_path).rstrip('/')
    #print('chemin complet :', chemin_complet)

    chemin_decoupe = chemin_complet.split('/')
    #print('chemin découpe :', chemin_decoupe)

    # Utiliser os.path.basename() pour obtenir le nom du répertoire
    nom_repertoire = os.path.basename(chemin_complet)
    #print('Nom du répertoire :', nom_repertoire)

    # Enlever le dernier '.' de l'extension
    extension = extension.lstrip('.')
    #print('Extension :', extension)

    print()

    # Combine le nom du répertoire et le nom du fichier pour le nom du fichier
    nom_fichier = nom_fichier + '.' + extension

    # Retourner le dictionnaire contenant les informations décrites ci-dessus
    return {
        'chemin complet': chemin_complet,
        'nom du fichier': nom_fichier, 
        'nom du répertoire': nom_repertoire, 
        'extension': extension
    }




