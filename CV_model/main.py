from PIL import Image
from PIL import Image, ImageDraw
import sys
import os

im = Image.open(sys.argv[1])
pix = im.load()

goods = []

for i in range(8,im.size[0]-8,8):
    for j in range(8,im.size[1]-8,8):
        for k in range(15):
            if(sum(pix[i-k,j-k][:3]) > 120):
                break
            if(sum(pix[i-k,j+k][:3]) > 120):
                break
            if(sum(pix[i+k,j-k][:3]) > 120):
                break
            if(sum(pix[i+k,j+k][:3]) > 120): 
                break

            if(k == 14):
                goods.append([i,j])
                break
print("Done\n")

for i in goods:
    draw = ImageDraw.Draw(im)
    draw.ellipse((i[0],i[1],i[0]+10,i[1]+10), fill="red", outline="red")

im.save(open("res.png", "wb"), "PNG")