import cv2
# Kullanacağımız videoyu çalışmamıza dahil edelim
# Kullanacağımız cascade dosyalarını çalışmamıza dahil edelim.
face_cascade = cv2.CascadeClassifier("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\eye_detection\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\eye_detection\\haarcascade_eye.xml")
vid = cv2.VideoCapture("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\eye_detection\\eye.mp4")


# Sonsuz bir döngü ile her kareyi(frame) tek tek inceleyelim.
while 1:
    # Her kareyi tek tek okuyalım.
    ret,frame = vid.read()
    frame = cv2.resize(frame, (480,360))

    # Haar-like özellikleri kolay algılayabilmek için her bir kareyi boz(gri) tonlara çevirelim.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Şimdi de cascade dosyamızı kullanarak her bir kare üzerindeki yüzlerin koordinarlarını bulalım.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # "faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w , y+h), (255,0,0), 3)

        # Şimdi de, bulduğum yüzler içinde göz arayacağım.
        roi_frame = frame[y:y+h , x:x+w]
        roi_gray = gray[y:y+h , x:x+w]

        #eye cascade dosyasını kullanarak gözlerin koordinatlarını bulalım.
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # bu koordinatlara dikdörtgen çizelim.
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_frame, (ex,ey), (ex+ew , ey+eh), (0,0,255), 2)

    # İşlediğimiz kareleri görelim.
    cv2.imshow("video", frame)

    # programi kapatacak kodu yazalim
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Son olarak videoyu serbest bırakalım.
vid.release()
cv2.destroyAllWindows()