"""Module providing some functions to work with diapos
"""

#! --------------------------------------------------------------------------------------
def rename_all_diapos_in_reverse_order(folder_path):
    """
    
    """

    from files.pfo_files import list_all_files, get_files_data
    from dates.pfo_dates import convert_string_to_datetime, set_duree, convert_datetime_to_string

    # Lister les fichiers présents dans le dossier et dans tous les sous-dossiers
    liste = list_all_files(folder_path)

    # Initialiser le compteur de fichiers
    i = 0

    # Initialiser le nom du répertoire précédent
    previous_repertoire_name = ''

    # Parcourir tous les chemins de fichiers
    for chemin in liste:

        # Obtenir les informations du répertoire et du fichier
        data = get_files_data(chemin)

        # Obtenir les dates original et digitized de la photo 
        folder_path = data['chemin complet']
        img_filename = data['nom du fichier']
        
        nom_repertoire = data['nom du répertoire']
        
        # si le fichier est encore dans le meme repertoire
        # alors ajouter 1 seconde a la date du fichier
        # sinon reinitialiser le compteur
        if nom_repertoire == previous_repertoire_name:
            i = i + 1
        else:
            i = 0

        # Convertir la date du répertoire en datetime
        new_date = convert_string_to_datetime(nom_repertoire)

        # Ajouter la durée de 1 seconde au dernier enregistrement de la photo
        duree = set_duree(seconds=1)
        new_date = new_date + i * duree 

        # Convertir la date en string avec le format double points
        new_date = convert_datetime_to_string(new_date, 'double_points')
        
        # Ajouter la date original et de la date digitilized de la photo au dictionnaire 
        set_original_date(folder_path, img_filename, new_date)

        previous_repertoire_name = nom_repertoire

    
        