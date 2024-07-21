"""Module providing to test some functions"""

from dictionnaires.pfo_dictionnaires import printd
from listes.pfo_listes import printl
from files.pfo_files import list_files_in_repertoire
from photos.pfo_photos import extract_some_exif_data

chemin = '/Users/pierre/Desktop/images'

filename = 'PXL_20240720_123424094.MP.jpg'

selection = [
    'datetime',
    'datetime_original',
    'datetime_digitized',
    'gps_longitude'
    ]

data = extract_some_exif_data(chemin, filename, selection)

printd(data)

a = list_files_in_repertoire(chemin)

printl(a)
