"""Module provided to test some functions"""

import pandas as pd

from files.pfo_files import list_all_files, get_files_data

from photos.pfo_photos import get_original_date, set_original_date, set_digitized_date

from dates.pfo_dates import convert_string_to_datetime, set_duree, convert_datetime_to_string

chemin = '/Users/pierre/Desktop/images/test3'

# Lister les fichiers présents dans le dossier et dans tous les sous-dossiers
liste = list_all_files(chemin)

# Créer une liste de dictionnaires pour stocker les données
data_list = []

# Initialiser le compteur de fichiers
i = 0

# Initialiser le nom du répertoire précédent
previous_repertoire_name = ''

# Parcourir les chemins de fichiers
for chemin in liste:

    # Obtenir les informations du répertoire et du fichier
    data_dict = get_files_data(chemin)

    # Obtenir les dates original et digitized de la photo 
    folder_path = data_dict['chemin complet']
    img_filename = data_dict['nom du fichier']

    # Récupérer la date de la photo et la mettre dans date digitized
    date_originale = get_original_date(folder_path, img_filename)

    date_digitized = date_originale
    
    nom_repertoire = data_dict['nom du répertoire']
    
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
    data_dict['date_originale'] = new_date
    data_dict['date_digitized'] = date_digitized
    
    # Ajouter le dictionnaire au DataFrame
    data_list.append(data_dict)

    set_digitized_date(folder_path, img_filename, date_digitized)
    set_original_date(folder_path, img_filename, new_date)

    previous_repertoire_name = nom_repertoire

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











