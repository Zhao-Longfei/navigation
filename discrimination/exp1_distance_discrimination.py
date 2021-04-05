import random
import cv2
import numpy as np
from PIL import Image,ImageFont,ImageDraw
import os

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)): 
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontStyle = ImageFont.truetype("font/simsun.ttc", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontStyle)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

def Drawing_random_Lines(image,num_test):
    h, w = image.shape[0],image.shape[1]
    x1 = random.uniform(0.5 * w - 75, 0.5 * w)
    y1 = 0.5 * h - np.sqrt(pow(75, 2)-pow(0.5 * w-x1, 2))
    (x2, y2) = (w-x1, h-y1)

    o = np.subtract(y2, y1)
    q = np.subtract(x2, x1)
    slope= - q / o
    d=random.uniform(0,5)
    
    a1=x1 + np.sqrt(abs(pow(d ,2)/(pow(slope,2)-1)))
    b1=y1 + slope * (a1 - x1)

    a2=x2 + np.sqrt(abs(pow(d ,2)/(pow(slope,2)-1)))
    b2=y2 + slope * (a2 - x2)

    cv2.line(image,(int(x1), int(y1)), (int(x2), int(y2)), (0, 225, 0), 1, cv2.LINE_AA)
    image1=image
    cv2.line(image1,(int(a1), int(b1)), (int(a2), int(b2)), (0, 225, 0), 1, cv2.LINE_AA)

    text1 = str(num_test)+"/500"
    text2 = "差がある → Type'Y'"
    text3 = "分からない、迷った → Type'N'"
    text4 = "戻る → Type'ESC'"
    image1=cv2ImgAddText(image1,text1 ,20,20, (0,0,0),20)
    image1=cv2ImgAddText(image1,text2 ,30,730, (0,0,0),15)
    image1=cv2ImgAddText(image1,text3 ,30,750, (0,0,0),15)
    image1=cv2ImgAddText(image1,text4 ,30,770, (0,0,0),15)

    return image1,d

data = [['disatance','YES_NO']]
num_test=num_yes=num_no=0
while True and num_test<500:

    image=np.zeros([800,800,3], np.uint8)+255
    img, d =Drawing_random_Lines(image,num_test)
    cv2.imshow('test', img)
    
    key = cv2.waitKey(0)
    if key == ord('y'):
        print("yes")
        data.append([d,1])
        num_test += 1
        num_yes += 1

    if key == ord('n'):
        print("no")
        data.append([d,0])
        num_test += 1
        num_no += 1

    if key == 27:
        print("End of program")
        break

#print("yes:",num_yes)
#print("no:",num_no)
#print(data)
output = open('data.xls','w',encoding='gbk')
for i in range(len(data)):
	for j in range(len(data[i])):
		output.write(str(data[i][j]))    
		output.write('\t')   
	output.write('\n')      
output.close()
