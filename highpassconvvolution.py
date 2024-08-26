import cv2
import numpy as np 

image= cv2.imread('')

image=cv2.cvtColor(image,0)
#performing the edge detection 
gradients_sobelx=cv2.Sobel(image,-1,1,0)#-1 indicates original depth 
gradients_sobely=cv2.Sobel(image,-1,0,1)
gradients_sobelxy=cv2.addWeighted(gradients_sobelx,0.5,gradients_sobely,0.5,0)

gradients_laplacian = cv2.Laplacian(image,-1)

canny_output=cv2.Canny(image,80,150)