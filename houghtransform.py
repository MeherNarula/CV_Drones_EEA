import cv2
import numpy as np
import matplotlib.pyplot as plt

def hough_line(s):
    # Read the image
    original_image = cv2.imread(s)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    
    # Apply edge detection using Canny
    edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)
    
    # Apply Hough Transform to detect lines
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, np.array([]), minLineLength=50, maxLineGap=5)
    
    # Draw lines on the original image
    image_with_lines = original_image.copy()
    draw_lines(image_with_lines, lines)
    
    # Display the result
    plt.imshow(cv2.cvtColor(image_with_lines, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

def draw_lines(image, lines, color=(0, 0, 255), thickness=2):
    # Draw lines on the image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), color, thickness)

# Example usage:
hough_line("C:\important downloads\calculator.jpeg")