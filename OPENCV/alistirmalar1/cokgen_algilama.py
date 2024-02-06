import cv2
import numpy as np

# font metodunu kullanarak resim ve videolarin uzerine metin yazabiliriz
font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX  # opencv fonts

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\alistirmalar1\\polygons.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold fonksiyonu tek bir deger dondurmedigi icin basina "_" koyuyoruz
_,threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    # şekillerin konturları arasındaki mesafenin belirtilen hassasiyete eşit veya
    # belirtilen hassasiyetten daha az olacak şekilde daha az sayıda köşeden oluşan
    # başka bir şekle yaklaştırılması işleminde kullanilan metot

    cv2.drawContours(img,[approx],0,0,5)

    # tum sütunlari yani dik siralari satirlara döker
    x = approx.ravel()[0]   # 0.indexteki deger x'i temsil eder
    y = approx.ravel()[1]  # 1.indexteki deger y'yi temsil eder

    #print(len(approx))    # tüm cokgenlerin koordinat degerlerini tutar

    if len(approx) == 3:
        cv2.putText(img,"Triangle",(x,y),font1,1, (0))
    elif len(approx) == 4:
        cv2.putText(img,"Rectangle",(x,y),font,1, (0))
    elif len(approx) == 5:
        cv2.putText(img,"Pentagon",(x,y),font1,1, (0))
    elif len(approx) == 6:
        cv2.putText(img,"Hexagon",(x,y),font,1, (0))
    else:
        cv2.putText(img,"Ellipse",(x,y),font,1, (0))


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




