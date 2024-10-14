# Importing Modules
import cv2
import pickle

width, height = 107, 48

try:
    with open('C:/Projects/ParkingSpot2/CarParkPos', 'rb') as f:
            posList = pickle.load(f)
except:
    posList = []

# Funcitons
def mouse_click(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('C:/Projects/ParkingSpot2/CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

# Main part
while True:
    img = cv2.imread('C:/Projects/ParkingSpot2/carParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouse_click)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break