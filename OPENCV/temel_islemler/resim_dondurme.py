import cv2
import numpy as np

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\arabam.jpg", 0)
height, width = img.shape[:2]

'''
getRotationMatrix2D() -> 2 boyutta bir rotasyon yon degistirme islemi uygulanir 
4 parametre alir ilki sutun sonra satir sonra  hangi yonde dondurmek istegimiz 
ve en sonda da olcek parametrelerini alir.  
'''
M = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
# yukseklik ve genislik degerlerini 2 ye bolmesinin nedeni  2 kat azaltmalarini(satir ve sutun sayisini) sagliyor

dst = cv2.warpAffine(img, M, (width, height))
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()





