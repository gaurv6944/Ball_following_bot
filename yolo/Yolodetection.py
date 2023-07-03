import cv2
import numpy as np

# Load YOLOv3 weights and configuration
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load class names
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Set input and output layers
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Load image
img = cv2.imread("ball.jpg")

# Get image dimensions
height, width, channels = img.shape

# Create blob from image
blob = cv2.dnn.blobFromImage(
    img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

# Pass blob through network
net.setInput(blob)
outs = net.forward(output_layers)

# Process outputs
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5 and class_id == 0:  # 0 corresponds to the class "person"
            # Get center coordinates and dimensions of bounding box
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Calculate top-left corner coordinates of bounding box
            x = center_x - w // 2
            y = center_y - h // 2

            # Add bounding box and confidence to lists
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Apply non-max suppression to remove overlapping bounding boxes
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Draw final bounding boxes on image
for i in indices:
    i = i[0]
    x, y, w, h = boxes[i]
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show image
cv2.imshow("Ball Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
