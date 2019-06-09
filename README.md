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
