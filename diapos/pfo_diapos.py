"""Module providing some functions to work with diapos
"""



#! --------------------------------------------------------------------------------------
def OLD_rename_all_diapos_in_reverse_order(folder_path):
    """
    
    """

    from files.pfo_files import get_file_infos, list_all_files

    # Lister les fichiers présents dans le dossier et dans tous les sous-dossiers
    liste = list_all_files(folder_path)

    i = 1
    previous_repertoire_name = ''

    # Parcourir tous les chemins de fichiers
    for chemin in liste:

        # Obtenir les informations sur le fichier
        data = get_file_infos(chemin)

        # Obtenir les noms de chemins et de répertoire 
        folder_path = data['chemin complet']
        print('folder_path = ', folder_path)

        img_filename = data['nom du fichier']
        print('img_filename = ', img_filename)
        
        nom_repertoire = data['nom du répertoire']
        print('nom_repertoire = ', nom_repertoire)

        print('previous_repertoire_name = ', previous_repertoire_name)

        # si le fichier est encore dans le meme repertoire
        # alors ajouter 1 seconde a la date du fichier
        # sinon reinitialiser le compteur
        if nom_repertoire == previous_repertoire_name:
            i = i + 1
        else:
            i = 1

        # On fait un TRY pour gérer les erreurs au cas où le nom du répertoire n'est pas dans le format YYYY-MM-DD
        try:
            print('i = ', i)

        except:
            print('erreur')
            continue

        previous_repertoire_name = nom_repertoire

#! --------------------------------------------------------------------------------------
def rename_all_diapos_in_reverse_order(folder_path):
    """
    
    """

    from files.pfo_files import get_file_infos, list_all_files

    # Lister les fichiers présents dans le dossier et dans tous les sous-dossiers
    liste = list_all_files(folder_path)

    print('liste des chemins = ', liste)

    # Parcourir tous les chemins de fichiers
    for chemin in liste:

        fichiers_contenus_dans_repertoire = list_all_files(chemin)
        print('contenu_du_repertoire = ', fichiers_contenus_dans_repertoire)



#! --------------------------------------------------------------------------------------
def rename_a_diapo(folder_path, intial_reference_tag ='DIAPO-', directory_reference_number='000', file_number=1):
    """
    This function renames a given diapo file by creating a new name based on 
    the provided initial reference tag,
    directory reference number, 
    and file number. 
    
    The new name includes 
    the initial reference tag,
    directory reference number, 
    a hyphen, 
    and a zero-padded file number, 
    followed by the original file's extension.

    :param folder_path: The path to the diapo file to be renamed.
    :type folder_path: str
    :param initial_reference_tag: The initial reference tag to be included in the new file name.
    :type initial_reference_tag: str, optional
    :param directory_reference_number: The directory reference number to be included in the new file name.
    :type directory_reference_number: str, optional
    :param file_number: The file number to be included in the new file name.
    :type file_number: int, optional
    :return: The new file name after renaming.
    :rtype: str
    
    """

    import os

    from files.pfo_files import get_file_infos

     # Obtenir le nom du répertoire
    repertoire = os.path.dirname(folder_path)

    # Obtenir l'extension du fichier et la mettre en minuscule
    extension = '.' + get_file_infos(folder_path)['extension']
    extension = extension.lower()

    # Créer le nouveau nom du fichier
    new_name = intial_reference_tag + directory_reference_number + '-{:03d}'.format(file_number) + extension
    new_name = os.path.join(repertoire, new_name)

    return new_name
    

        
