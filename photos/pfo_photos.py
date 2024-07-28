"""Module providing some functions to work with photos
extraction des informations EXIF (Exchangeable image file format) d'une photo. 
L'information EXIF contient des métadonnées sur une image, comme la résolution, 
le format, les informations de prise de vue, etc.
"""

from exif import Image

#from files.pfo_files import list_all_files, get_files_data
#from dates.pfo_dates import convert_string_to_datetime, set_duree, convert_datetime_to_string

# ! --------------------------------------------------------------------------------------
def get_all_exif_data(folder_path, img_filename):
    """
    Cette fonction extrait toutes les données EXIF d'une photo. 
    Elle prend en argument le chemin du répertoire où se trouve la photo 
    et le nom du fichier de la photo. 
    Elle retourne un dictionnaire contenant toutes les données EXIF de la photo.

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.

    Returns:
        dictionnaire: 
        cle = parametre EXIF
        valeur = valeur du parametre EXIF

    Example:
        >>> extraire_donnees_exif('images', 'toto.jpg')
        
        x_resolution
        72.0

        y_resolution
        72.0

        resolution_unit
        2

        datetime
        2024:07:20 14:34:24

        exposure_time
        0.000479

    """

    # chemin complet vers le fichier de la photo
    img_path = f'{folder_path}/{img_filename}'

    # création d un objet Image contenant les données de la photo
    with open(img_path, 'rb') as img_file:
        image = Image(img_file)

    # si l image continet des donnees EXIF
    if image.has_exif:

        # extraire la liste de  tous les paralmetres EXIF contenus dans la photo
        data = image.list_all()

        # intialiser un dictionnaire vide pour mettre kles resultats
        d = {}

        # pour chacun des parametres EXIF de la photo
        for item in data:

            # extraitre la valeur du parametre EXIF concerné
            value = image.get(item)

            # mettre cette valeur dans le ditionnaire qui contiendra les resultats
            d[item] = value

    # si l image ne contient pas de données EXIF, renvoyer un dictionnaire vide
    else:

        d={}

    # retourner le dictionnaire

    return d

# ! --------------------------------------------------------------------------------------
def get_one_exif_data(folder_path, img_filename, exif_tag):
    """
    Cette fonction extrait une seule donnée EXIF d'une photo. 
    Elle prend en argument le chemin du répertoire où se trouve la photo, 
    le nom du fichier de la photo et le nom du paramètre EXIF recherché. 
    Elle retourne la valeur du paramètre EXIF recherché.

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.
        exif_tag (chain): nom du parametre exif recherché, ex :

            datetime
            datetime_original
            datetime_digitized
            offset_time
            offset_time_original
            offset_time_digitized
            subject_distance
            pixel_x_dimension
            pixel_y_dimension
            lens_make
            lens_model
            gps_version_id
            gps_latitude_ref
            gps_latitude
            gps_longitude_ref
            gps_longitude
            gps_altitude_ref
            gps_altitude
            gps_timestamp
            gps_img_direction_ref
            gps_img_direction
            gps_datestamp

    Returns:
        dictionnaire: 
        cle = parametre EXIF
        valeur = valeur du parametre EXIF

    Example:
        >>> extraire_donnees_exif('images', 'toto.jpg', 'datetime_original')
    
        2024:07:20 14:34:24

    """

    #extraire toutes les données EXIF
    data = get_all_exif_data(folder_path, img_filename)

    # retourner la valeur du dictionnaire correspondant a la cle exif_data
    return data[exif_tag]

## ! --------------------------------------------------------------------------------------
def get_some_exif_data(folder_path, img_filename, tag_selection):
    """
    Cette fonction extrait plusieurs données EXIF d'une photo. 
    Elle prend en argument le chemin du répertoire où se trouve la photo, 
    le nom du fichier de la photo et une liste des noms des paramètres EXIF recherchés. 
    Elle retourne un dictionnaire contenant les valeurs des paramètres EXIF recherchés.

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.
        exif_data (table): tableau avec les noms du parametre exif recherché, ex :

        tag_selection = [
            'datetime',
            'datetime_original',
            'datetime_digitized'
        ]

    Returns:
        dictionnaire: 
        cle = parametre EXIF
        valeur = valeur du parametre EXIF

    Example:
        >>> extraire_donnees_exif('images', 'toto.jpg', 'datetime_original')
    
        2024:07:20 14:34:24

    """

    d = {}

    for tag in tag_selection:

        value = get_one_exif_data(folder_path, img_filename, tag)
        d[tag] = value

    return d

