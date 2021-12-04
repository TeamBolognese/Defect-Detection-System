from PIL import Image
from PIL import Image, ImageDraw
import sys
from scipy import stats
from collections import Counter
import numpy as np

for w in ['1','2','4','5']:
    im = Image.open("datasets/training_data/"+w+".png") # some training
    pix = im.load()

    cords = []

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if(pix[i,j][:3] == (255, 0, 0)):
                cords.append([i,j]) # сбор координат помеченного брака

    im = Image.open("datasets/bads/"+w+".png") # open original defect-photo
    pix = im.load()

    deffarr = []

    for i in cords:
        deffarr.append(pix[i[0],i[1]])

    print(stats.describe(deffarr))
    print("np median: ", np.median(deffarr))
    print("np mean: ", np.mean(deffarr))
    print("most common RGB: ", Counter(deffarr).most_common()[0])

    # Главные признаки были использованы в модели.
