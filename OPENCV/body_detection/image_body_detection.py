import cv2

# Kullanacağımız resmi çalışmamıza dahil edelim
img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\body_detection\\body.jpg")

# Kullanacağımız cascade dosyalarını çalışmamıza dahil edelim.
body_cascade = cv2.CascadeClassifier("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\body_detection\\haarcascade_fullbody.xml")

# Haar-like özellikleri kolay algılayabilmek için resmi boz(gri) tonlara çevirelim.
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

#  Şimdi de cascade dosyamızı kullanarak her bir kare üzerindeki yüzlerin koordinarlarını bulalım.
bodies = body_cascade.detectMultiScale(gray, 1.1, 2)

#  "bodies" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
for x,y,w,h in bodies:
    cv2.rectangle(img, (x,y), (x+w, y+h),(0,0,255), 3)

# İşlediğimiz kareleri görelim.
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cascade özellikleri her zaman dogru calismaz 
