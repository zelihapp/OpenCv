import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

'''
cv2.putText() fonksiyonu ekrana yazi yazdirmak icin kullanilir
cv2.putText(cizim yapacagimiz ekran, yazacagimiz metin, metnin baslayacagi koordinatlar,
yazi tipi(font), fontun büyüklügu, yazinin rengi, yazinin tipi)
yazinin tipi-> cv2.LINE_AA(varsayilan olarak)
'''

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX


cv2.putText(canvas, "OpenCV", (50, 50), font3, 2, (0, 0, 0),  )





cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()