import cv2
import numpy as np

'''
roi -> region of interest -> ilgi alani
bir resimde bir kisinin gozlerinin acik olup olmadigini ogrenmek istiyorsak tum
bir resmi islemektense kisinin gozlerinin resimden ayiririz ve sadece o kismi isleme
aliriz bu sekilde daha kisa, kolay ve yuksek dogrulukta  sekilde islemleri yapmis oluruz.
'''

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\robot.jpeg")
cv2.imshow("Lost in Space", img)
#print(img.shape[:2]) -> boyut ogrenme

roi = img[0:400, 550:900]
cv2.imshow("ROI", roi)


cv2.waitKey(0)
cv2.destroyAllWindows()

