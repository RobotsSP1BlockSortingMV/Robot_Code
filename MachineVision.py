import cv2
import numpy as np

# Initialize video capture from the camera
cap = cv2.VideoCapture(0)

# Define the colors to track in HSV format (you can use a tool like colorpicker.net)
import cv2
import numpy as np

# Convert RGB color (20, 0, 255) to HSV
rgb_color1 = np.uint8([[[20, 0, 255]]])  # RGB color
hsv_color1 = cv2.cvtColor(rgb_color1, cv2.COLOR_BGR2HSV)

# Define a threshold range based on the HSV color
color1_lower = np.array([hsv_color1[0][0][0] - 10, 100, 100])  # Adjust the -10 to fit your desired range
color1_upper = np.array([hsv_color1[0][0][0] + 10, 255, 255])  # Adjust the +10 to fit your desired range

# Convert RGB color (255, 0, 51) to HSV
rgb_color2 = np.uint8([[[255, 0, 51]]])  # RGB color
hsv_color2 = cv2.cvtColor(rgb_color2, cv2.COLOR_BGR2HSV)

# Define a threshold range based on the HSV color
color2_lower = np.array([hsv_color2[0][0][0] - 255, 0, 51])  # Adjust the -10 to fit your desired range
color2_upper = np.array([hsv_color2[0][0][0] + 255, 0, 51])  # Adjust the +10 to fit your desired range

#color1_lower = np.array([25, 100, 100])
#color1_upper = np.array([35, 255, 255])
#color2_lower = np.array([100, 100, 100])
#color2_upper = np.array([120, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create masks for each color range
    mask1 = cv2.inRange(hsv, color1_lower, color1_upper)
    mask2 = cv2.inRange(hsv, color2_lower, color2_upper)

    # Find contours in the masks
    contours1, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes and calculate centroids
    for contour in contours1:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        centroid1 = (x + w // 2, y + h // 2)

    for contour in contours2:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        centroid2 = (x + w // 2, y + h // 2)

    # Calculate distance between centroids
    if 'centroid1' in locals() and 'centroid2' in locals():
        distance = np.sqrt((centroid1[0] - centroid2[0])**2 + (centroid1[1] - centroid2[1])**2)
        cv2.putText(frame, f'Distance: {distance:.2f} pixels', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('Object Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
