import os.path

import cv2 as cv
import turtle as t
import numpy as np
import math
import sys


img_org = cv.resize(cv.imread(r'IMAGE_PATH_HERE'), (438, 300)) # dont forget to change the image path and the dimensions
img_gray = cv.cvtColor(img_org, cv.COLOR_BGR2GRAY)

(thresh, img_bw) = cv.threshold(img_gray, 150, 255, 0) # my threshold is set at 150 rgb value

cv.imshow('bw', img_bw)

cv.waitKey(0)
cv.destroyAllWindows()
img_dimensions = img_bw.shape
img_width = img_dimensions[0]
img_height = img_dimensions[1]

t.screensize(img_width, img_height)
t.pencolor('black')
t.resizemode('user')
t.shape('classic')
t.speed('fastest')
# t.pensize()

for i in range(int(img_height/2), int(img_height/-2),  -1):
    t.penup()
    t.goto(-(img_width / 2), i)

    for l in range(-int(img_width/2), int(img_width/2), 1):
        pix_width = int(l + (img_width/2))
        pix_height = int(img_height/2 - i)
        if img_bw[pix_height, pix_width] == 0:
            t.pendown()
            t.forward(1)
        else:
            t.penup()
            t.forward(1)
    t.update()




