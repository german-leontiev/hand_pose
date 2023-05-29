import cv2
import mediapipe as mp

mp_model = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
hist = []

while (True):
    ret, frame = cap.read()

    h, w, _ = frame.shape
    results = mp_model.process(frame)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)
            if len(hist) < 5:
                hist.append([x,y])
            else:
                hist = hist[1:]
                hist.append([x,y])
        for x, y in hist:
            frame = cv2.circle(frame, (x, y), 10, (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()