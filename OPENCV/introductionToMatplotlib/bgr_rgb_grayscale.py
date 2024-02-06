import numpy as np 
import matplotlib.pyplot as plt 
import cv2

path = "C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\introductionToMatplotlib\\smile.jpg"
img = cv2.imread(path,1)    # BGR 

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)      # RGB
plt.show()

# cv2 kutuphanesi ile bir resmi okudugumuzda BGR formatinda okur . plt.imshow() ile okudugumuzda ise RGB seklinde okur
# eger cv2.imread() ile okuduysak resmin formatini donusturmemiz gerekiyor (bgr->rgb)

'''
# resmi gri olarak gormek istiyorsak
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cmap color map kisaltilmis hali
# renk haritasinin gri bicimde olacagini soyluyoruz ama yeterli olmuyor resmin onceki halinde rgb olmadigi icin sikinti cikiyor 
# buna ek olarak interpolation uygulanmasi gerekiyor
plt.imshow(img,cmap="gray",interpolation="BICUBIC")

# griye cevirmenin daha kisa yolu:
# img = cv2.imread(path,1) # 1 yerine 0 yazilirsa direkt grayscale modda aliyor
'''


