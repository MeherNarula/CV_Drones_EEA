import cv2
import numpy as np

def apply_sobel(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel filter for horizontal edges
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)

    # Apply Sobel filter for vertical edges
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # Combine results to obtain the magnitude of the gradient
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Normalize the magnitude to 0-255
    magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

    # Convert to uint8 for display
    magnitude = np.uint8(magnitude)

    return magnitude

# Read the input image
input_image = cv2.imread("C:\important downloads\headphones.webp")

# Apply Sobel filter and obtain the magnitude of the gradient
edge_detected_image = apply_sobel(input_image)

# Display the original and edge-detected images
cv2.imshow('Original Image', input_image)
cv2.imshow('Edge-Detected Image', edge_detected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
