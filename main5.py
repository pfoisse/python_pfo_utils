
import os

from files.pfo_files import list_all_files, list_all_directories, get_file_infos, rename_file
from diapos.pfo_diapos import rename_a_diapo

chemin = '/Users/pierre/Desktop/images/test3'

print('#############################################################')
print('#############################################################')
print('#############################################################')
print()
print('chemin = ', chemin)
print()

# Lister les répertoires présents dans le dossier et dans tous les sous-repertoires
liste_repertoires = list_all_directories(chemin)


for repertoire in liste_repertoires:

    print('---------------------------------------------------')
    print(repertoire, 'ORDRE INVERSE')

     # Extract the last element of the repertoire string
    last_element = repertoire.split('/')[-1]

    # Extract the first 3 characters of the last_element string
    first_3_chars = last_element[:3]

    print('First 3 characters of the repertoire:', first_3_chars)
    print('Last element of the repertoire:', last_element)

    print('---------------------------------------------------')

    # Lister les fichiers présents dans le dossier
    liste_fichiers = list_all_files(repertoire)

    # Inverser la liste des fichiers
    liste_fichiers = list(reversed(liste_fichiers))

    # Obtenir le nombre de fichiers dans la liste
    nombre_fichiers = len(liste_fichiers)

    print('Nombre de fichiers :', nombre_fichiers)

    # Parcourir les noms des fichiers
    for i, fichier in enumerate(liste_fichiers):

        # Obtenir les informations sur le fichier
        nom_fichier = get_file_infos(fichier)['nom du fichier']
        old_name = os.path.join(repertoire, nom_fichier)
        print('OLD name :', old_name)

        # Si le nom du fichier commence par 'DIAPO'
        if nom_fichier.startswith('DIAPO'):

            print('Pas de changement de nom')

        else:

            print('--------------------------------------------')

            

            # Obtenir l'extension du fichier
            extension = '.' + get_file_infos(fichier)['extension']

            new_name = rename_a_diapo(old_name, intial_reference_tag ='DIAPO-', directory_reference_number=first_3_chars, file_number=i+1)
            
            print('NEW name :', new_name)
            
            #rename_file(old_name, new_name)
    
 