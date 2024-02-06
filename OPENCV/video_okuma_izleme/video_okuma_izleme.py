import cv2
'''
VideoCapture():icine aldigi argumanlara gore videoyu webcam uzerinden mi yoksa bilgisayarda
hazirda olan vir dosya uzerinden mi okuyacagini belirler. eger arguman 0 ise webcam uzerinden
okunur. ya da adres ile
'''
# video dosyasi

cap = cv2.VideoCapture("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\video_okuma_izleme\\1.mp4")

# webcam: cap = cv2.VideoCapture(0)

'''
read(): videoda yakalanan kareleri tek tek okumak icin kullanilir.iki tane deger dondürür
videolar dogru okunmussa True yanlis okuduysa False, (eger read dogru okumussa frame'leri ret true yanlis ise false) 
**frameler ekranda ne kadar uzun kalirsa görüntü kalitesi de o kadar dusuk olur
**cv2.waitKey(0)-> tek bir frame gorunur
'''
while True:
    ret, frame = cap.read()
    if ret==0:
        break
    frame = cv2.flip(frame, 1)
    cv2.imshow("window", frame)
    if cv2.waitKey(50) & 0xFF == ord("q"):
        break
cap.release()

'''
0xFF == ord("q")->klavyeden girilen harfi ile donguden cikar. ord() fonksiyonu ile klavye baglantili olur
cap.release():video dosyasi uzerine baska islemler yapilacagindan while da yapilan islem cap.release ile kapatilir
kapatilmazsa baska islem yapilmasina izin vermez
'''

cv2.destroyAllWindows()

'''
cv2.flip():webcamden alinan goruntuler bazen ters bir sekilde görünebilir
aldigimiz her bir frame ters cevrilir ve istedigimiz eksenlere göre yansitir
2 argüman alir ilki yonunu degistirmek istedigimiz degisken:frame
ikincisi de hangi yönde degistirmek istedigimizdir eger 1 yazarsak y eksenine gore
yansitilir . 
'''