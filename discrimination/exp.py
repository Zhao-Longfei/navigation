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

def random_line(image,num_test,content):
    h, w = image.shape[0],image.shape[1]
    length = 150
    x1 = random.uniform(0.5 * w - length / 2, 0.5 * w)
    y1 = 0.5 * h - np.sqrt(pow(length / 2, 2)-pow(0.5 * w-x1, 2))
    (x2, y2) = (w-x1, h-y1)

    o = np.subtract(y2, y1)
    q = np.subtract(x2, x1)
    slope = - q / o

    if content == 1:
        d = 0.1 * random.randint(0,50)
        alpha = 0 
    elif content == 2:
        d = 10
        alpha = 0.1 * random.randint(0, 60)
    
    a1=x1 + (d - length /2 * np.sin(alpha * np.pi / 180)) / np.sqrt(pow(slope ,2) + 1)
    b1=y1 + slope * (a1 - x1)

    a2=x2 + (d + length /2 * np.sin(alpha * np.pi / 180)) / np.sqrt(pow(slope ,2) + 1)
    b2=y2 + slope * (a1 - x1)


    cv2.line(image,(int(x1), int(y1)), (int(x2), int(y2)), (0, 225, 0), 1, cv2.LINE_AA)
    image=image
    cv2.line(image,(int(a1), int(b1)), (int(a2), int(b2)), (0, 225, 0), 1, cv2.LINE_AA)

    text1 = str(num_test)+"/500"
    text2 = "差がある → Type'Y'"
    text3 = "分からない、迷った → Type'N'"
    text4 = "戻る → Type'ESC'"
    image=cv2ImgAddText(image,text1 ,20,20, (0,0,0),20)
    image=cv2ImgAddText(image,text2 ,30,730, (0,0,0),15)
    image=cv2ImgAddText(image,text3 ,30,750, (0,0,0),15)
    image=cv2ImgAddText(image,text4 ,30,770, (0,0,0),15)

    return image,d,alpha

name = 'None'
while True:
    os.system('cls')
    if name == 'None' :
        name = str(input("please entry your name:"))
    print("Name:",name)
    print("1:distance experiment")
    print("2:angle experiment")
    print("3:end this program")
    content = int(input("please entry option:"))
    if content == 1:
        data = [['distance','YES_NO']]
        num_test=num_yes=num_no=0
        while num_test<500:
            image=np.zeros([800,800,3], np.uint8)+255
            img, d, alpha =random_line(image,num_test, content)
            d = round(d , 1)
            cv2.imshow('Discrimination ability experiment:distance', img)

            key = cv2.waitKey(0)
            if key == ord('y'):
                #print("yes")
                data.append([d,1])
                num_test += 1
                num_yes += 1

            if key == ord('n'):
                #print("no")
                data.append([d,0])
                num_test += 1
                num_no += 1

            if key == 27:
                print("End of program")
                cv2.destroyAllWindows()
                break

        output = open(name + '_data_distance.xls','w',encoding='gbk')
        for i in range(len(data)):
            for j in range(len(data[i])):
                output.write(str(data[i][j]))    
                output.write('\t')   
            output.write('\n')      
        output.close()

    elif content == 2:
        data = [['angle','YES_NO']]
        num_test=num_yes=num_no=0
        while num_test<500:
            image=np.zeros([800,800,3], np.uint8)+255
            img, d, alpha =random_line(image,num_test, content)
            alpha = round(alpha , 1)
            cv2.imshow('Discrimination ability experiment:angle', img)

            key = cv2.waitKey(0)
            if key == ord('y'):
                #print("yes")
                data.append([alpha,1])
                num_test += 1
                num_yes += 1

            if key == ord('n'):
                #print("no")
                data.append([alpha,0])
                num_test += 1
                num_no += 1

            if key == 27:
                print("End of program")
                cv2.destroyAllWindows()
                break

        output = open(name + '_data_angle.xls','w',encoding='gbk')
        for i in range(len(data)):
            for j in range(len(data[i])):
                output.write(str(data[i][j]))    
                output.write('\t')   
            output.write('\n')      
        output.close()
    elif content == 3:
        break
    else:
        print('please check your option!')

