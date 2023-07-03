import serial
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import argparse
import numpy as np

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(640, 480))


def callback(value):
    pass



def main():

    ser = serial.Serial('/dev/ttyACM0', 9600)   #the arduino is conected here amd the bard value is set to 9600

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        i = frame.array
        image = cv2.flip(i, -1)
        
        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)         #getting the thresh of the image from rgb to hsv 

    

        thresh = cv2.inRange(
            frame_to_thresh, (0 , 173, 50), (131, 255, 245))

        #morphing to get a clearer image without distortions in the image buffer
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # finding the contour in the mask and intializing the current
        # (x, y) center of the ball
        cnts = cv2.findContours(
            mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            #finding the max contour and enclosing it 
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            #distance calculation
            
            
            f = 637.27  
            dist = (f * 6) / (2 * radius)
            print("py", dist)
            r = str(dist) + "\n" + str(x) + "\n" + str(y) + "\n"
            
            ser.write(r.encode("utf-8"))

            # only proceed if the radius meets a minimum size
            if radius > 10:
                #updating the tracking points according to the centriod we got 
                cv2.circle(image, (int(x), int(y)),
                           int(radius), (0, 255, 255), 2)
                cv2.circle(image, center, 3, (0, 0, 255), -1)
                cv2.putText(image, "centroid", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0 ),
                            1)
                cv2.putText(image, "(" + str(center[0]) + "," + str(center[1]) + ")", (center[0] + 10, center[1] + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

        # show the frame to our screen
        cv2.imshow("Original", image)
        cv2.imshow("Mask", mask)

        rawCapture.truncate(0)   #ending the frame buffer input

        if cv2.waitKey(1) & 0xFF is ord('q'):
            break

#just a checking variable for the 
if __name__ == '__main__':
    main()

