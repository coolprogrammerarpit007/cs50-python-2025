# Bands and Modes of an Image in the Python Pillow Library
from PIL import Image

filename = 'strawberry.jpg'

with Image.open(filename) as img:
    img.load()

# print(img.mode)
# img.show()


# converting images into the various modes.
cmyk_img = img.convert("CMYK")
# cmyk_img.show()
gray_img = img.convert("L")
# gray_img.show()
# img.getbands()   will o/p ('R', 'G', 'B')
# The outputs from the calls to .getbands() confirm that there are three bands in the RGB image, four bands in the CMYK image, and one band in the grayscale image.