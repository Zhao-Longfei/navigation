import random
import cv2
import numpy as np
from PIL import Image,ImageFont,ImageDraw


def Drawing_random_Lines(image):
    h, w = image.shape[0],image.shape[1]
    x1 = random.randint(0.5 * w - 75, 0.5 * w)
    y1 = 0.5 * h - np.sqrt(pow(75, 2)-pow(0.5 * w-x1, 2))
    (x2, y2) = (w-x1, h-y1)

    o = np.subtract(y2, y1)
    q = np.subtract(x2, x1)
    slope= - q / o
    d=random.randint(0,10)
    
    a1=x1 + np.sqrt(pow(d ,2)/(pow(slope,2)-1))
    b1=y1 + slope * (a1 - x1)

    a2=x2 + np.sqrt(pow(d ,2)/(pow(slope,2)-1))
    b2=y2 + slope * (a2 - x2)

    cv2.line(image,(int(x1), int(y1)), (int(x2), int(y2)), (0, 225, 0), 1, cv2.LINE_AA)
    image1=image
    cv2.line(image1,(int(a1), int(b1)), (int(a2), int(b2)), (0, 225, 0), 1, cv2.LINE_AA)
    return image1

data_directory = 'plan\\'
#image=cv2.imread(data_directory+'001'+'.png',1)
image=cv2.imread('plan\\002.jpg',1)
image1=Drawing_random_Lines(image)


cv2.imshow("image", image1)
cv2.waitKey(0)