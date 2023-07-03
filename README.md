
<h1>Ball_following_bot-2022-23-Project</h1>
<hr>
<img src="https://user-images.githubusercontent.com/79747698/229343724-9ffa2d01-7c86-4305-b14d-dd788f58a9de.jpeg" alt="Robotics club MNNIT" />
<h3>About</h3>
<p>This is a project based on hardware and OpenCV which is proposed and executed by robotics club of MNNIT to provide hands on experience and exposure to the students in different fields related to robotics.</p>
<img src="https://user-images.githubusercontent.com/79747698/229343600-aa178f7f-1cf4-4532-8e00-98a17d6e7e50.jpg" alt="Ball following bot" width="70%" height="60%"/>
<hr>
<h3>This project is mentored by:</h3>
<table>
  <tr>
    <th>Name</th>
    <th>Branch</th>
    <th>Registration number</th>
  </tr>
  <tr>
    <td>Kandukuri Yaswanth</td>
    <td>Civil Engineering</td>
    <td>20201057</td>
  </tr>
  <tr>
    <td>Anurag gupta</td>
    <td>Electronics and Communication Engineering</td>
    <td>20195168</td>
  </tr>
  <tr>
    <td>Purushotam Kumar Agrawal</td>
    <td>Electrical Engineering</td>
    <td>20192042</td>
  </tr>
 </table>
 <hr>
<h3>This project is completed by</h3>
<table>
  <tr>
    <th>Name</th>
    <th>Branch</th>
    <th>Registration number</th>
  </tr>
  <tr>
    <td>SSR Sri Harsha Kedarisetty</td>
    <td>Computer Science and Engineering</td>
    <td>20214527</td>
  </tr>
  <tr>
    <td>Vikas Gaur</td>
    <td>Mechanical Engineering</td>
    <td>20213038</td>
  </tr>
  <tr>
    <td>Vishal Yadav</td>
    <td>Mechanical Engineering</td>
    <td>20213044</td>
  </tr>
 </table>
<hr>
<h3> Tech Stack </h3>
<ul>
  <li>Python</li>
  <li>OpenCV</li>
  <li>Raspberry Pi [Raspbian OS buster series]</li>
 </ul>
<hr>
<h3>Hardware components</h3>
   <table> 
    <tr>
          <th>COMPONENT NAME</th>
          <th>QUANTITY</th>
          <th>DESCRIPTION</th>
        </tr>
        <tr>
          <td>Arduino Uno</td>
          <td>  1</td>
          <td>Microcontroller,used to drive the motor driver</td>
        </tr>
        <tr>
          <td>Motor Driver</td>
          <td>1</td>
          <td>use to control the working speed and direction of two motor</td>
        </tr>
        <tr>
          <td>DC Motor</td>
          <td>2</td>
          <td>use to rotate wheel</td>
        </tr>
        <tr>
          <td>Wheel</td>
          <td>2</td>
          <td>To drive the bot</td>
        </tr>
        <tr>
          <td>Raspberry Pi</td>
          <td>1</td>
          <td>use in image processing,wireless connectivity,send the coordinate and distance of object to arduino</td>
        </tr>
        <tr>
          <td>Camera Module</td>
          <td>1</td>
          <td>used to detect the ball as an objeft in the video frame</td>
        </tr>
        <tr>
          <td>BreadBoard</td>
          <td>1</td>
          <td>use in power distribution ,use to connect multiple pin to a single pin</td>
        </tr>
     </table>
   
   <hr>
<h3>Circuit Diagram</h><br>
<br>
 <ul>
   <li> <img src="https://user-images.githubusercontent.com/117128615/229332812-a73c6fbc-30c1-4024-96b3-d3f0309c2496.png" alt="Circuit diagram" width="80%" height="60%"/></li>
   <li><img src="https://user-images.githubusercontent.com/117128615/229332931-1dc10930-3478-4594-9fa2-fbc279fc4072.png" alt="arduino diagram" width="80%" height="50%"/></li>
</ul>
<hr>
<h3>Implementation</h3>
This project uses wide range of functions for the processing of camera input and communicating 
with the arduino for finding and following the ball
We use the following modules.
<ol type="1">
<li>Serial: provides a way to communicate with devices connected to a serial port 
on a computer, such as USB-to-serial adapters. It allows you to configure the serial port settings, 
such as the baud rate, data bits, parity, and stop bits, and then send and receive data using the read() and write() methods. </li>

