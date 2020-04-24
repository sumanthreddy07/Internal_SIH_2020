import cv2

img1 = cv2.imread('awifs_ndvi_201712_15_1_clipped.tif', 0)
img2 = cv2.imread('awifs_ndvi_201712_15_2_clipped.tif', 0)

img_h1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2RGB)
img_h2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)

#for in i range()

x = -1.9
x1 = -1.9
x2 = -1.9

#print(img1[0][0])

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
                    elif(z < -0.1 and z >= -0.2):
                        img_h1[l][m] = (255,0,0)
                    elif(z < 0 and z >= 0.1):
                        img_h1[l][m] = (191,0,0)
                    elif(z < 0.1 and z >= 0):
                        img_h1[l][m] = (127,0,0)
                    elif(z < 0.2 and z >= 0.1):
                        img_h1[l][m] = (255,255,0)
                    elif(z < 0.3 and z >= 0.2):
                        img_h1[l][m] = (191,191,0)
                    elif(z < 0.4 and z >= 0.3):
                        img_h1[l][m] = (127,127,0)
                    elif(z < 0.5 and z >= 0.4):
                        img_h1[l][m] = (0,255,255)
                    elif(z < 0.6 and z >= 0.5):
                        img_h1[l][m] = (0,191,191)
                    elif(z < 0.7 and z >= 0.6):
                        img_h1[l][m] = (0,127,127)
                    elif(z < 0.8 and z >= 0.7):
                        img_h1[l][m] = (0,255,0)
                    elif(z < 0.9 and z >= 0.8):
                        img_h1[l][m] = (0,191,0)
                    elif(z < 1.0 and z >= 0.9):
                        img_h1[l][m] = (0,127,0)

            n = str('NDVI Extract/'+str(i)+'-'+str(j)+'-'+str(0)+'15.tif')
            cv2.imwrite(n, img_h1)
