import os
from PIL import Image

image_dir = os.listdir('testdir')

for image in image_dir:
    im = Image.open('testdir/' + image)
    width, height = im.size
    new_width = 1000
    ratio = new_width/width
    new_height = int(height * ratio)
    new_image = im.resize((new_width, new_height))
    new_image.save('testdir/' + image, optimize = True, quality = 30)