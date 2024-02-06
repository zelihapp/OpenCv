'''
 ilk olarak kullanacagimiz resmi griye ceviririz
 gri tona cevrilen resmin koselerini yumusatmamiz gerekiyor (bilateralFilter)
 plakanin sinir cizgilerini yakalamayi amacliyoruz dolayisiyla ihtiyacimiz olmayan sinir cizgilerini resimden atmamiz gerekiyor
 daha sonra elimizdeki resme Canny() fonksiyonunu uyguluyoruz ve resimdeki koseleri tespit ediyoruz
 resme findContours() uygulanarak plakanin contourlari elde edilir
 tespit edilen plakayi maske uygulayip kirpiyoruz en sonunda elimizde kalan görüntuyu pytesseract islemine tabii tutariz
 ** plaka disindaki her seyi gürültü olarak kabul ederiz ve onlari adim adim yok atmeye calisiriz
 ** resmi yumusatmadan direkt canny fonksiyonu uygularsak cok daha fazla ayrinti icerir o yuzden ilk yumusatilmali
 cv2.contourArea() ve reverse -> koordinatlari alanlarina gore ters cevirip siralama yapar 

'''

import cv2
import numpy as np 
import pytesseract
import imutils

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\licence_plate_detection\\licence_plate.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filtered = cv2.bilateralFilter(gray, 6, 250, 250)

edged = cv2.Canny(filtered, 30, 200)

contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print("kontur: ", contours)

cnts = imutils.grab_contours(contours)
#print("imutils.grab_contours: ", cnts)
cnts = sorted(cnts, key=cv2.contourArea,reverse=True)[:10]
#print("sorted: ", cnts)

screen = None


for c in cnts:
    epsilon = 0.018*cv2.arcLength(c,True)   # yay uzunlugunu bulur (true bosluk yoksa devam et )
    approx = cv2.approxPolyDP(c,epsilon,True)

    if len(approx) == 4:    # yani 4 kose tespit edilmisse bu bir dikdortgendir
        screen = approx
        break
 
# algilanan bölgeye mask uygulanir

mask = np.zeros(gray.shape, np.uint8)
cv2.imshow("gray",gray)
# cv2.imshow("mask",mask)  # her yer siyah ile kaplanacak sadece plakanin oldugu bölge verilen koordinatlar haric

# cv2.drawContours() fonks. ile plaka bölgesini beyaza cevirecez

new_img = cv2.drawContours(mask, [screen], 0, (255,255,255), -1)
cv2.imshow("mask",mask)

# plaka bölgesindeki yazi kontur alanina yapistirilir

new_img = cv2.bitwise_and(img,img,mask = mask)
# cv2.imshow("mask",new_img)

#resmin kirpilmasi gerekiyor öncelikle (x ve y) iki degisken olusturuyoruz. bunlar beyaz olan bölgenin koordinatlarini icinde tutar

(x,y) = np.where(mask == 255)

# en büyük x ve en büyük y koordinatini tutar
(topx,topy) = (np.min(x), np.min(y))
(bottomx,bottomy) = (np.max(x), np.max(y))

cropped = gray[topx: bottomx + 1, topy: bottomy + 1]
#cv2.imshow("gray",cropped)

text = pytesseract.image_to_string(cropped, lang="eng")
print("Detected Text: ",text)


'''
cv2.imshow("1.Original",img)
cv2.imshow("2.Gray",gray)
cv2.imshow("3.filtered",filtered)
cv2.imshow("3.edged",edged)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()