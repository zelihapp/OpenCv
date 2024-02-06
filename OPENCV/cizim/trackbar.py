import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.namedWindow("image")

'''
cv2.createTrackbar("kizagin adi", "kizagin yerlesecegi pencerenin adi", "baslangic degeri","bitis degeri)
nothing fonksiyonunu eklememizin nedeni trackbar'in calisma sekli ile ilgilidir hatasiz calismasini saglar
** ve bir anahtar olusturmaliyiz
'''

cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

switch = "0: OFF, 1: ON"
cv2.createTrackbar("switch", "image", 0, 1, nothing)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")


    if s == 0:
        img[:] = (0, 0, 0)
    if s == 1:
        img[:] = [b, g, r]

    # aldigimiz degerleri degiskenlerin icinde (r,g,b) tutariz daha sonra pencereye dondeririz
    # anahtar kapali iken her hangi bir degisim yok acik iken renkler pencereye aktarilir
    
cv2.waitKey(15)
cv2.destroyAllWindows()

