import sys
from PIL import Image

images = []

if len(sys.argv) == 1:
    print("No image files provided. Please provide the path to the image files.")
    sys.exit(1)

try:
    for arg in sys.argv[1:]:
        image = Image.open(arg)
        images.append(image)


    images[0].save(
        "costumes.gif",save_all=True,append_images=[images[1]],duration=200,loop=0
    )

except Exception:
    print("Error: An error occurred while processing the image files.")