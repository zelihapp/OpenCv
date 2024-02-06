import cv2
import numpy as np 
from collections import deque
# deque fonksiyonu sayesinde bir listeleme islemi yapilir

cap = cv2.VideoCapture(0)
# aldigimiz noktalari hsv formatina donusturup mask islemi yapilir
lower_blue= np.array([100,60,60])
upper_blue= np.array([140,255,255])
# farkle renklerde olan noktalarin saklandigi degiskenler :
blue_points = [deque(maxlen=512)]
green_points = [deque(maxlen=512)]
red_points = [deque(maxlen=512)]
yellow_points = [deque(maxlen=512)]

blue_index=0
green_index=0
red_index=0
yellow_index=0
# colors renk degerlerini tutar
colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
color_index = 0
# paintWindow:cizim yapilacak pencere 'bir beyaz ekrana her sey cizilebilir'
# ekran beyaz ???
paintWindow = np.zeros((471,636,3))+255
#1) temizleme dugmesi
paintWindow = cv2.rectangle(paintWindow,(40,1),(140,65),(0,0,0),2)
#2) mavi dugme
paintWindow = cv2.rectangle(paintWindow,(160,1),(255,65),colors[0],-1)
#3) yesil dugme
paintWindow = cv2.rectangle(paintWindow,(275,1),(370,65),colors[1],-1)
#4)kirmizi dugme
paintWindow = cv2.rectangle(paintWindow,(390,1),(485,65),colors[2],-1)
#5) sari dugme
paintWindow = cv2.rectangle(paintWindow,(505,1),(600,65),colors[3],-1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(paintWindow,"CLEAR ALL",(49,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
cv2.putText(paintWindow,"BLUE",(185,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintWindow,"GREEN",(298,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintWindow,"RED",(420,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintWindow,"YELLOW",(520,33),font,0.5,(255,255,255),2,cv2.LINE_AA)

cv2.namedWindow("Paint")


while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    # cizim yapacagimiz nesneyi hsv formatina ceviriyoruz (mavi silgi)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    frame = cv2.rectangle(frame,(40,1),(140,65),(0,0,0),2)
    frame = cv2.rectangle(frame,(160,1),(255,65),colors[0],-1)
    frame = cv2.rectangle(frame,(275,1),(370,65),colors[1],-1)
    frame = cv2.rectangle(frame,(390,1),(485,65),colors[2],-1)
    frame = cv2.rectangle(frame,(505,1),(600,65),colors[3],-1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,"CLEAR ALL",(49,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(frame,"BLUE",(185,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"GREEN",(298,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"RED",(420,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"YELLOW",(520,33),font,0.5,(255,255,255),2,cv2.LINE_AA)

    # video biterse ya da frameler yanlis okunursa donguden cik demek
    if ret is False:
        break

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    # framelerdeki karincalanmalari yok etmek icin asagidaki mask islemleri uygulanir
    # "kernel = ((5,5),np.uint8)" islemi hata verdiginden dolayi 2.parametre (5,5) fonksiyon icine yazdik direkt
    mask = cv2.erode(mask,(5,5),iterations =2)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,(5,5))
    mask = cv2.dilate(mask,(5,5),iterations = 1)

    
    contours,_ =cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    center = None

    if len(contours) > 0:
        #sorted -> konturlari alana göre siralar
        max_contours = sorted(contours, key = cv2.contourArea, reverse=True)[0]
        # kontur alani icine sinirlayici bir cember cizer
        # x,y -> merkez , radius yaricap
        ((x,y),radius) = cv2.minEnclosingCircle(max_contours)
        cv2.circle(frame,(int(x),int(y)),int(radius),(255,255,0),3)

        # merkez noktalarina erismek icin max contours kullanilir
        M = cv2.moments(max_contours)
        # integer'a cevirme islemi
        center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))

        # centerin bulundugu konuma gore renk degerlerini degistirecez
        if center[1] <= 65:
            if 40<=center[0]<=140:

                blue_points = [deque(maxlen=512)]
                green_points = [deque(maxlen=512)]
                red_points = [deque(maxlen=512)]
                yellow_points = [deque(maxlen=512)]

                blue_index=0
                green_index=0
                red_index=0
                yellow_index=0

                # 67den itibaren olan yerleri temizler (beyaza cevirir)
                # 67 olmasinin sebebi dugmelerin oldugu kisimlari temizlemesine gerek olmadigi icin
                paintWindow[67:,:,:]=255

            elif 160<=center[0]<=255:
                color_index = 0

            elif 275<=center[0]<=370:
                color_index = 1

            elif 390<=center[0]<=485:
                color_index = 2

            elif 505<=center[0]<=600:
                color_index = 3

        else:
            if color_index == 0:
                blue_points[blue_index].appendleft(center)
                
            elif color_index == 1:    
                green_points[green_index].appendleft(center)
                
            elif color_index == 2:
                red_points[red_index].appendleft(center)
                
            elif color_index == 3:
                yellow_points[yellow_index].appendleft(center)

    else:
        blue_points.append(deque(maxlen=512))
        blue_index+=1
        
        green_points.append(deque(maxlen=512))
        green_index+=1
        
        red_points.append(deque(maxlen=512))
        red_index+=1
        
        yellow_points.append(deque(maxlen=512))
        yellow_index+=1

    points = [blue_points,green_points,red_points,yellow_points]
    
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1,len(points[i][j])):
                # baslangic ve bitis noktalarinin bos olmadigina dikkat edilir
                if points[i][j][k-1] is None or points[i][j][k] is None:
                    continue
                
                cv2.line(frame,points[i][j][k-1], points[i][j][k], colors[i], 2)
                cv2.line(paintWindow,points[i][j][k-1], points[i][j][k], colors[i], 2)
                

    cv2.imshow("Frame",frame)
    cv2.imshow("Paint",paintWindow)
    
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



