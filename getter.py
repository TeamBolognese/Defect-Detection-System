from PIL import Image
import sys

im = Image.open(sys.argv[1])
pixels = list(im.getdata())

print(pixels)
