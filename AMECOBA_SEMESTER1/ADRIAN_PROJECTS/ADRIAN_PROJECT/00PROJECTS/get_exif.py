from PIL import Image

im = Image.open("IMG_6782.JPG")

exif = im._getexif()

for id, value in exif.items():
    print(id, value)