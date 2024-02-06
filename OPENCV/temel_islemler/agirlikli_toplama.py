# f(x, y) = x*a + y*b + c

import cv2
import numpy as np

circle = np.zeros((512, 512, 3), np.uint8) + 255   # beyaz tuval olusturulur
cv2.circle(circle, (256, 256), 60, (255, 0, 0), thickness=-1)

rectangle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rectangle, (150, 150), (350, 350), (0, 0, 155), thickness=-1)

'''
dst->resmin en son hali 
cv2.Weighted(ilk resim, ilk resmi yuzde kac ikinci resme aktardigimiz olacak, ikinci resim, ikinci resmi ilk resme yuzde kac
eklenir, ve sabit sayi)
eklenen yuzdelir toplami 100 olmali
'''

dst = cv2.addWeighted(circle, 0.3, rectangle, 0.7, 0)


cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()