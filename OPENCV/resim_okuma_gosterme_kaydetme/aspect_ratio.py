import cv2

'''
aspect ratio : en boy oranini ifade eder.
fonksiyon icine 4 arguman verilebilir ilk arguman resmin tutulacagi degiskendir
resmi yeniden boyutlandirirken bir takim cakismalar olabilir bunu engellemek icin default (varsayilan) 
olarak INTER_AREA kullanilir.
-> resmin yeni boyutunu temsil etmek uzere yeni dimenson diye bir degisken olusturulur.
-> resmin boyutlari elde edilir
-> resmin boyutlarina ulasmak icin img.shape[:2] ifadesi kullanilir
-> interpolasyon  degeri basta verdigimiz inter area dir cakismamamsi icin

'''
def resizewithAspectratio(img, width=None ,height=None, inter=cv2.INTER_AREA):
    dimension = None
    (h, w) = img.shape[:2]
    if width is None and height is None:
        return img
    if width is None:
        r = height / float(h)
        dimension = (int(w*r), height)
    else:
        r = width / float(w)
        dimension = (width, int(h*r))

    return cv2.resize(img, dimension, interpolation=inter)

img = cv2.imread("C:\\Users\\zelih\\OneDrive\\Belgeler\\OPENCV\\resim_okuma_gosterme_kaydetme\\yildizligece.jpg")
img1 = resizewithAspectratio(img,width=None,height=200,inter=cv2.INTER_AREA)
cv2.imshow("Original",img)
cv2.imshow("Resized",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


