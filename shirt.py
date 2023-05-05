import sys
import os
from PIL import Image, ImageOps
def main():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)==3:
        path_check()
        try:
            image1 = Image.open(sys.argv[1])
            image2 = Image.open('shirt.png')
            new_size = image2.size
            image1 = ImageOps.fit(image1, new_size)
            image1.paste(image2, mask=image2)
            image1.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Input does not exist")
    else:
        sys.exit("Too many command-line arguments")

def path_check():
    path = sys.argv[1]
    ext = os.path.splitext(path)
    path_2 = sys.argv[2]
    second_ext = os.path.splitext(path_2)

    if ext[1] == "":
        sys.exit("Invalid input")
    elif ext[1] not in [".png", ".jpeg", ".jpg"]:
        sys.exit("Invalid input")
    elif second_ext[1] == "":
        sys.exit("Invalid output")
    elif second_ext[1] not in [".png", ".jpeg", ".jpg"]:
        sys.exit("Invalid output")
    elif (ext[1] in [".png", ".jpeg", ".jpg"]) and (second_ext[1] in [".png", ".jpeg", ".jpg"]):
        if ext[1]!=second_ext[1]:
            sys.exit("Input and output have different extensions")
        else:
            return True
if __name__ == "__main__":
    main()
