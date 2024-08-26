

import cv2
import numpy as np
s= "C:\important downloads\headphones.webp"

def solve(s):
    # Read the image
    image = cv2.imread(s, cv2.IMREAD_GRAYSCALE)
    
    # Perform Canny edge detection
    edges = cv2.Canny(image, 100, 200)  # Adjust thresholds as needed
    
    # Display the original and edge-detected images
    cv2.imshow('Original Image', image)
    cv2.imshow('Edges Detected', edges)
    
    # Wait for any key to be pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows
