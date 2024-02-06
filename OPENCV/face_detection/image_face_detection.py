import cv2

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\face_detection\\face.png")

face_cascade = cv2.CascadeClassifier("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\face_detection\\haarcascade_frontalface_default.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detectMultiScale() -> bu fonksiyon bize resmin üzerindeki yüzlerin bulundugu koordinatlari verir
# 3 parametre alir ilk resim , ikincisi ise ölceklendirme degeri resmin kac oraninda kücültülecegi bilgisini verir
# son parametre de belirli bir bölgede kac farkli pencerenin yüz bulmasini istedigimizi yazariz
# bu koordinatlari bir degisken icinde saklariz (faces)

faces = face_cascade.detectMultiScale(gray, 1.3, 7)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)    # detectMultiScale() fonksiyonu ile x ve y koord. bulunur bunlara eklenerek genislik ve yukseklik elde edilir

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()