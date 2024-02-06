import cv2
import numpy as np

# resimleri birbiri uzerine ekleyip daha sonra agirliklarini yogunluklarini degistirerek bir resim kaybolacak digeri cikacak
# wow!!

def nothing(x):
    pass

img1 = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\alistirmalar2\\aircraft.jpg")
img1 = cv2.resize(img1,(640, 480))
img2 = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\alistirmalar2\\balls.jpg")
img2 = cv2.resize(img2, (640, 480))

# üst üste olusturacagimiz görüntü icin output degiskeni olusturulur
# addWeighted() -> resimlerin agirliklarini birbiri uzerine ekleme aslinda biri seffaf digeri daha baskin hale gelecek
# bu fonksiyon toplam 5 parametre alir. ilk iki parametre olarak ekleyecegimiz ilk resim ve bulmasini istedigimiz agirlik
# 3. ve 4. parametre olarak ikinci resim ve bulmasini istedigimiz agirlik (Agirliklarinin toplaminin 1 olmasi gerekiyor)
# son parametre de gama degeridir varsayilan olarak 0 girebiliriz

output = cv2.addWeighted(img1, 0.5,img2,0.5,0)

windowName = "Transition Program"
cv2.namedWindow(windowName)

cv2.createTrackbar("Alpha-Beta", windowName, 0, 1000, nothing)

while True:
    cv2.imshow(windowName,output)

    # trackbardaki degeri degistiririz
    # alpha ve beta degerleri 0 ile 1 arasinda degisiyor kizagin hareketini daha rahat gozlemlemek icin 1000e bölündü
    alpha = cv2.getTrackbarPos("Alpha-Beta", windowName)/1000
    beta = 1 - alpha  #alpha ve beta degerleri 0 ile 1 arasinda
    # her bir frame de output degisecek
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)


    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()



