import cv2

'''
imread() : resimlerin matematiksel degerlerinin okur ve img degiskenine isler
iki parametre alir.ilki resmin adi uzantisi ile birlikte yazilir .
ikinci paremetre ise eger resmin olfugu gibi okunmasini istiyorsak girmeye
gerek kalmaz ama eger gri tonlarinda okunmasini istiyorsak bir *flag*
girilmesi gerekiyor -> cv2.IMREAD_GRAYSCALE yada 0.bir diger okuma yöntemi ise -> 
impread("C:\(u)sers\zelih\OneDrive\Masaüstü\yildizligece.jpg")
kaydetmek icin de (imwrite) yine dosya uzantisi kullanilabilir. türkce karakter icermemelidir
'''


img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\resim_okuma_gosterme_kaydetme\\yildizligece.jpg")
# print(img)
'''
namedWindow(): acilan resim penceresinin boyutlandirmak icin kullanilir iki arguman alir ilki 
resmin gosterilecegi pencere ikincisi ise boyutlandirilabilir oldugunu gosteren flag degeri
cv2.WINDOW_NORMAL
'''

cv2.resize(img, (540, 480))
'''
cv2.resize: resmi istedigimiz boyutlara getirebiliriz.
ilk parametre resmi tutan degisken ikinci parametre ise resmin boyutlari
eger bu fonksiyon icinde boyutlandirmak yapmak istiyorsak namedWindow fonksiyonu icindeki 
WINDOW_NORMAL parametresi silinmelidir.
'''
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)


'''
imshow(): icine iki argüman alir . ilki resmin gösterilecegi pencerenin adi
        ikincisi de resmin tututldugu degiskenin adi
'''
cv2.imshow("Image",img)

'''
imwrite():resmin kaydedilmesini saglar.
'''
cv2.imwrite("yildizligece1.jpg",img)
cv2.waitKey(0)
'''
waitKey():resim fonksiyonun icine koyulan deger kadar ekranda tutulur (ms) 
0 girilirse pencere kapanana kadar ekranda tutulur
'''

cv2.destroyAllWindows()
'''
destroyAllWindows():acik olan tüm pencereleri kapatir
'''















