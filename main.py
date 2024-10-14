# Modules
import cv2
import pickle
import cvzone
import numpy as np

# Import Video
cap = cv2.VideoCapture(r'C:\Projects\ParkingSpot2\carPark.mp4')

with open('C:/Projects/ParkingSpot2/CarParkPos', 'rb') as f:
            posList = pickle.load(f)

# Width and Height
width, height = 107, 48 

# Function
def check_parking_space(imgProcess):
      
    space_count = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgProcess[y: y + height, x: x + width]
        # cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            space_count += 1
        else:
            color = (0, 0, 255)
            thickness = 2
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, 
                           thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f"Free: {space_count}/{len(posList)}", (100, 50), scale=2, 
                           thickness=2, offset=15, colorR=(0, 200, 0))


# Main Part
while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)


    check_parking_space(imgDilate)

    cv2.imshow("Parking Spot Detection", img)
    # cv2.imshow("ImageBlur", imgBlur)
    # cv2.imshow("ImageThres", imgMedian)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break