
import os, sys
from PIL import Image

def png2snes(pngfile, snesfile, width, height):
    png = Image.open(pngfile)
    assert png.mode == "RGB"
    assert png.size == (width, height)

    snes = Image.new("RGB", (width, height), "black")
    for y in range(height):
        for x in range(width):
            r, g, b = png.getpixel((x, y))
            snes.putpixel((x, y), (r >> 3, g >> 3, b >> 3))

    snes.save(snesfile)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: png2snes.py <pngfile> <snesfile> <width> <height>")
        sys.exit(1)

    pngfile = sys.argv[1]
    snesfile = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])

    png2snes(pngfile, snesfile, width, height)
