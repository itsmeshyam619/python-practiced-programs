import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
# Load YOLO model
net = cv2.dnn.readNet('yolov8.weights', 'yolov8.cfg')
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
# Initialize video capture
cap = cv2.VideoCapture(0)  # Replace 0 with the video file path for recorded footage

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess frame
    height, width, channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Process detection
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Threshold for detection
                # Get bounding box
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Draw rectangle
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Shop Intrusion Detection", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
restricted_zone = [(100, 100), (400, 400)]  # Example coordinates
cv2.rectangle(frame, restricted_zone[0], restricted_zone[1], (0, 0, 255), 2)
if x > restricted_zone[0][0] and y > restricted_zone[0][1]:
    print("Intrusion Detected!")
if intrusion_detected:
    cv2.imwrite("intrusion_event.jpg", frame)
    with open("log.txt", "a") as log:
        log.write(f"Intrusion detected at {time.ctime()}\n")
