import cv2
import pickle

img1 = cv2.imread('awifs_ndvi_201712_15_1_clipped.tif', 0)
img2 = cv2.imread('awifs_ndvi_201712_15_2_clipped.tif', 0)

img_h1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2RGB)
img_h2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)

#for in i range()

x = -1.9
x1 = -1.9
x2 = -1.9

rows, cols = (24, 13)
percent = [[0]*cols]*rows
percent_arr = [[0]*cols]*rows

size = 2118*2135

k = 0

for i in range(2017, 2019):
    for j in range(1,13):
            if(j <= 9):
                x = str('awifs_ndvi_'+ str(i) +'0'+ str(j) +'_15_'+ str(1) +'_clipped.tif')
                y = str('awifs_ndvi_'+ str(i) +'0'+ str(j) +'_15_'+ str(2) +'_clipped.tif')
            else:
                x = str('awifs_ndvi_'+ str(i) +''+ str(j) +'_15_'+ str(1) +'_clipped.tif')
                y = str('awifs_ndvi_'+ str(i) +''+ str(j) +'_15_'+ str(2) +'_clipped.tif')

            img1 = cv2.imread(x, 0)
            img2 = cv2.imread(y, 0)

            img_h1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2RGB)

            for l in range(0,2135):
                for m in range(0,2118):
                    # NDVI = (NRI - RED)/(NRI + RED)
                    x1 = int(img1[l][m]) - int(img2[l][m])
                    x2 = int(img1[l][m]) + int(img2[l][m])

                    if x2==0:
                        z = 0
                    else:
                        z = x1/x2

                    if(z < -0.2 and z >= -1.0):
                        img_h1[l][m] = (0,0,0)
                        percent[k][0] = percent[k][0] + 1
                    elif(z < -0.1 and z >= -0.2):
                        percent[k][1] = percent[k][1] + 1
                    elif(z < 0 and z >= 0.1):
                        percent[k][2] = percent[k][2] + 1
                    elif(z < 0.1 and z >= 0):
                        percent[k][3] = percent[k][3] + 1
                    elif(z < 0.2 and z >= 0.1):
                        percent[k][4] = percent[k][4] + 1
                    elif(z < 0.3 and z >= 0.2):
                        percent[k][5] = percent[k][5] + 1
                    elif(z < 0.4 and z >= 0.3):
                        percent[k][6] = percent[k][6] + 1
                    elif(z < 0.5 and z >= 0.4):
                        percent[k][7] = percent[k][7] + 1
                    elif(z < 0.6 and z >= 0.5):
                        percent[k][8] = percent[k][8] + 1
                    elif(z < 0.7 and z >= 0.6):
                        percent[k][9] = percent[k][9] + 1
                    elif(z < 0.8 and z >= 0.7):
                        percent[k][10] = percent[k][10] + 1
                    elif(z < 0.9 and z >= 0.8):
                        percent[k][11] = percent[k][11] + 1
                    elif(z < 1.0 and z >= 0.9):
                        percent[k][12] = percent[k][12] + 1

            for b in range(13):
                percent_arr[k][b] = (percent[k][b]/size)*100

            k = k + 1

with open('percent_arr_values.txt', 'wb') as fp:
    pickle.dump(percent_arr, fp)
