"""Module providing to test some functions"""

import os

from dictionnaires.pfo_dictionnaires import printd

from listes.pfo_listes import printl

from files.pfo_files import list_all_files
from files.pfo_files import get_directory_name

from photos.pfo_photos import extract_some_exif_data
from photos.pfo_photos import change_date
from photos.pfo_photos import change_copyright

chemin = '/Users/pierre/Desktop/images/divers'

filename = 'PXL_20240720_123424094.MP.jpg'

# change_date(chemin, filename, '1998:01:01 00:00:01')
# change_copyright(chemin, filename, 'ernest')

# selection = [
#     'datetime_original',
#     'copyright'
#     ]

# data = extract_some_exif_data(chemin, filename, selection)

# printd(data)


# a = list_files_in_repertoire(chemin)
# printl(a)

liste = list_all_files(chemin)

for item in liste:
    print(item)
    print(get_directory_name(item))
    


