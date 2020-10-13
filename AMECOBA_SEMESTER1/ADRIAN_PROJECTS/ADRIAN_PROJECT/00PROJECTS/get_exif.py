from PIL import Image

im = Image.open("kyoto.jpg")

exif = im._getexif()

for id, value in exif.items():
    print(id, value)