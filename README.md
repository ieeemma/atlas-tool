# atlas-tool
A tool for converting Speedrunners Atlas files to JSON and back

## Installation
Head to the [releases](https://github.com/commentsr/atlas-tool/releases) page and download the latest binary.

## Usage
```atlas-tool.exe file.xnb``` to convert an xnb to a json file, and ```atlas-tool.exe file.json``` to convert a json to an xnb  
To decompress game files, download ```RL_uncmp_xnb.bms``` from [this link](https://forum.xentax.com/viewtopic.php?f=32&t=10855) and drag and drop it onto [QuickBMS.exe](https://aluigi.altervista.org/quickbms.htm), then select an XNB file. When I am able to implement decompression this step wont be necessary

## Limitations
- Currently doesn't support compressed files (pop please help heh)
- Currently only supports a proprietary json layout, so no gamefroot/texturepacker compatibility
- Probably has loads of bugs and crashes?

---

# sprite deobfuscation script

## Usage
Disregard the above instructions if you plan on using the sprite deobfuscation script

- if you dont have python, install python (do it yourself)
- copy everything from [RL_uncmp_xnb.bms](https://forum.xentax.com/viewtopic.php?f=32&t=10855) and make a file named liked that where you paste the contents
- download [quickbms](https://aluigi.altervista.org/papers/quickbms.zip)

Download the above 2 files and place them in the same folder as the scripts

- place the unaltered atlas files of the skins you want to extract in the same folder
- place the **EXTRACTED** animation xnbs, so that means you make them into pngs, in the same folder
- in the folder, click on the path and type cmd
- call the scripts as such:
  - ```get_sprites.py [animation_variant number 0-5] [output folder]```
  - Example: ```get-sprites.py 1 white```
  - ```make-images.py [input folder]```
  - Example: ```make-images.py white```

## Additional information

If you want to extract the sprites of another character other than cosmo you need to find that character's hard pixel limit set by the game exe, you cannot find this number anywhere, you have to find it out through trial and error, for example, cosmo's max height is 190, if you dont know this hard limit the sprites you end up making are going to be teared

One way to find it (which I used) is to make a sprite sheet with black and red rectangles of different sizes until you find the correct value, of course
this is done with the help of [pop's atlas generator](https://github.com/pop4959/Atlas-Generator/releases/tag/1.1.5)

## Huge thanks:

Unfortunately i had to edit 1 singular line in this [python script](https://github.com/ieeemma/atlas-tool) to make it work so I can't make people download it on their own and I have to include it with this archive, I'm really sorry to emma, but all credit goes to you for this!
