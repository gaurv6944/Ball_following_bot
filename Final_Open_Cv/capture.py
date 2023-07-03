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


def get_trackbar_values(range_filter):
    values = []

    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
            values.append(v)
    return values



# Constructing the argument parse and parse the arguments for the terminal screen
ap = argparse.ArgumentParser()
# the argument is used to specify a range filter that can be either RGB or HSV.
#-f and --filter expect a value 
ap.add_argument('-f', '--filter', required=True,
                help='Range filter. RGB or HSV')

#used to convert the "Namespace" object into dictionary values for 
args = vars(ap.parse_args())

#if we dont get the correct fliter that is rgb or Hsv then we put up a request to   
if not args['filter'].upper() in ['RGB', 'HSV']:
    ap.error("Please speciy a correct filter.")

# ensuring that the filter is case-insensitive
range_filter = args['filter'].upper()



# set up a graphical user interface by create a window to display the images or videos.
cv2.namedWindow("Trackbars", 0)

for i in ["MIN", "MAX"]:
    v = 0 if i == "MIN" else 255
    # We are tweaking with the variable instantly without closing and relaunching the program
    for j in range_filter:
        cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, callback)


ser = serial.Serial('/dev/ttyACM0', 9600)   #the arduino is conected here amd the bard value is set to 9600

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    i = frame.array
    image = cv2.flip(i, -1)
    if range_filter == 'RGB':
        frame_to_thresh = image.copy()
    else:
        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)         #getting the thresh of the image from rgb to hsv 

    v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(
        range_filter)

    thresh = cv2.inRange(
        frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

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
    #cv2.imshow("Mask", mask)
#     cv2.imshow()

    rawCapture.truncate(0)   #ending the frame buffer input

    if cv2.waitKey(1) & 0xFF is ord('q'):
        break
