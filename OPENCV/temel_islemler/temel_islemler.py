import cv2
import numpy as np

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\temel_islemler\\robot.jpeg")

'''
cv2.resize(img, (1200, 1260))
dimension = img.shape                   # resmin boyutlarini gosterir
print(dimension)

color = img[150, 200]                   #150ye200 pikselindeki renk degerine (b,g,r) ulasilir
print(color)
'''
color = img[150, 200]                   #150ye200 pikselindeki renk degerine (b,g,r) ulasilir
print("BGR: ", color)


blue = img[150, 200, 0]
print("blue: ", blue)

green = img[150, 200, 1]
print("green: ", green)

red = img[150, 200, 2]
print("red: ", red)

#mavi degerini degistirmek istersek
img[150, 200, 0] = 250
print("New Blue: ", img[150, 200, 0])

blue1 = img.item(150, 200, 0)
print("blue1: ", blue1)
img.itemset((150, 200, 0), 172)
print("New blue1: ", img[150, 200, 0])




cv2.imshow("Tablo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()