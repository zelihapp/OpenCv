import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

'''
cizecegimiz geometrik seklin parametrelerini fonksiyona veririz 
ilk parametre resmin cizelecegi tuval(canvas) olur
ikinci baslangic noktasi girilmelidir daha sonra bitis noktasi girilir
sonra rengi girilir (bgr) ve son olarak kalinligi(thickness) parametre olarak verilir
'''
cv2.line(canvas, (50, 50), (512, 512), (255, 0, 0), thickness=5)
cv2.line(canvas, (100, 50), (200, 512), (0, 0, 255), thickness=7)

'''
cv2.rectangle() fonksiyonu dikdortgen cizmek icin kullanilir
baslangic noktasi -> sol ust kose , bitis noktasi-> sag alt kose
kalinlik parametresine "-1" degerini verirsek ici dolu bir dikdortgen elde edilir
'''

cv2.rectangle(canvas, (20, 20), (100, 100), (0, 255, 0), thickness=3)
cv2.rectangle(canvas, (150, 150), (200, 200), (0, 0, 255), thickness=-1)


'''
cv2.circle() fonksiyonu cember cizmek icin kullanilir
oncelikle cemberin merkez noktasini daha sonra da cemberin yaricapi 
parametreleri verilir
'''

cv2.circle(canvas, (250, 250), 100, (25, 200, 100), thickness=5)
#cv2.circle(canvas, (250, 250), 100, (255, 200, 100), thickness=-1)

'''
cv2 kutuphanesi ücgen cizmek icin özel bir fonksiyon saglamiyor bunun yerine 
ucgenin 3 tane noktanin koordinatini kullanarak cizebiliriz
'''
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)

cv2.line(canvas, p1, p2, (0, 0, 0), thickness=7)
cv2.line(canvas, p2, p3, (0, 0, 0), thickness=7)
cv2.line(canvas, p3, p1, (0, 0, 0), thickness=7)

'''
cv2.rectangle ile nasil yamuk yada besgen olusturulabilir (duzgun olmayanlar)
bu durumda cv2.polylines() fonksiyonu kullanilir
polylines fonksiyonunun calisma ilkesine gore ilk once bir numpy dizisi olusturulur
3.parametreye olusturulacak seklin kapali olmasini istiyorsak "True" degerinin acik olmasini
istiyorsak da "False" degerini gireriz.true girersek sekil otomatikmen kapanir
'''

points = np.array([[110, 200], [330, 200], [290, 220], [100, 150]], np.int32)
cv2.polylines(canvas, [points], True,(0, 0, 100), thickness=5)

'''
cv2.ellipse(canvas, merkez, (genislik,yukseklik), (elipsin yatay eksenle yapacagi aci),
(baslangic derecesini ve bitis derecesi girilir 90-360)
'''
cv2.ellipse(canvas, (300, 300), (80, 20), 10, 90, 360, (255, 255, 0,), thickness=-1)
cv2.ellipse(canvas, (200, 200), (100, 50), 0, 0, 360, (255, 255, 0,), thickness=-1)


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()