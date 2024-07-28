"""Module providing some functions to work with diapos
"""

#! --------------------------------------------------------------------------------------
def rename_all_diapos_in_reverse_order(folder_path):
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



        