# ! --------------------------------------------------------------------------------------
def set_exif_data(folder_path, img_filename, exif_tag, new_value):
    """
    Cette fonction permet de changer la valeur d'un paramètre EXIF d'une photo. 
    Elle prend en argument le chemin du répertoire où se trouve la photo, 
    le nom du fichier de la photo, le nom du paramètre EXIF à modifier 
    et la nouvelle valeur de la donnée EXIF. 
    Elle retourne la nouvelle photo avec le nouveau paramètre EXIF.     

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.
        
        exif_tag (chain): nom du parametre EXIF à modifier
            ex : 'datetime_original'
            ex : 'copyright'

        new_value (chain): nouvelle valeur de la donnee EXIF
            ex : '2024:07:20 14:34:24'
            ex : 'FOISSELON'
        
    Returns:
        La nouvelle photo avec le nouveau tag EXIF

    Example:
        >>> set_exif_data('images', 'toto.jpg', 'datetime_original', '2024:07:20 14:34:24')

    """
    # On crée le chemin d acces à l'image
    img_path = f'{folder_path}/{img_filename}'

    # On ouvre l'image
    with open(img_path, 'rb') as img_file:
        image = Image(img_file)

    # On modifie la valeur du tag EXIF
    if exif_tag == 'datetime_original':

        image.datetime_original = new_value 

    elif exif_tag == 'copyright':

        image.copyright = new_value

    # On sauvegarde le fichier avec les nouvelles données EXIF
    with open(f'{folder_path}/{img_filename}', 'wb') as new_image_file:
        new_image_file.write(image.get_file())

# ! --------------------------------------------------------------------------------------
def get_original_date(folder_path, img_filename):
    """
    Extrait la date originale d'une photo.

    Args:
        chemin_dossier (str): Le chemin du dossier où se trouve la photo.
        nom_fichier (str): Le nom du fichier de la photo.

    Returns:
        str: La valeur du paramètre EXIF 'datetime_original', qui représente la date originale de la photo.

    Exemple:
        >>> get_original_date('images', 'toto.jpg')
        2024:07:20 14:34:24
    """

    # extraire la date de la photo
    value = get_one_exif_data(folder_path, img_filename, 'datetime_original')

    return value

# ! --------------------------------------------------------------------------------------
def set_original_date(folder_path, img_filename, new_date):
    """
    Cette fonction permet de changer la date originale d'une photo. 
    Elle prend en argument le chemin du répertoire où se trouve la photo, 
    le nom du fichier de la photo et la nouvelle date de la photo. 
    Elle retourne la nouvelle photo avec la nouvelle date.     

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.
        new_date (datetime): nouvelle date de la photo.
        
    Returns:
        La nouvelle photo avec le nouveau tag EXIF

    Example:
        >>> set_exif_data('images', 'toto.jpg', '2024:07:20 14:34:24')

    """

    set_exif_data(folder_path, img_filename, 'datetime_original', new_date)

# ! --------------------------------------------------------------------------------------
def get_digitized_date(folder_path, img_filename):
    
    """
    Cette fonction extrait la date digitized d'une photo.

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.

    Returns:
        str: valeur du paramètre EXIF 'datetime_original'.

    Example:
        >>> get_original_date('images', 'toto.jpg')
        2024:07:20 14:34:24 

    """

    # extraire la date de la photo
    value = get_one_exif_data(folder_path, img_filename, 'datetime_digitized')

    return value

# ! --------------------------------------------------------------------------------------
def set_digitized_date(folder_path, img_filename, new_date):
    """
    Cette fonction permet de changer la date d'une photo. 
    Elle prend en argument le chemin du répertoire où se trouve la photo, 
    le nom du fichier de la photo et la nouvelle date de la photo. 
    Elle retourne la nouvelle photo avec la nouvelle date.     

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.
        new_date (datetime): nouvelle date de la photo.
        
    Returns:
        La nouvelle photo avec le nouveau tag EXIF

    Example:
        >>> set_exif_data('images', 'toto.jpg', '2024:07:20 14:34:24')

    """

    set_exif_data(folder_path, img_filename, 'datetime_digitized', new_date)

