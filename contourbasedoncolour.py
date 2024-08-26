import cv2
import numpy as np
import matplotlib.pyplot as plt

def colour(s):
    # Read the image
    image_rgb= cv2.imread(s,-1)
    
    
   
    # Define the color range (here, red color is used as an example)
    red_lower = np.array([0, 0, 100], dtype=np.uint8)
    red_upper = np.array([100, 100, 255], dtype=np.uint8)
    
    # Create a binary mask for the specified color range
    color_mask = cv2.inRange(image_rgb, red_lower, red_upper)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on the original image
    result_image =image_rgb.copy()
    cv2.drawContours(result_image, contours, -1, (0, 255, 0), 2)  # -1 draws all contours
    
    # Display the result
    plt.imshow(result_image)
    plt.axis('off')
    plt.show()

# Example usage:
image_path = "C:\important downloads\coloured shapes.jpg"
colour(image_path)