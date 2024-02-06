import cv2

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\alistirmalar2\\starwars.jpg")
blurry_img = cv2.medianBlur(img, 7)

# laplacian() fonksiyonu bir resmin bulanik olup olmadigini saptamaya yarar
# ilk parametre olarak blurlu olan resim girilir , ikinci parametre varsayilan olarak girilir bir deger dondurulur

laplacian = cv2.Laplacian(blurry_img, cv2.CV_64F).var()

if laplacian < 500:
    print("Blurry Image")





cv2.imshow("img", img)
cv2.imshow("blurry_img", blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
