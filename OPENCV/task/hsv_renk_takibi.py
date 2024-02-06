import cv2
import numpy as np 

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\task\\color.jpg")
cv2.resize(img,(480,300))

def nothing(z):
    pass

# opencv fotograflari BGR olarak okur
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# trackbarlari olusturacagimiz pencere 
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,480)
# HSV -> Hue Saturation Value
cv2.createTrackbar("H Min","Trackbars",0,179,nothing)
cv2.createTrackbar("H Max","Trackbars",179,179,nothing)
cv2.createTrackbar("S Min","Trackbars",0,255,nothing)
cv2.createTrackbar("S Max","Trackbars",255,255,nothing)
cv2.createTrackbar("V Min","Trackbars",0,255,nothing)
cv2.createTrackbar("V Max","Trackbars",255,255,nothing)


while True:
    h_min = cv2.getTrackbarPos("H Min","Trackbars")
    h_max = cv2.getTrackbarPos("H Max","Trackbars")
    s_min = cv2.getTrackbarPos("S Min","Trackbars")
    s_max = cv2.getTrackbarPos("S Max","Trackbars")
    v_min = cv2.getTrackbarPos("V Min","Trackbars")
    v_max = cv2.getTrackbarPos("V Max","Trackbars")
    # bu degerler kullanilarak alt ve ust sinirlar belirlenir
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    # maskeleme islemi yapilir
    # lower ve upper degerleri hsv degerleri olacak o yuzden once hsvye cevirmemiz gerekiyor
    mask = cv2.inRange(img_hsv,lower,upper)
    # bitwise_and() -> aldigi iki fotografi birlestiriyor
    result = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("image",img)
    cv2.imshow("result",result)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# sari icin renk degerleri -> 22 63 43 255 0 255
# mor icin renk degerleri -> 52 148 146 187 85 157
'''