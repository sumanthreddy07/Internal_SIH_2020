import cv2


# img1 = cv2.imread('2017-1-015')
per_y = [0] * 24
per_g = [0] * 24

k = 0

size = 2118*2135

for i in range(2017, 2019):
    for j in range(1,13):
        x = str(str(i)+'-'+str(j)+'-'+str(0)+'15.tif')

        img1 = cv2.imread(x)

        for l in range(0,2135):
            for m in range(0,2118):
                if(img1[l][m][2] == 0):
                    if(img1[l][m][0] != 0 and img1[l][m][1] != 0):
                        per_y[k] = per_y[k] + 1
                if(img1[l][m][0] == 0 and img1[l][m][2] == 0):
                    if(img1[l][m][1] != 0):
                        per_g[k] = per_g[k] + 1

        per_y[k] = (per_y[k] / size) * 100
        per_g[k] = (per_g[k] / size) * 100
        print('Percentage of Yellow @' + str(j) +'-'+ str(i) + ' : '+ str(per_y[k]))
        print('Percentage of Green  @' + str(j) +'-'+ str(i) + ' : '+ str(per_g[k]))
        k = k + 1

per_total = per_y + per_g
print('Percentage of Total:')
print(per_total)
