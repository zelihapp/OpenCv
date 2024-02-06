import cv2
import numpy as np

'''
np.zeros(): belli bir alana siyah bir tuval olusturur. fonksiyon icine girdigimiz parametrelerle belli
bir buyuklukte siyah bir alan olusturur. 
np.uint8 -> cizim yaptigimizda kullandigimiz veri tipidir.
'''


'''
canvas = np.zeros((512, 512, 3), dtype=np.uint8)
#"print(canvas)" tüm matrisler 0 elemanindan olusur (siyah tuval)--> bgr(0,0,0) ; beyaza cevirme-->bgr(255,255,255)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255      # beyaza cevrilir
#print(canvas)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()




