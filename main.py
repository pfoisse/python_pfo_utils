"""Module provided to test some functions"""

from dictionnaires.pfo_dictionnaires import printd

import pandas as pd

from listes.pfo_listes import printl

from files.pfo_files import get_all_files_content_in_a_dataframe

from photos.pfo_photos import extract_some_exif_data
from photos.pfo_photos import change_date
from photos.pfo_photos import change_copyright

chemin = '/Users/pierre/Desktop/images/divers'

print(get_all_files_content_in_a_dataframe(chemin))





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



