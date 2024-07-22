from exif import Image

folder_path = 'images'
img_filename = 'PXL_20240720_192436027.MP.jpg'

img_path = f'{folder_path}/{img_filename}'

with open(img_path, 'rb') as img_file:
    image = Image(img_file)

    image.datetime_original = '2024:07:20 10:00:00'
    image.copyright = "FOISSELON"

    
