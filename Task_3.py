import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('path_to_your_video_file.mp4')

# Define the HSV color range for the ball
lower_color = np.array([30, 150, 50])   # Modify these values based on your ball's color
upper_color = np.array([50, 255, 255])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask based on color range
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Only proceed if at least one contour is found
    if contours:
        # Find the largest contour in the mask
        largest_contour = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)

        # Draw a circle around the ball
        if radius > 10:  # Only track large enough objects
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)

    # Show the frame with tracking
    cv2.imshow('Ball Tracking', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
