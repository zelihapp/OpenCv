import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.zeros((500, 500), np.uint8) + 50 #500'e 500luk bir siyah ekran olusturulur

cv2.rectangle(img, (0, 60), (200, 150), (255, 255, 255), -1)
cv2.rectangle(img, (250, 170), (350, 200), (255, 255, 255), -1)


cv2.imshow("img", img)



#hist fonksiyonu sayesinde histogrami cizip show fonksiyonu ile gorebiliyoruz
#plt.hist 3 parametre alir (img,ravel() , 256 (kac deger oldugu) , (deger araligi) )
#img.ravel -> resmin tum piksellerini alip tek bir satira dokuyor


plt.hist(img.ravel(),256, [0, 256])
plt.show()
# olusan histogram 250000e kadar gidiyor (500x500) toplam piksel sayisi, ve dogru seklinde yukariya dogru ilerlemesinin
# tek nedeni tek bir renk olmasi (siyah -> 0 )
cv2.waitKey(0)
cv2.destroyAllWindows()