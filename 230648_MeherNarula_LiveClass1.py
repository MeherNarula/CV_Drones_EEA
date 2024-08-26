
import cv2
import numpy as np
 
#code to solve the problem 
image = cv2.imread(rs)
 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 

fourier = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)

fourier_shift = np.fft.fftshift(fourier)

magnitude = 20*np.log(cv2.magnitude(fourier_shift[:,:,0],fourier_shift[:,:,1]))
 

magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
 
#code to show the image
cv2.imshow('ft', magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows('ft')


