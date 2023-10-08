import cv2
import numpy as np
def set_capture(capture_device):
    # Initialize video capture from the camera
    cap = cv2.VideoCapture(capture_device)
    return cap

def set_color_ranges():
    # Convert RGB color (20, 0, 255) to HSV for blue
    rgb_blue = np.uint8([[[20, 0, 255]]])
    hsv_blue = cv2.cvtColor(rgb_blue, cv2.COLOR_BGR2HSV)

    # Define a threshold range for blue in the HSV color space
    blue_lower = np.array([hsv_blue[0][0][0] - 10, 100, 100])  # Adjust the -10 to fit your desired range
    blue_upper = np.array([hsv_blue[0][0][0] + 10, 255, 255])  # Adjust the +10 to fit your desired range

    # Convert RGB color (0, 153, 0) to HSV for green
    rgb_green = np.uint8([[[0, 153, 0]]])
    hsv_green = cv2.cvtColor(rgb_green, cv2.COLOR_BGR2HSV)

    # Define a threshold range for green in the HSV color space
    green_lower = np.array([hsv_green[0][0][0] - 10, 100, 100])  # Adjust the -10 to fit your desired range
    green_upper = np.array([hsv_green[0][0][0] + 10, 255, 255])  # Adjust the +10 to fit your desired range
    
    return blue_lower,blue_upper,green_lower,green_upper

def view_image_get_distance(color1_lower,color1_upper,color2_lower,color2_upper,cap):
    count = 0
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
            horizontal_distance = centroid1[0] - centroid2[0]
            vertical_distance = centroid1[1] - centroid2[1]
            cv2.putText(frame, f'Horizontal Distance: {horizontal_distance:.2f} pixels', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f'Vertical Distance: {vertical_distance:.2f} pixels', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if count == 1000:
                return horizontal_distance, vertical_distance

        # Show the frame
        cv2.imshow('Object Tracking', frame)
        count += 1
        if count > 1000:
            return 10000000,10000000

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

def view_image_get_distance1(blue_lower, blue_upper, green_lower, green_upper, cap):
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create masks for blue and green
        blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
        green_mask = cv2.inRange(hsv, green_lower, green_upper)

        # Find contours in the masks
        blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        green_contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Initialize lists to store centroids of blue and green objects
        blue_centroids = []
        green_centroids = []

        # Draw bounding boxes and calculate centroids for blue objects
        for contour in blue_contours:
            if cv2.contourArea(contour) > 100:  # Filter out small contours
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                centroid = (x + w // 2, y + h // 2)
                blue_centroids.append(centroid)

        # Draw bounding boxes and calculate centroids for green objects
        for contour in green_contours:
            if cv2.contourArea(contour) > 100:  # Filter out small contours
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                centroid = (x + w // 2, y + h // 2)
                green_centroids.append(centroid)

        # Calculate distance between centroids of blue and green objects
        for blue_centroid in blue_centroids:
            for green_centroid in green_centroids:
                horizontal_distance = blue_centroid[0] - green_centroid[0]
                vertical_distance = blue_centroid[1] - green_centroid[1]
                cv2.putText(frame, f'Distance: ({horizontal_distance:.2f}, {vertical_distance:.2f}) pixels',
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show the frame
        cv2.imshow('Object Tracking', frame)
        count += 1
        if count > 1000:
            return 10000000, 10000000

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close all windows
    cap.release()
    cv2.destroyAllWindows()
