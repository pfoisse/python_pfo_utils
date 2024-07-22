"""Module providing some functions to work with photos"""

import datetime

from exif import Image

# ! --------------------------------------------------------------------------------------
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

# ! --------------------------------------------------------------------------------------
def extract_one_exif_data(folder_path, img_filename, exif_tag):
    """
    Extraire une seule donnee EXIF d une photo 

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
    data = extract_all_exif_data(folder_path, img_filename)

    # retourner la valeur du dictionnaire correspondant a la cle exif_data
    return data[exif_tag]

## ! --------------------------------------------------------------------------------------
def extract_some_exif_data(folder_path, img_filename, tag_selection):
    """
    Extraire plusieurs donnees EXIF d une photo 

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

        value = extract_one_exif_data(folder_path, img_filename, tag)
        d[tag] = value

    return d

# ! --------------------------------------------------------------------------------------
def change_exif_data(folder_path, img_filename, exif_tag, new_value):
    """
    Changer la valeur d'une donnee EXIF d une photo     

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
        >>> change_exif_data('images', 'toto.jpg', 'datetime_original', '2024:07:20 14:34:24')

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
def change_date(folder_path, img_filename, new_date):
    """
    Changer la date d une photo     

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.
        new_date (datetime): nouvelle date de la photo.
        
    Returns:
        La nouvelle photo avec le nouveau tag EXIF

    Example:
        >>> change_exif_data('images', 'toto.jpg', '2024:07:20 14:34:24')

    """

    change_exif_data(folder_path, img_filename, 'datetime_original', new_date)

# ! --------------------------------------------------------------------------------------
def change_copyright(folder_path, img_filename, new_copyright):
    """
    Changer le copyright d une photo     

    Args:
        folder_path (chain): chemin du repertoire où se trouve la photo.
        img_filename (chain): nom de fichier de la photo.
        new_copyright (chain): nouveau copyright de la photo.
        
    Returns:
        La nouvelle photo avec le nouveau tag EXIF

    Example:
        >>> change_exif_data('images', 'toto.jpg', 'FOISSELON')

    """

    change_exif_data(folder_path, img_filename, 'copyright', new_copyright)

        