<li>PiRGBArray and PiCamera:PiRGBArray provides a way to store the image data captured by the camera in a format that is easy to work with in Python.
 and the PiCamera python module that provides a way to control and interface with the camera module on a Raspberry Pi.</li>

<li>OpenCv(Open Source Computer Vision):It is an open-source computer vision and machine learning software library. 
It provides various functions and algorithms that can be used to perform tasks related to image and video processing.</li>

<li>NumPy (Numerical Python):It is a Python library for scientific computing and data analysis. 
It provides powerful multi-dimensional arrays and matrices, as well as functions to manipulate and perform operations on them.
NumPy is widely used in scientific computing, data analysis, and machine learning applications.</li>
  <li>Virtual Enviroment(Venv):We usually require different modules compared to the already installed versions of a certain software present on the system, therefore its highly recommended to use virtual environment for every project 
For our project the dependencies used in the virtual environment are available in the packages.txt
  </li>
</ol>

The basis of implementation of the ball detection is differentiating the ball color from its 
background and finding its contour to make the bot follow the ball

This is a very efficient way of detecting the ball as it provides accurate dimensions of the ball through some processing.

In the code the step of processing is as follows
<ol type="1">
<li>We first Set the basic set of values for the pi camera such as resolution , framerate and use PiRGBArray to capture it in store in an array .</li>

<li>We then ask the user for setting the hsv values for the ball they want the ball to follow.</li>

<li>Now the contour is formed from the given hsv values, High definition of the contour assures accurate detection and smooth run of the bot.</li>

<li>So for the user input we are creating trackbars with min and max values for the hsv so as to adjust the contour we obtain in the Mask frame.</li>

<li>Through this we are applying the fliter over the input for the required input.</li>

<li>After applying we are implementing the serial connection between the raspberry pi and arduino uno through the /dev/ttyACM0 port with baud rate of 9600.</li>

<li>We then run a loop for the frame in the camera.capture_continuous function that takes format of input and the use_video_port if availiable with the captures.</li>
</ol>

From here we have to explain line by line of what happens to every frame that the camera

1.	i = frame.array: 
This line assigns the value of frame.array to the variable I;
2.	image = cv2.flip(i, -1): 
This line flips the image stored in i using the OpenCV function cv2.flip and -1 indicates if the image should be flipped horizontally or vertically 
3.	if range_filter == 'RGB': frame_to_thresh = image.copy(): 
This line checks if the value of range_filter is 'RGB'. If it is, it creates a copy of the image and assigns it to the variable frame_to_thresh 
4.	else: frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV): 
If range_filter is not 'RGB', this line converts the image from the RGB color space to the HSV color space using the OpenCV function cv2.cvtColor, and assigns the result to the variable frame_to_thresh.
5.	v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter):
 This line calls a function get_trackbar_values with the argument range_filter, and assigns the returned values to six variables: v1_min, v2_min, v3_min, v1_max, v2_max, and v3_max
6.	thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max)): 
This line creates a binary image (thresh) using the OpenCV function cv2.inRange, which thresholds the frame_to_thresh image based on the values of v1_min, v2_min, v3_min, v1_max, v2_max, and v3_max. Pixels in the frame_to_thresh image that fall within this range are set to white, while pixels outside the range are set to black
7.	kernel = np.ones((5, 5), np.uint8): 
This line creates a 5x5 kernel (an array of ones) using NumPy's ones function and assigns it to the variable kernel. The data type of the kernel is np.uint8, which stands for "unsigned 8-bit integer".
8.	mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel): 
This line applies an opening operation to the binary image thresh using the cv2.morphologyEx function with the cv2.MORPH_OPEN flag. An opening operation consists of an erosion followed by a dilation, and is useful for removing small objects and noise from the foreground of an image. The kernel is used as the structuring element for the operation, and the resulting binary image is assigned to the variable mask

9.	mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel): 
This line applies a closing operation to the binary image mask using the cv2.morphologyEx function with the cv2.MORPH_CLOSE flag. A closing operation consists of a dilation followed by an erosion, and is useful for closing small holes in the foreground of an image. The kernel is used as the structuring element for the operation, and the resulting binary image is assigned back to the variable mask

