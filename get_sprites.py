import os
import sys
import importlib
from PIL import Image, ImageOps
atlas_tool = importlib.import_module("atlas-tool")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: get_sprites.py [animation_variant number 0-5] [output folder]\nExample: get-sprites.py 1 white")
        raise SystemExit
    else:
        directory = sys.argv[2]
        i = sys.argv[1]
    os.mkdir(directory)

    atlas = atlas_tool.AtlasFile()
    atlas_file_name = "animation_atlas_variant0" + str(i) + ".xnb"
    png_file_name = "animation_variant0" + str(i) + ".png"
    xnb_unpacked_name = "animation_atlas_variant0" + str(i) + "_unpacked.xnb"

    image = Image.open(png_file_name)
    os.system("quickbms.exe RL_uncmp_xnb.bms " + atlas_file_name)

    atlas.read(xnb_unpacked_name)
    for j in atlas.atlas_data_items:
        sprite = image.crop((j.sprite_x, j.sprite_y, j.sprite_x + j.sprite_h, j.sprite_y + j.sprite_w))
        sprite = ImageOps.expand(sprite, border=(int(j.bounding_box_x),int(j.bounding_box_y),0,0), fill=(0,0,0,0))
        sprite.save(directory + f"\{j.name}.png")
    os.remove(xnb_unpacked_name)
