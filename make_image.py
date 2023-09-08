from PIL import Image
import sys
import os

if __name__ == "__main__":
    sprite_width = 270
    sprite_height = 190 # change this for different characters
    sprites_per_column = 20 # dont go above 22, nice even number is ok
    image_height = sprite_height * sprites_per_column
    image_width = 4590 # kept like this in case you want full taunt animation (you have to change sprites_files below)
    row_spacing = 270

    if len(sys.argv) == 1:
        print("Usage: make-images.py [input folder]\nExample: make-images.py white")
        raise SystemExit
    else:
        directory = sys.argv[1]

    image = Image.new("RGBA", (image_width, image_height), (255, 255, 255, 0))

    sprite_files = [filename for filename in os.listdir(directory) if filename.endswith(".png") and ("Taunt0001" in filename or not "Taunt0" in filename)]

    x_position = 0
    y_position = 0
    
    with open(directory + "_sprite_names.txt", "w") as f:
        for sprite_file in sprite_files:
            if y_position + sprite_height > image_height:
                break

            sprite = Image.open(os.path.join(directory, sprite_file))
            image.paste(sprite, (x_position, y_position))

            f.write(sprite_file[:-4] + "\n")

            y_position += sprite_height
            if y_position + sprite_height > image_height:
                y_position = 0
                x_position += sprite_width

            if x_position + sprite_width > image_width:
                break

    image.save(directory + ".png")
