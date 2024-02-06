import matplotlib.pyplot as plt 
import numpy as np 

path = "C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\introductionToMatplotlib\\coins.jpg"
# dosyayi okuyor
img = plt.imread(path)
# sayisal olaral dizey veriyorsa resmi okumustur -> print(img)

'''
# resmi görsel olarak görmek icin
plt.imshow(img)
plt.show()
'''

# resmin dizeyini ve tipini gormek icin:
print(img);print("type",type(img));print("shape: ",img.shape);print("ndim: ",img.ndim);print("size: ",img.size);print("dtype: ",img.dtype)

print("red channel: ",img[50,50,0])  # rgb -> r=0 , g = 1 , b=2
print("green channel: ",img[50,50,1])
print("blue channel: ",img[50,50,2])
# tum renkleri elde etmek icin ise: 
print("rgb channel value: ",img[50,50,:])



