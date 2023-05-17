import cv2

cap = cv2.VideoCapture('BadApple.mp4')
x = 0
while True:
    exist, frame = cap.read()
    if not exist:
        break
    if True:
        cv2.imwrite(f'Frames/{x}.jpg', frame)
    x += 1