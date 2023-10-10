from PIL import Image
from PIL import ImageOps
import os
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1].strip()
    output_file = sys.argv[2].strip()
    overlay_file = "shirt.png"

    if is_valid_input(input_file, output_file):
        overlay_shirt(input_file, output_file, overlay_file)

def is_valid_input(input_file, output_file):
    input_extension = os.path.splitext(input_file)[1].lower()
    output_extension = os.path.splitext(output_file)[1].lower()

    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")

    valid_extensions = [".jpg", ".jpeg", ".png"]

    if input_extension not in valid_extensions or output_extension not in valid_extensions:
        sys.exit("Invalid input")

    return True

def overlay_shirt(input_file, output_file, overlay_file):
    input_image = Image.open(input_file)
    overlay_image = Image.open(overlay_file)

    # resize / crop the input image to the size of the overlay
    cropped_input_image = ImageOps.fit(input_image, overlay_image.size)
    cropped_input_image.paste(overlay_image, overlay_image)
    cropped_input_image.save(output_file)

if __name__ == "__main__":
    main()