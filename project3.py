import cv2
import numpy as np
#######################################################
frameHeight = 480
frameWidth = 640
plateCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_russian_plate_number.xml")
minArea = 500
color = (255, 0, 0)
count = 0
#######################################################

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

while True:
    _, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Plate", (x, y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)

            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow('Plate', imgRoi)

    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite('Resources/nPlates/Scanned/nPlate_'+str(count)+'.jpg', imgRoi)
        count += 1


    cv2.imshow("WebCam", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
