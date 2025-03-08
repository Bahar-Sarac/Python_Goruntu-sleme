import cv2
import numpy as np
import matplotlib.pyplot as plt

# I = cv2.imread(r'C:\Users\Bahar\Desktop\resimler1\circles.png', 0)
# I3 = cv2.imread(r'C:\Users\Bahar\Desktop\resimler1\fig1.jpg', 0)
"""
print(I.shape)
cv2.imshow('I',I)

cv2.waitKey()
cv2.destroyAllWindows()
"""
"""
print(I.shape)

se=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15)) #se kerneldir
print(se)
I2=cv2.dilate(I,se) 

cv2.imshow('I',I)
cv2.imshow('I2',I2)
cv2.waitKey()
cv2.destroyAllWindows()
"""
"""
print(I.shape)

se=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(40,40)) #15,15
print(se)
I2=cv2.dilate(I,se)
I4=cv2.morphologyEx(I3,cv2.MORPH_OPEN,se)

cv2.imshow('I3',I3)
cv2.imshow('I4',I4)
cv2.waitKey()
cv2.destroyAllWindows()
"""
"""
print(I.shape)

se=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(40,40)) #15,15
print(se)
I2=cv2.dilate(I,se)
I4=cv2.morphologyEx(I3,cv2.MORPH_OPEN,se)

I4_cnt1=cv2.erode(I3,se)
I4_cnt2=cv2.dilate(I4_cnt1,se)

cv2.imshow('I3',I3)
cv2.imshow('I4',I4)
cv2.imshow('Ier',I4_cnt1)
cv2.imshow('Idil',I4_cnt2)
cv2.waitKey()
cv2.destroyAllWindows()
"""

# print(I.shape)
#
# se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (40, 40))  #15,15
# print(se)
# I2 = cv2.dilate(I, se)
# I4 = cv2.morphologyEx(I3, cv2.MORPH_OPEN, se)
#
# I4_cnt1 = cv2.erode(I3, se)
# I4_cnt2 = cv2.dilate(I4_cnt1, se)
#
# print(np.sum(I4 - I4_cnt2))
# cv2.imshow('I3', I3)
# cv2.imshow('I4', I4)
# cv2.imshow('Ier', I4_cnt1)
# cv2.imshow('Idil', I4_cnt2)
# cv2.waitKey()
# cv2.destroyAllWindows()
