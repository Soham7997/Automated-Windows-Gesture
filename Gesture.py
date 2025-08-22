import time
import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard
# Video capture
cap = cv2.VideoCapture(0)
# Hand detector
detector = HandDetector(
    detectionCon=0.6,
    maxHands=2
)
treshold = 285
width = 900
while cap.isOpened():
    # Read frame
    success, frame = cap.read()
    # Hand detection q
    hands,frame = detector.findHands(frame)
    cv2.line(frame,(0, treshold), (width,treshold),(0,225,0),10)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1["center"]
        handTypes1 = hand1["type"]
        finger1 = detector.fingersUp(hand1)
        cx,cy = hand1["center"]

        if cy <= treshold:
            if finger1 == [0, 1, 1, 0, 0]:
                keyboard.press_and_release("windows+ tab")
                time.sleep(1)

            if finger1 == [1, 0, 0, 0, 0]:
                keyboard.press_and_release("right arrow")
                time.sleep(1)
            if finger1 == [0, 0, 0, 0, 1]:
                keyboard.press_and_release("left arrow")
                time.sleep(1)
            if finger1 == [1, 1, 0, 0, 0]:
                keyboard.press_and_release("up arrow")
                keyboard.press_and_release("up arrow")
                keyboard.press_and_release("up arrow")
                keyboard.press_and_release("up arrow")
                keyboard.press_and_release("up arrow")
                time.sleep(1)
            if finger1 == [0, 1, 1, 1, 1]:
                keyboard.press_and_release("space")
                time.sleep(1)
            if finger1 == [0, 1, 0, 0, 0]:
                keyboard.press_and_release("ctrl + tab")
                time.sleep(1)

            if finger1 == [1, 1, 1, 0, 0]:
                keyboard.press_and_release("down arrow")
                keyboard.press_and_release("down arrow")
                keyboard.press_and_release("down arrow")
                keyboard.press_and_release("down arrow")
                keyboard.press_and_release("down arrow")
                time.sleep(1)
            if finger1 == [1, 1, 1, 1, 1]:
                keyboard.press_and_release("f3")
                time.sleep(1)
        #print(lmList1)
        print(finger1)
# Display frame
    cv2.imshow('Hand Detection', frame)  # More descriptive title

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
