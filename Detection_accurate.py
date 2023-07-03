import cv2
import numpy as np
from imutils.video import VideoStream
from concurrent.futures import ThreadPoolExecutor

# Define the capture device
vs = VideoStream(src=0, resolution=(640, 480)).start()

# Define a function to process the frames


def process_frame(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    gray = cv2.GaussianBlur(gray, (23, 23), 0)

    # Detect circles using HoughCircles function
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100,
                              param1=100, param2=30, minRadius=20, maxRadius=400)

    # If circles are detected, calculate the distance to the ball and draw the circles
    if circles is not None:
        # Convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # Loop over the detected circles and draw them on the frame
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv2.circle(frame, (x, y), 2, (0, 0, 255), 3)
            # Calculate the distance to the ball using the radius
            # 1250 is a constant that depends on the size of the ball and the camera parameters
            distance = round(1250/r, 2)
            # Display the distance on the frame
            cv2.putText(frame, f"Distance: {distance} cm", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0 , 0 ), 2)

    return frame


# Create a thread pool with one worker
executor = ThreadPoolExecutor(max_workers=1)

# Loop over the frames from the camera
while True:
    # Read a frame from the camera
    frame = vs.read()

    # Process the frame in a separate thread
    future = executor.submit(process_frame, frame)

    # Display the processed frame
    cv2.imshow('frame', future.result())

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture device and close all windows
vs.stop()
cv2.destroyAllWindows()
