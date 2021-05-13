import numpy as np
from numpy import array
from PIL import Image
from sys import argv

if len(argv) < 2:
    print("Error! Not enough parameters")
    exit(-1)

try:
    image = Image.open(argv[1])
except:
    print("No such image!")
    exit(-1)
image_arr = array(image)

for i in range(image_arr.shape[0]):
    for j in range(image_arr.shape[1]):
        brightness = int(image_arr[i][j][0]) + image_arr[i][j][1] + image_arr[i][j][2]
        image_arr[i][j][0] = brightness / 3
        image_arr[i][j][1] = brightness / 3
        image_arr[i][j][2] = brightness - image_arr[i][j][1] - image_arr[i][j][0]

new_im = Image.fromarray(image_arr)
new_im.save(argv[2])