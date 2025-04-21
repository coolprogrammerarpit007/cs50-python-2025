from PIL import Image,ImageOps
import sys


#  check if file format is valid or not.
def check_file_format(file):
    if file.endswith(".png") or file.endswith(".jpg"):
        return True
    return False

# check if both input and output images has same extensions

def check_file_type(file1,file2):
    if file1.endswith(".png") and file2.endswith(".png"):
        return True
    elif file1.endswith(".jpg") and file2.endswith(".jpg"):
        return True
    return False


if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

if not check_file_format(sys.argv[2]):
    print("Invalid output")
    sys.exit(1)

if not check_file_type(sys.argv[1],sys.argv[2]):
    print("Input and output have different extensions")
    sys.exit(1)



try:
    input_img = sys.argv[1]
    shirt_img = Image.open('shirt.png').convert("RGBA")
    shirt_img_width,shirt_img_height = shirt_img.size
    background = Image.open(input_img).convert("RGBA")
    background = ImageOps.fit(background,(shirt_img_width,shirt_img_height))
    background.paste(shirt_img,(0,0),shirt_img)
    result = background.convert("RGB")
    result.save(sys.argv[2])
    

except FileNotFoundError:
    print("File not found")
    sys.exit(1)
   
    
        

    
    


