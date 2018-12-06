import os
import cv2

dataset=[]
m='final'
image = cv2.imread("%s.jpg" %m)
print(image.shape)  # görüntünün boyut bilgisi , genişlik-yükseklik-sRGB

for i in os.listdir("C:/Users/Asus/Desktop/Proje çalışmaları/temizZemin"):     #pathdeki tüm verileri arraya atamak
    dataset.append(i)


for x in range(0,25):
    print(dataset[x])
    y=(dataset[x])
    image = cv2.imread("%s" %y)
    cv2.imshow("original", image)  # orjinal fotoğrafı ekrana basar
    cv2.waitKey(1)
    b=0
    for m in range(0,4):
        a=0
        for n in range(0,5):
            cropped = image[a:a+256, b:b+256]    #fotoğrafın kesilecek genişlik-uzunluk bilgisi
            cv2.imshow("cropped", cropped)      #kırpılan görüntüyü göster
            cv2.waitKey(1)
            cv2.imwrite("%sf_%sr_%sc.jpg" %(x,m,n), cropped)  # yeni görüntüyü dosyaya kaydet
            a=a+256
        b=b+256

    #cv2.imshow("original", image)  #orjinal fotoğrafı ekrana basar
#cv2.waitKey(1)
#cropped = image[200:240,200:250]    #fotoğrafın kesilecek genişlik-uzunluk bilgisi
#cv2.imshow("cropped", cropped)      #kırpılan görüntüyü göster
#cv2.waitKey(1)
#cv2.imwrite("img.jpg", cropped)  # yeni görüntüyü dosyaya kaydet


print("cropped images")
