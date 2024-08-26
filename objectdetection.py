import cv2
import numpy as np

def shape(s):
    # Read the image
    image = cv2.imread(s)
    original_image = image.copy()  # Make a copy for marking centers
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and improve contour detection
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Apply Canny edge detection
    edges = cv2.Canny(blurred_image, 50, 150)
    
    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Define a dictionary to map the number of sides to shape names
    shape_names = {
        3: "Triangle",
        4: "Rectangle",
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon",
        9: "Nonagon"
    }
    
    # List to store information about all detected shapes
    detected_shapes = []
    
    # Iterate through each contour
    for contour in contours:
        # Approximate the shape to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Get the number of sides of the approximated polygon
        num_sides = len(approx)
        
        # Get the area of the contour
        area = cv2.contourArea(contour)
        
        # Check if the shape has 3 to 9 sides (simple shapes)
        if 3 <= num_sides <= 9:
            # Print the name of the shape
            shape_name = shape_names[num_sides]
            
            # Append information about the shape to the list
            detected_shapes.append({
                "name": shape_name,
                "area": area,
                "contour": contour
            })
            
    # Sort the list of detected shapes based on area in descending order
    detected_shapes.sort(key=lambda x: x["area"], reverse=True)
    
    for idx, shape_info in enumerate(detected_shapes):
        # Display the name of all shapes
        M = cv2.moments(shape_info["contour"])
        if M["m00"] != 0:
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
            cv2.putText(original_image, shape_info["name"], (center_x - 30, center_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
        # Display the center for the largest two shapes
        if idx < 2:
            M = cv2.moments(shape_info["contour"])
            if M["m00"] != 0:
                center_x = int(M["m10"] / M["m00"])
                center_y = int(M["m01"] / M["m00"])
                cv2.circle(original_image, (center_x, center_y), 5, (255, 0, 0), -1)
               
    # Display the image with marked centers and shape names
    cv2.imshow("Image with Centers and Names", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
image_path = r"C:\important downloads\polygons.png"
shape(image_path)