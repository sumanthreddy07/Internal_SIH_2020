import numpy as numpy
import cv2

img = cv2.imread('awifs_ndvi_201701_15_1_clipped.tif', 0)


color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)



#


for i in range(0,2135):
    for j in range(0,2118):

            if(color_img[i][j][1] < 80  and color_img[i][j][1] > 60):
            
                color_img[i][j][1] = 255
                color_img[i][j][0] = 0
                color_img[i][j][2] = 0

cv2.imwrite('imafgase.tif', color_img);           
                            




