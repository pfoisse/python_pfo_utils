"""Module provided to test some functions"""

import pandas as pd

from files.pfo_files import list_all_files
from files.pfo_files import get_files_data

from photos.pfo_photos import get_original_date
from photos.pfo_photos import set_original_date

chemin = '/Users/pierre/Desktop/images/test1'

# Lister les fichiers présents dans le dossier et dans tous les sous-dossiers
liste = list_all_files(chemin)

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
    date_originale = get_original_date(folder_path, img_filename)
    date_digitized = date_originale

    nom_repertoire = data_dict['nom du répertoire']

    date_originale = set_original_date(folder_path, img_filename, nom_repertoire)
    
    # Ajouter la date de la photo au dictionnaire 
    data_dict['date_originale'] = date_originale
    data_dict['date_digitized'] = date_digitized
    
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










