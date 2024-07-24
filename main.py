"""Module provided to test some functions"""

import pandas as pd

from files.pfo_files import list_all_files
from files.pfo_files import decoupe_chemin

from photos.pfo_photos import get_date

chemin = '/Users/pierre/Desktop/images/divers'

# Lister les fichiers présents dans le dossier et dans tous les sous-dossiers
liste = list_all_files(chemin)

# Créer une liste de dictionnaires pour stocker les données
data_list = []

# Parcourir les chemins de fichiers
for chemin in liste:

    # Obtenir les informations du répertoire et du fichier
    data_dict = decoupe_chemin(chemin)

    # Obtenir la date de la photo 
    folder_path = data_dict['chemin complet']
    img_filename = data_dict['nom du fichier']
    date_de_la_photo = get_date(folder_path, img_filename)

    # Ajouter la date de la photo au dictionnaire 
    data_dict['date'] = date_de_la_photo
    
    # Ajouter le dictionnaire au DataFrame
    data_list.append(data_dict)

# Convertir la liste de dictionnaires en un DataFrame pandas
df = pd.DataFrame(data_list)

# Afficher le DataFrame
print(df)








