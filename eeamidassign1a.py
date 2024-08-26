import cv2
import numpy as np

def ig_filter(image_path):
    # Step 1: Read the image
    original_image = cv2.imread(image_path)

    # Step 2: Reduce brightness to 0.5 of its initial value
    reduced_brightness_image = original_image * 0.5

    # Step 3: Increase contrast to 1.5 of its initial value
    increased_contrast_image = cv2.convertScaleAbs(reduced_brightness_image, alpha=1.5, beta=0)

    # Step 4: Convert BGR to HSV and increase saturation to 1.5 of its initial value
    hsv_image = cv2.cvtColor(increased_contrast_image, cv2.COLOR_BGR2HSV)
    hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * 1.5, 0, 255)
    final_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    # Display the final image
    cv2.imshow('Final Image', final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
image_path = "s"
ig_filter(image_path)