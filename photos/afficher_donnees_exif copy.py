from exif import Image

folder_path = 'images'
img_filename = 'toto.jpg'

img_path = f'{folder_path}/{img_filename}'

with open(img_path, 'rb') as img_file:
    image = Image(img_file)

if image.has_exif:
    print("L'image contient des métadonnées EXIF.")
    
    data = image.list_all()

    for item in data:
        value = image.get(item)
        print(item, ' = ', value)

else:
    print("L'image ne contient pas de métadonnées EXIF.")