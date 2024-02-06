import cv2   

# Kullanacağımız videoyu çalışmamıza dahil edelim.
vid = cv2.VideoCapture("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\body_detection\\body.mp4")

# Kullanacağımız cascade dosyalarını çalışmamıza dahil edelim.
body_cascade = cv2.CascadeClassifier("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\body_detection\\haarcascade_fullbody.xml")

# Sonsuz bir döngü ile her kareyi(frame) tek tek inceleyelim.
while 1:
    # Her kareyi tek tek okuyalım.
    ret, frame = vid.read()
    
    # Haar-like özellikleri kolay algılayabilmek için her bir kareyi boz(gri) tonlara çevirelim.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Şimdi de cascade dosyamızı kullanarak her bir kare üzerindeki yüzlerin koordinarlarını bulalım.
    bodies = body_cascade.detectMultiScale(gray)

    # "bodies" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

         
    # İşlediğimiz kareleri görelim.
    cv2.imshow('video',frame)

    # Programı kapatacak kodu yazalım.
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Son olarak videoyu serbest bırakalım.
vid.release()
cv2.destroyAllWindows()

# haar cascadeler insan bedeni bulmada algilamada cok basarili degildirler