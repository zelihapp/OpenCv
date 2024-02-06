import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\introductionToMatplotlib\\smile.jpg"
img = plt.imread(path)
print(img)

# min() -> resmin piksellerinde sahip oldufu en kucuk degeri hesaplar (rgb renk bir tanesi siyah ya da beyaz olabilir)
print("min value: ",img.min())
# max() -> resmin piksellerinde sahip oldufu en buyuk degeri hesaplar 
print("max value: ", img.max())
# mean -> tum renk degerlerinin ortalamasini hesaplar
print("mean: ", img.mean())
# median() -> rgb degerlerinin medyanini hesaplayabiliriz 
print("median: ",np.median(img))
# average() -> tum renk degerlerinin ortalamasini hesaplar
print("average: ",np.average(img))
print("mean1: ",np.mean(img))