import cv2
import numpy as np
import matplotlib.pyplot as plt

#print("Opencv sürümü:", cv2.__version__)

I=cv2.imread(r'C:\Users\Bahar\Desktop\resimler1\peppers.png',1)

# print(type(I))
# print(I.ndim) #boyut sayısını (ndim) konsola yazdırır. Bir renkli görüntü 3 boyutlu bir dizi olarak temsil edilir (yükseklik, genişlik, renk kanalları). Dolayısıyla, bu değer genellikle 3 olacaktır. Eğer görüntü gri tonlamalı ise, bu değer 2 olur.
# print(I.shape) #şekil bilgilerini (boyutlarını) konsola yazdırır
# print(I.dtype) #I dizisinin veri tipini (dtype) konsola yazdırır


# #Bu kod parçacığı, bir pikselin değerini değiştirip, görüntünün nasıl göründüğünü kontrol etmenizi sağlar:
# print('*'*28)
# print(I[10,10]) #I görüntüsündeki (10, 10) koordinatındaki pikselin renk değerleri
# I2=I.copy() #I görüntüsünün bir kopyasını I2 değişkenine atar
# I2[10,10]=[8,8,8] #I2 kopyası üzerinde (10, 10) koordinatındaki pikselin rengini değiştirir. [8,8,8] değeri, bu pikselin renk değerini çok koyu gri (neredeyse siyah) yapar. (Iyı etkilemez)
# print(I[10,10]) #I görüntüsündeki (10, 10) koordinatındaki pikselin renk değerlerini yazdırır. (I2yi etkilemez)
#
# cv2.imshow('peppers1',I) #I görüntüsünü, "peppers1" adlı yeni bir pencere içinde görüntüler.
# cv2.waitKey(0) #Programın duraklamasını sağlar ve herhangi bir tuşa basılmasını bekler.
# cv2.destroyAllWindows() #Açık olan tüm OpenCV pencerelerini kapatır. Görüntü gösterildikten sonra kullanıcı pencereyi kapatmak istediğinde bu fonksiyon kullanılır.
#

# #Bu kod parçacığı, rastgele bir görüntü oluşturur ve bunu uygun bir formatta (0-255 arası tam sayılar) temsil eder:
# I3=np.random.random((300,500,3)) #!! 300x500 piksel boyutunda ve 3 renk kanalı (RGB) olan bir dizi oluşturur. np.random.random fonksiyonu, 0 ile 1 arasında rastgele değerler içeren bir NumPy dizisi oluşturur. I3 değişkeni, her piksel için 3 değer (kırmızı, yeşil, mavi) içeren bir dizi olacaktır.
# print(I3.shape) #(300, 500, 3) -  Dizinin 300 piksel yüksekliğinde, 500 piksel genişliğinde ve 3 renk kanalına sahip olduğunu gösterir.
# I3=np.uint8(np.round(I3*255)) #Dizideki değerleri 0 ile 255 arasındaki tam sayılara dönüştürür.
# print(I3.dtype)


# #OpenCV, görüntüleri genellikle BGR formatında saklar. Matplotlib, RGB modunda görüntüler.
# plt.imshow(I) #imshow fonksiyonu, verilen diziyi (bu durumda bir görüntü dizisini) bir görüntü olarak gösterir. I değişkeni, daha önce okunan bir görüntüyü temsil ediyor.
# plt.waitforbuttonpress() #Kullanıcı bir tuşa bastığında, program bir sonraki satıra geçer.
# plt.close() #Açık olan matplotlib penceresini kapatır.


# I4=np.zeros((I.shape[0],I.shape[1],3),dtype=np.uint8)
# #np.zeros fonksiyonu, verilen boyutlarda (burada I dizisinin yüksekliği ve genişliği ile 3 renk kanalı) sıfır değerlerinden oluşan bir NumPy dizisi oluşturur.
# #dtype=np.uint8 parametresi, dizinin veri türünü uint8 olarak belirler; bu da her bir pikselin 0 ile 255 arasında tam sayılar içerebileceği anlamına gelir.
# print(I4.shape)
# I_b=I[:,:,0] #İlk renk kanalını (kırmızı) I_b değişkenine atar. I_b, I dizisinin her piksel için kırmızı kanal değerlerini içeren 2D bir dizi olacaktır.
# print(I_b.shape)


