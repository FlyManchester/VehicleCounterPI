from picamera import PiCamera
import time
from datetime import datetime
import cv2
from vehicle_detector import VehicleDetector

temp_image_location = "/tmp/Vehicle/image.jpg"

## Startup
camera=PiCamera()
time.sleep(2)

def date_time():
    now=datetime.now()
    dtstring=now.strftime("%Y/%m/%d %H:%M:%S")
    return(dtstring)

def get_next_image():
    camera.capture(temp_image_location)
    print('done')


vd = VehicleDetector()

get_next_image()
img = cv2.imread(temp_image_location)

vehicle_boxes = vd.detect_vehicles(img)

vehicle_count = len(vehicle_boxes)
print('count of cars =', vehicle_count )
for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

cv2.imshow("Cars", img)
cv2.waitKey(0)
vehicle_count = len(vehicle_boxes)
