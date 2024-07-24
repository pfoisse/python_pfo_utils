"""Module providing some functions to work with files"""

import os
import pandas as pd
from photos.pfo_photos import get_date

# ! --------------------------------------------------------------------------------------
def list_files_in_directory(folder_path):
    """
    Cette fonction liste les fichiers présents dans un répertoire spécifique. 
    Elle ne liste pas les fichiers cachés (ceux qui commencent par un point).

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
def get_directory_name(folder_path):
    """
    Cette fonction donne le nom du répertoire qui contient un fichier spécifique.
    Dans ce code, la fonction get_directory_name utilise la fonction os.path.dirname
    pour obtenir le nom du répertoire qui contient le fichier. 
    Ensuite, elle utilise la méthode split pour séparer le nom du répertoire 
    de la chaîne de chemin d'accès, et elle retourne le dernier élément 
    de la liste, qui est le nom du répertoire.

    Args:
        folder_path (chain): chemin vers le nom du fichier
        ex : '/Users/pierre/Desktop/images/divers/2019-02-12/IMAG0045.JPG'

    Returns:
        (chain) : le nom du répertoire qui contient le fichier
        ex : 2019-02-12

    Example:
        
    """

    # Obtenir le chemin complet du fichier
    a = os.path.dirname(folder_path)
    
    # Split le chemin complet du fichier par '/'
    a = a.split('/')
    
    # Retourner le dernier élément de la liste, qui est le nom du répertoire
    a = a[-1]
    
    return a


# ! --------------------------------------------------------------------------------------
def get_file_name(folder_path):
    """
    La fonction get_file_name prend en paramètre un chemin complet vers un fichier 
    spécifique. Elle utilise la méthode split pour séparer le chemin complet 
    du fichier par '/' et retourne le dernier élément de la liste, 
    qui est le nom du fichier. 
    Cette fonction est utile pour extraire le nom du fichier 
    à partir de son chemin complet.

    Args:
        folder_path (chain): chemin vers le nom du fichier
        ex : '/Users/pierre/Desktop/images/divers/2019-02-12/IMAG0045.JPG'

    Returns:
        (chain) : le nom du fichier
        ex : IMAG0045.JPG

    Example:
        
    """
    
    # Split le chemin complet du fichier par '/'
    a = folder_path.split('/')
    
    # Retourner le dernier élément de la liste, qui est le nom du fichier
    a = a[-1]
    
    return a


# ! --------------------------------------------------------------------------------------
def get_all_files_content_in_a_dataframe(folder_path):
    """
    La fonction get_all_files_content_in_a_dataframe prend en entrée un chemin d'accès 
    à un dossier et renvoie un DataFrame contenant le contenu du dossier. 
    Elle liste d'abord tous les fichiers dans le dossier 
    et dans tous les sous-dossiers en utilisant la fonction list_all_files. 
    Ensuite, elle crée une liste de dictionnaires pour stocker les informations 
    des fichiers, y compris le chemin du fichier, le nom du fichier et le nom du dossier. 
    Enfin, elle convertit la liste de dictionnaires en un DataFrame pandas.

    Args:
        folder_path (chain): chemin vers le nom du fichier
        ex : '/Users/pierre/Desktop/images/divers/2019-02-12/IMAG0045.JPG'

    Returns:
        (chain) : le nom du fichier
        ex : IMAG0045.JPG

    Example:
        
    """
    # Lister les fichiers présents dans le dossier et dans tous les sous-dossiers
    liste = list_all_files(folder_path)

    # Créer une liste de dictionnaires pour stocker les données
    data_list = []

    # Parcourir les chemins de fichiers
    for chemin in liste:

        directory_name = get_directory_name(chemin)
        file_name = get_file_name(chemin)
        date = get_date(folder_path, file_name)
        data_dict = {
            'chemin': chemin,
            'nom du fichier': file_name,
            'nom du répertoire': directory_name,
            'date': date
        }
        data_list.append(data_dict)

    # Convertir la liste de dictionnaires en un DataFrame pandas
    df = pd.DataFrame(data_list)

    return(df)

# ! --------------------------------------------------------------------------------------
def decoupe_chemin(folder_path):
    """
    La fonction decoupe_chemin prend en entrée un chemin d'accès à un fichier 
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

    # Utiliser os.path.splitext() pour séparer le nom du fichier et l'extension
    nom_fichier, extension = os.path.splitext(nom_fichier_avec_extension)

    # Obtenir le nom du répertoire sans le dernier '/'
    chemin_complet = os.path.dirname(folder_path).rstrip('/')

    # Utiliser os.path.basename() pour obtenir le nom du répertoire
    nom_repertoire = os.path.basename(chemin_complet)

    # Enlever le dernier '.' de l'extension
    extension = extension.lstrip('.')

    # Combine le nom du répertoire et le nom du fichier pour le nom du fichier
    nom_fichier = nom_fichier + '.' + extension

    # Retourner le dictionnaire contenant les informations décrites ci-dessus
    return {
        'chemin complet': chemin_complet,
        'nom du fichier': nom_fichier, 
        'nom du répertoire': nom_repertoire, 
        'extension': extension
    }


