"""Module providing some functions to work with files"""

import os
import pandas as pd

# ! --------------------------------------------------------------------------------------
def list_files_in_directory(folder_path):
    """
    Lister le contenu d un répertoire
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
    Lister le contenu d un répertoire y compris dans les sous-répertoires
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

    liste = list_all_files(folder_path)

    # Créer une liste de dictionnaires pour stocker les données
    data_list = []

    for chemin in liste:
        directory_name = get_directory_name(chemin)
        file_name = get_file_name(chemin)
        data_dict = {
            'chemin': chemin,
            'nom du fichier': file_name,
            'nom du répertoire': directory_name
        }
        data_list.append(data_dict)

    # Convertir la liste de dictionnaires en un DataFrame pandas
    df = pd.DataFrame(data_list)

    return(df)
