import cv2
import numpy as np

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\arabam.jpg",0)  # 0 flagi girdigimiz icin resim siyah beyaz olur

#" row, col = img.shape ile hata verdi index eklenince calisti"  //-ilginc

height, width = img.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 20]])

'''
warpAffine()
resmi istedigimiz kadar kaydirmayi saglar
'''
dst = cv2.warpAffine(img, M, (width, height))

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()