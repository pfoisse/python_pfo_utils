from exif import Image

# ! --------------------------------------------
def extract_all_exif_data(folder_path, img_filename):
    """
    Extraire toutes les données EXIF d une photo 

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

# ! --------------------------------------------
def extract_one_exif_data(folder_path, img_filename, exif_data):
    """
    Extraire une seule donnee EXIF d une photo 

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.
        exif_data (chain): nom du parametre exif recherché, ex :

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
    data = extract_all_exif_data(folder_path, img_filename)

    # retourner la valeur du dictionnaire correspondant a la cle exif_data
    return data[exif_data]

# ! --------------------------------------------
def extract_some_exif_data(folder_path, img_filename, selection):
    """
    Extraire plusieurs donnees EXIF d une photo 

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.
        exif_data (table): tableau avec les noms du parametre exif recherché, ex :

        selection = [
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

    for tag in selection:

        value = extract_one_exif_data(folder_path, img_filename, tag)
        d[tag] = value

    return d

