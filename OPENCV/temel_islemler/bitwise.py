import cv2
import numpy as np

img1 = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\bitwise_1.png")
img2 = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\bitwise_2.png")
'''
bitwise_and()-> bit duzeyinde and(ve) islemlerini gerceklestirir , img2 ve img1 'i karsilastiracaz
bitwise_or()-> bit duzeyinde or(veya) islemlerini gerceklestirir , img2 ve img1 'i karsilastiracaz
bitwise_and()-> bit duzeyinde ve islemlerini gerceklestirir , img2 ve img1 'i karsilastiracaz
'''
#bit_and = cv2.bitwise_and(img2, img1)
#bit_or = cv2.bitwise_or(img2, img1)
#bit_xor = cv2.bitwise_xor(img2, img1)
bit_not = cv2.bitwise_not(img2)
bit_not2 = cv2.bitwise_not(img1)





cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
#cv2.imshow("bit_and", bit_and)
#cv2.imshow("bit_or", bit_or)
#cv2.imshow("bit_xor", bit_xor)
cv2.imshow("bit_not", bit_not)
cv2.imshow("bit_not2", bit_not)




cv2.waitKey(0)
cv2.destroyAllWindows()

'''
"AND"
siyah bolgenin degeri 0 beyaz bolgenin degeri 1'dir.
ve baglacinda ; img1(0) + img2(1) -> bit de o bolge "0" yani siyaha boyanir
img1(1) + img2(0) -> bit de o bolge "0" yani siyaha boyanir 
ucgen icin; img1(1) + img2(1) -> bit de o bolge "1" yani beyaza boyanir

"OR"
veya baglacinda ; img1(0) + img2(1) -> bit de o bolge "1" yani beyaza boyanir
img1(1) + img2(0) -> bit de o bolge "1" yani beyaza boyanir 
ucgen icin; img1(1) + img2(1) -> bit de o bolge "1" yani beyaza boyanir
aradaki siyah cizginin nedeni resimlerin siyah ve beyaz bolumlerinin boyutlarinin tam olarak
ayni olmamasi tam cizginin oldugu yerde siyah kisimlar ust ust geliyor ve siyah cizgi olusur

"XOR"
xor baglacinda; 
img1(0) + img2(1) -> bit de o bolge "1" yani beyaza boyanir
img1(1) + img2(0) -> bit de o bolge "1" yani beyaza boyanir
ucgen icin; img1(1) + img2(1) -> bit de o bolge "0" yani siyaha boyanir
aradaki siyah cizginin nedeni resimlerin siyah ve beyaz bolumlerinin boyutlarinin tam olarak
ayni olmamasi tam cizginin oldugu yerde siyah kisimlar ust ust geliyor ve siyah cizgi olusur

"NOT"
her iki resmin de beyaz kisimlarini siyaha , siyah kisimlarini da beyaza boyar 
degili , tumleyeni iste

'''
