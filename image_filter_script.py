import numpy as numpy
import cv2


for i in range(2017, 2019):

    for j in range(1,13):
        
        for k in range(1,3):

            if(j<=9):
                x = str('awifs_ndvi_'+ str(i) +'0'+ str(j) +'_15_'+ str(k) +'_clipped.tif')
                img = cv2.imread(x, 0)
                color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

                for l in range(0,2135):
                    for m in range(0,2118):

                        if(color_img[l][m][1] < 80  and color_img[l][m][1] > 60):
                            
                            color_img[l][m][1] = 255
                            color_img[l][m][0] = 0
                            color_img[l][m][2] = 0


                y = str('green_filter/'+str(i)+'-'+str(j)+'-'+str(k)+'15.tif')
                cv2.imwrite(y , color_img)        
                     

            else:
                x = str('awifs_ndvi_'+ str(i) +''+ str(j) +'_15_'+ str(k) +'_clipped.tif')
                img = cv2.imread(x, 0)
                color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

                for l in range(0,2135):
                    for m in range(0,2118):
    
                        if(color_img[l][m][1] < 80  and color_img[l][m][1] > 60):
                            
                            color_img[l][m][1] = 255
                            color_img[l][m][0] = 0
                            color_img[l][m][2] = 0

                y = str('green_filter/'+str(i)+'-'+str(j)+'-'+str(k)+'15.tif')
                cv2.imwrite(y, color_img)                




                
                            




