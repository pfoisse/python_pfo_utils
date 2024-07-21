from exif import Image
import os

folder_path = 'images'

# Liste des fichiers dans le répertoire
fichiers = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith('.')])

# Afficher la liste des fichiers
for img_filename in fichiers:

    img_path = f'{folder_path}/{img_filename}'

    with open(img_path, 'rb') as img_file:

        image = Image(img_file)

        print('---')
        print(img_filename)
        print('Date Prise de Vue : ', image.get('datetime_original'))