# ! --------------------------------------------------------------------------------------
def set_copyright(folder_path, img_filename, new_copyright):
    """
    Cette fonction permet de changer le copyright d'une photo. 
    Elle prend en argument le chemin du répertoire où se trouve la photo, 
    le nom du fichier de la photo et le nouveau copyright de la photo. 
    Elle retourne la nouvelle photo avec le nouveau copyright.    

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.
        new_copyright (chain): nouveau copyright de la photo.
        
    Returns:
        La nouvelle photo avec le nouveau tag EXIF

    Example:
        >>> set_exif_data('images', 'toto.jpg', 'FOISSELON')

    """

    set_exif_data(folder_path, img_filename, 'copyright', new_copyright)

#! --------------------------------------------------------------------------------------
def get_copyright(folder_path, img_filename):
    """
    Cette fonction extrait le copyright d'une photo.

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.

    Returns:
        str: valeur du paramètre EXIF 'copyright'.

    Example:
        >>> get_copyright('images', 'toto.jpg')
        FOISSELON 

    """

    # extraire le copyright de la photo
    value = get_one_exif_data(folder_path, img_filename, 'copyright')

    return value

##! --------------------------------------------------------------------------------------
def show_all_photos_files_caracterictics(folder_path):
    """
    Cette fonction affiche les caractéristiques des photos dans un répertoire 
    et dans tous ses sous-dossiers.

    Args:
        folder_path (chain): chemin du répertoire où se trouve les photos.

    Returns:
        None

    Example:
        >>> show_all_files_caracterictics('images')
    """
    import pandas as pd
    from files.pfo_files import list_all_files, get_files_data

    # Lister les fichiers présents dans le dossier et dans tous les sous-dossiers
    liste = list_all_files(folder_path)

    # Créer une liste de dictionnaires pour stocker les données
    data_list = []

    # Parcourir les chemins de fichiers
    for chemin in liste:

        # Obtenir les informations du répertoire et du fichier
        data_dict = get_files_data(chemin)

        # Obtenir les dates original et digitized de la photo 
        folder_path = data_dict['chemin complet']
        img_filename = data_dict['nom du fichier']

        # Récupérer la date de la photo et la mettre dans date digitized
        data_dict['date_originale'] = get_original_date(folder_path, img_filename)
        data_dict['date_digitized'] = get_digitized_date(folder_path, img_filename)
        
        # Ajouter le dictionnaire au DataFrame
        data_list.append(data_dict)

    # Convertir la liste de dictionnaires en un DataFrame pandas
    df = pd.DataFrame(data_list)

    # Afficher le DataFrame
    pd.set_option('display.max_colwidth', 0)
    pd.set_option('display.max_rows', 0)
    pd.options.display.width = 0
    pd.options.display.max_seq_items = 1000
    pd.options.display.float_format = '{:,.2f}'.format
    pd.options.display.precision = 2
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    selection = [
        'nom du fichier', 
        'nom du répertoire',
        'date_originale', 
        'date_digitized'
        ]

    print(df[selection])

#! --------------------------------------------------------------------------------------
def change_all_original_dates_according_to_directories_names(folder_path):
    """
    Cette fonction modifie la date originale de toutes les photos dans un répertoire 
    et dans tous ses sous-dossiers.

    Args:
    folder_path (chain): chemin du répertoire où se trouve les photos.

    Returns:

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

        # On fait un TRY pour gérer les erreurs au cas où le nom du répertoire n'est pas dans le format YYYY-MM-DD
        try:
            # Convertir la date du répertoire en datetime
            new_date = convert_string_to_datetime(nom_repertoire)

            # Ajouter la durée de 1 seconde au dernier enregistrement de la photo
            duree = set_duree(seconds=1)
            new_date = new_date + i * duree 

            # Convertir la date en string avec le format double points
            new_date = convert_datetime_to_string(new_date, 'double_points')
            
            # Ajouter la date original et de la date digitilized de la photo au dictionnaire 
            set_original_date(folder_path, img_filename, new_date)

        except:
            print(f'Erreur lors de la conversion du répertoire {nom_repertoire} en date')
            continue

        
        previous_repertoire_name = nom_repertoire

    
        