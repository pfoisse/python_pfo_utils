import os

def list_files_in_repertoire(folder_path):
    """
    Lister le contenu d un répertoire

    Args:
        folder_path (chain): chemin vers le répertoire
        ex : folder_path = '/Users/pierre/Desktop/images'

    Returns:
        liste avec le contenu du répertoire

    Example:
        
    """

    fichiers = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith('.')])
    
    return fichiers
