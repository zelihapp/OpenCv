import cv2
import numpy as np

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\arabam.jpg",0)

#erode metodu 4 parametre alir -> erozyona ugrayacak olan resmin adi , kernel(matris girilecek(?)), iterasyon degeri
# iterasyon matris dizeyinin resim uzerinde kac defa tekrar ettigini gosteriyor
kernel = np.ones((10, 10), np.uint8)
# erosion = cv2.erode(img, kernel, iterations = 1)
#cv2.imshow("erosion", erosion)


# dilate metodu resim üzerinde kalinlastirma yapar
#dilation = cv2.dilate(img, kernel, iterations = 5)
#cv2.imshow("dilation", dilation)

#opening resmin uzerindeki gürültüyü, bozulmayi kaldirir
#opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#cv2.imshow("opening", opening)

#closing resmin uzerindeki uyumsuzluklari gidermeye calisir
#closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#cv2.imshow("closing", closing)

#gradient resmin en dis kismini cizer geri kalan yerleri ise siyah olarak birakir
#gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
#cv2.imshow("gradient", gradient)

#tophat resmin dis kismini beyaz cizgilerle cizer kalan ic kisimlarin hepsini de siyah olarak birakir
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("img", img)
cv2.imshow("tophat", tophat)






cv2.waitKey(0)
cv2.destroyAllWindows()