Here is a image of the ball getting detected after applying the hsv values

<img src="https://user-images.githubusercontent.com/99545486/229351416-c84fd054-6c86-4857-9c5f-ed791d07a2f6.jpg" alt="Ball Contour" width="80%" height="60%"/>

10.	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]: This line finds the contours in the binary image mask using the cv2.findContours function. The mask.copy() argument is a copy of the binary image to avoid modifying the original image. The second argument cv2.RETR_EXTERNAL specifies that only the external contours (contours along the edges of the foreground) should be found. The third argument cv2.CHAIN_APPROX_SIMPLE specifies that the contours should be approximated using only the endpoints of their segments, which saves memory. The [-2] at the end of the line extracts the second-to-last element of the tuple returned by cv2.findContours, which contains the actual contours. The resulting list of contours is assigned to the variable cnts
11.	Here is the total description of detection of ball and sending the required data to Arduino:-
This block of code checks if the list of contours cnts is not empty. If there are contours present, it finds the contour with the largest area using cv2.contourArea and encloses it in a circle using cv2.minEnclosingCircle. It then calculates the centroid of the contour using cv2.moments and calculates the distance of the object from the camera using the formula dist = (f * 6) / (2 * radius), where f is the focal length of the camera and radius is the radius of the enclosing circle. The calculated distance is printed and sent over serial communication using ser.write. The code then checks if the radius of the enclosing circle is greater than a minimum size, and if so, it updates the tracking points by drawing circles and text on the image using cv2.circle, cv2.putText, and cv2.putText. Finally, the updated image is displayed using cv2.imshow



<h4>The predef.py is the same code that has been modified with hardcoded values of hsv to detect a specify ball of a certain color</h4>


<h4>Now coming to the aduino Code implementation</h4> 

Here we are firstly  defining the pins for the Arduino 
<code>
//M1 M2 left motors
#define M1 3 //forward
#define M2 5 //backward
//M3 M4 right motors
#define M3 6 //forward
#define M4 11 //backward
</code>
After that we have to setup the pins in the function
<code>
void setup()
{
    Serial.begin(9600);

    pinMode(M1, OUTPUT);
    pinMode(M2, OUTPUT);
    pinMode(M3, OUTPUT);
    pinMode(M4, OUTPUT);
} 
</code>

Then the code control shifts to the loop function 


The loop function begins with a condition of  Serial. Available() which returns true or false 
So the rest of the code runs if we are receiving a serial input from the raspberry pi 


The we are reading the input from the serial that we are receiving in the form of string 
We are using he necessary functions such as Serial.readStringUntil('\n') for getting the values encoded in the string and then atof(a.c_str()) for converting the sting to a floating integer for the required values that is 
3)Distance of the ball from the camera
2)X coordinate of the ball’s center in the frame
3) Y coordinate of the ball’s center in the frame


Then we are defining some functions for using in the logic

The Logic is simple where the  balls x coordinates are used to call the function according to where the balls center is .
Using this we are able to move the bots motors at necessary speed and also calibrate the amount of left and right movement the bot need to move.


   
     
<hr>
<h3>Application</h3>
<ul>
<li>Goods carrying and management: The bot can be upgraded to track and follow staff in industries that help and carry much heavier loads and dynamically follow any path followed by a staff which results in efficiency and effectiveness and is economical to the industries.</li>
<li>Research: Ball following bots can be used in research settings to study various aspects of robotics and machine learning, such as object detection, tracking, and control.</li>
</ul>

<hr>
<h3>Future plans</h3>
<ul>
<li>Machine learning models can be implemented to make the bot work in complex dynamic environments.</li>
<li>Image analysis part can be used for home automated security systems, automated CCTV’s which can track intruders and click pictures and send them over wireless systems.</li>
<li>The bot can be upgraded by replacing raspberry Pi with jetson nano to provide GPU power for object detection and model training dynamically and to help in building real-time applications.</li>
<li>Currently working on integrating neural networks and the bot to build bots like a person following an object following bot which helps in carrying and deploying heavy objects at the desired destination without human intervention.</li>
  </ul>
<hr>

