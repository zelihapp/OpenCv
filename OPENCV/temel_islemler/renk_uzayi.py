import cv2

img_bgr = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\robot.jpeg")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

'''
#bgr'dan rgb'ya cevirme
cvtColor(kaynak resim, donusumu yapan deger(flag girilir)

'''

cv2.imshow("Robot BGR", img_bgr)    # goruntu su an bgr formatinda
cv2.imshow("Robot RGB", img_rgb)   # goruntu su an rgb formatinda
cv2.imshow("Robot HSV", img_hsv)
cv2.imshow("Robot Gray", img_gray)


cv2.waitKey(0)
cv2.destroyAllWindows()
