import cv2
import random
img= cv2.imread("C:\important downloads\galaxy.webp",1)
print(img.shape)

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

tag = img[200:300,500:800]
img[400:500,100:400]=tag
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()