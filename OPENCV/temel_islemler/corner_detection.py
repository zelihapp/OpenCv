import cv2
import numpy as np

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\text.png")
img1 = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\contour.jpg")

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


# goodFeaturesToTrack() goruntudeki koseleri saptar .  bu fonksiyon 4 parametre alir
# (gray , maksimum kose sayisi , kalite degeri , minimum kose arasi mesafe )

#gray direkt calismaz once float32 tipine cevrilmesi gerekiyor
gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(gray, 200, 0.01, 10)

corners = np.intp(corners)   # bunu yapmamizin nedeni cemberler cizerken float sayilar kullanilmaz int olmasi gerekli

for corner in corners:
    x, y = corner.ravel()  #x,y degerlerini alabilmek icin cornersi tek bir satir haline getirmek gerekiyor
    cv2.circle(img1, (x, y), 3, (0, 0, 255), -1)

cv2.imshow("corner",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
