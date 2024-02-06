import cv2
import numpy as np

'''
resimlerin uzerindeki gurultuleri pürüzleri azaltmayi amacliyoruz
resimleri daha yumusak hale getirmeye calisiriz
'''
'''
blur(degisken, resmin yumusama degeri(?), )
'''
'''
GaussianBlur() metodunda en son parametre olarak sinir cizgileri ile ilgili bir deger girmemiz beklenir
cv2.BORDER_DEFAULT -> varsayilan olarak ayarlandi 
'''
img_filter = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\filter.png")
img_median = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\median.png")
img_bilateral = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\bilateral.png")


blur = cv2.blur(img_filter, (7, 7))     # ksize parametresinde sadece pozitif tek sayilar olmaliymis
blur_g = cv2.GaussianBlur(img_filter, (9, 9), cv2.BORDER_DEFAULT)
blur_m = cv2.medianBlur(img_median, 7)
blur_b = cv2.bilateralFilter(img_bilateral, 9, 95, 95)

cv2.imshow("Original", img_median)
cv2.imshow("Blur", blur)
cv2.imshow("blur_g", blur_g)
cv2.imshow("blur_m", blur_m)
cv2.imshow("original", img_bilateral)
cv2.imshow("blur_b", blur_b)


cv2.waitKey(0)
cv2.destroyAllWindows()
