import os
from PIL import Image


img_dir = "testdir/"
dirs = os.listdir( img_dir )

def resize_bulk_images():
	for img in dirs:
		if os.path.isfile(img_dir + img):
			im = Image.open(img_dir + img)
			f, e = os.path.splitext(img_dir + img)
			imResize = im.resize((1200, 628), Image.ANTIALIAS)
			imResize.save(f + '_resized.jpg', 'JPEG', quality=90)

print('Bulk images resizing started...')
resize_bulk_images()
print('Bulk images resizing finished...')