# I4=np.zeros((I.shape[0],I.shape[1],3),dtype=np.uint8)
# print(I4.shape)
# I_b=I[:,:,0] #I dizisinin ilk renk kanalını (kırmızı) I_b değişkenine atar.
# I_g=I[:,:,1] #I dizisinin ikinci renk kanalını (yeşil) I_g değişkenine atar.
# I_r=I[:,:,2] #I dizisinin üçüncü renk kanalını (mavi) I_r değişkenine atar.
# print(I_b.shape)
#
# cv2.imshow('random1',I_r) #I_r yalnızca mavi kanalın değerlerini içerdiği için bu görüntü gri tonlamalı olarak gösterilecektir.
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# I4=np.zeros((I.shape[0],I.shape[1],3),dtype=np.uint8)
# print(I4.shape)
# I_b=I[:,:,0] #I dizisinin ilk renk kanalını (kırmızı) I_b değişkenine atar.
# I_g=I[:,:,1] #I dizisinin ikinci renk kanalını (yeşil) I_g değişkenine atar.
# I_r=I[:,:,2] #I dizisinin üçüncü renk kanalını (mavi) I_r değişkenine atar.
# print(I_b.shape)
# I4[:,:,0]=I_r #I4 dizisinin kırmızı kanalını I_r ile günceller. Burada I_r, aslında mavi kanalın değerlerini içeriyor.
# I4[:,:,0]=I_g #I4 dizisinin kırmızı kanalını I_g ile günceller. Bu, önceki I_r değerini geçersiz kılar.
# I4[:,:,0]=I_b #I4 dizisinin kırmızı kanalını I_b ile günceller. Bu, yine önceki değerleri geçersiz kılar.
#
# cv2.imshow('random1',I_r) #I_r yalnızca mavi kanalın değerlerini içerdiği için bu görüntü gri tonlamalı olarak gösterilecektir.
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# I4=np.zeros((I.shape[0],I.shape[1],3),dtype=np.uint8)
# print(I4.shape)
# I_b=I[:,:,0] #I dizisinin ilk renk kanalını (kırmızı) I_b değişkenine atar.
# I_g=I[:,:,1] #I dizisinin ikinci renk kanalını (yeşil) I_g değişkenine atar.
# I_r=I[:,:,2] #I dizisinin üçüncü renk kanalını (mavi) I_r değişkenine atar.
# print(I_b.shape)
# I4[:,:,0]=I_r #I4 dizisinin kırmızı kanalını I_r ile günceller. Burada I_r, aslında mavi kanalın değerlerini içeriyor.
# I4[:,:,1]=I_g #I4 dizisinin kırmızı kanalını I_g ile günceller. Bu, önceki I_r değerini geçersiz kılar.
# I4[:,:,2]=I_b #I4 dizisinin kırmızı kanalını I_b ile günceller. Bu, yine önceki değerleri geçersiz kılar.
#
# cv2.imshow('random1',I4) #I_r yalnızca mavi kanalın değerlerini içerdiği için bu görüntü gri tonlamalı olarak gösterilecektir.
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# I4=np.zeros((I.shape[0],I.shape[1],3),dtype=np.uint8)
# print(I4.shape)
# I_b=I[:,:,0] #I dizisinin ilk renk kanalını (kırmızı) I_b değişkenine atar.
# I_g=I[:,:,1] #I dizisinin ikinci renk kanalını (yeşil) I_g değişkenine atar.
# I_r=I[:,:,2] #I dizisinin üçüncü renk kanalını (mavi) I_r değişkenine atar.
# print(I_b.shape)
# I4[:,:,0]=I_r
# I4[:,:,1]=I_g
# I4[:,:,2]=I_b
#
# plt.imshow(I)
# plt.waitforbuttonpress()
# plt.close()
#
# cv2.imshow('random1',I4) #I_r yalnızca mavi kanalın değerlerini içerdiği için bu görüntü gri tonlamalı olarak gösterilecektir.
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# I5_b, I5_g, I5_r=cv2.split(I) #cv2.split() fonksiyonu, görüntüyü üç ayrı bileşene (BGR) ayırır.Dönen üç bileşen değişkenlere atanır.
# print(I5_b.shape)


# I5_b, I5_g, I5_r=cv2.split(I)
# I6=cv2.merge([I5_r,I5_g,I5_b]) #cv2.merge() fonksiyonu, bir dizi görüntü bileşenini birleştirerek tek bir görüntü matrisine dönüştürür.
# print(I6.shape)
# plt.imshow(I6)
# plt.waitforbuttonpress()
# plt.close()


# I7=I[:,:,::-1] #NumPy dizisi dilimleme (slicing) özelliğini kullanarak I matrisinin tüm satır ve sütunlarını alır, ancak üçüncü boyutu (renk kanalları) tersine çevirir.
# plt.imshow(I7)
# plt.waitforbuttonpress()
# plt.close()


# print(I.shape)
# I8=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
# print(I8.shape)
#
# cv2.imshow('example',I8)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# print(I.shape)
# I8=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) #COLOR_BGR2HSV
# print(I8.shape)
#
# cv2.imwrite('deneme1.tif',I8)
# cv2.imshow('example',I8)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# print(I.shape)
# I8=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) #COLOR_BGR2HSV
# print(I8.shape)
# cv2.imwrite('deneme1.tif',I8)
# plt.imshow(I8)
# plt.waitforbuttonpress()
# plt.close()


#matplotlib ile yapacak olursak:
# print(I.shape)
# I8=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) #COLOR_BGR2HSV
# print(I8.shape)
# cv2.imwrite('deneme1.tif',I8)
# plt.imshow(I8,cmap='gray',interpolation='Nearest')
# plt.waitforbuttonpress()
# plt.close()


# print(I.shape)
# I8=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) #COLOR_BGR2HSV
# print(I8.shape)
# cv2.imwrite('deneme1.tif',I8)
# plt.imshow(I8,cmap='gray',interpolation='Nearest')
# cv2.imwrite('deneme2.tif',dpi=600)
# plt.waitforbuttonpress()
# plt.close()

#Bunu sormazmış:
# I2=I.copy()
# cv2.line(I2,(100,100),(200,200),(255,255,0),thickness=3)
# cv2.imshow('example',I2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Bunu sormazmış:
# I2=I.copy()
# cv2.line(I2,(100,100),(200,200),(0,0,255),thickness=3)
# cv2.imshow('example',I2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Resmin üzerinde küçük bir nokta oluşturur
# I9 = cv2.imread(r'C:\Users\Bahar\Desktop\resimler1\fig1.jpg')
# print(I9.shape)
# I9[180,180]=[0,0,255]
# cv2.imshow('example',I9)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

