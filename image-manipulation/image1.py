from PIL import Image

with Image.open('buildings.jpg') as img:
    img.load()



# Methods to show image properties
# img.show()
# print(img.size)
# print(img.format)
# print(img.mode)



# crop and resize your Image
cropped_img = img.crop((300,150,700,1000))
# cropped_img.show()

resized_img = cropped_img.resize((cropped_img.width//4,cropped_img.height//4))
# print(resized_img.size)
# resized_img.show()


# Image reduction can same happened with the reduce
# low_res_img = cropped_img.reduce(4) , the argument defines the scale to which you can scale the Image down.

# Once you’re happy with your returned image, you can save any of the Image objects to file using .save():
# cropped_img.save("cropped_img.jpg")
# resized_img.save("low-resolution-img")

# Basic Image Manipulation
converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
# converted_img.show()

# There are seven options that you can pass as arguments to .transpose():

# Image.FLIP_LEFT_RIGHT: Flips the image left to right, resulting in a mirror image
# Image.FLIP_TOP_BOTTOM: Flips the image top to bottom
# Image.ROTATE_90: Rotates the image by 90 degrees counterclockwise
# Image.ROTATE_180: Rotates the image by 180 degrees
# Image.ROTATE_270: Rotates the image by 270 degrees counterclockwise, which is the same as 90 degrees clockwise
# Image.TRANSPOSE: Transposes the rows and columns using the top-left pixel as the origin, with the top-left pixel being the same in the transposed image as in the original image
# Image.TRANSVERSE: Transposes the rows and columns using the bottom-left pixel as the origin, with the bottom-left pixel being the one that remains fixed between the original and modified versions