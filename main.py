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

print(data)





