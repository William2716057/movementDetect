
import cv2

#Initialise capture from webcam 
cap = cv2.VideoCapture(0) #0 for webcam

ret, frame1 = cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

while cap.isOpened():
    # read next frame
    ret, frame2 = cap.read()
    if not ret:
        break
    
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)
    
    diff = cv2.absdiff(gray1, gray2)
    
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    
    dilated = cv2.dilate(thresh, None, iterations=2)
    
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 1000: 
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Movement Detector", frame2)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

#use args for settings
#alarm
#security (take screenshot)
#record movements

