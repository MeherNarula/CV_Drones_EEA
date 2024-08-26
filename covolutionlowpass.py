import numpy as np 
import cv2

#import the image 
img=cv2.imread("C:\important downloads\galaxy.webp",1)

#form the filters 
kernel_identity = np.array([[0,0,0],[0,1,0],[0,0,0]])
kernel_3= np.ones((3,3) ,dtype=np.float32)/9.0
kernel_11=np.ones((11,11), dtype=np.float32)/121.0#float32 is used for smaller numbers and float64 is used fo bigger numbers , its the number of bits  

#Apply the filters 
output1 = cv2.filter2D(img,-1,kernel_identity)#-1 means the same depth as the pic
output2 = cv2.filter2D(img,-1,kernel_3)
output3 = cv2.filter2D(img,-1,kernel_11)

#Show the Image
cv2.imshow('same',output1)
cv2.imshow('same2',output2)
cv2.imshow('same3',output3)
cv2.waitKey(0)
