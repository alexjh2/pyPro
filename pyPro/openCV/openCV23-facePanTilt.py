import cv2
print(cv2.__version__)
dispW = 640
dispH = 480
flip = 2
from adafruit_servokit import Servokit
kit = Servokit(channels = 16)
pan = 90
tilt = 90
kit.servo[0].angle = pan
kit.servo[1].angle = tilt
#Uncomment These next Two Line for Pi Camera
#camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('/home/aj/Desktop/pyPro/cascade/face.xml')
eye_cascade = cv2.CascadeClassifier('/home/aj/Desktop/pyPro/cascade/eye.xml')
while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+W,y+h), (0,0,255), 2)
        Xcent = x+w/2
        Ycent = y+h/2
        errorPan = Xcent - dispW/2
        errorTilt = Ycent - dispH/2
        if abs(errorPan) > 15:
            pan = pan - errorPan / 50
        if abs(errorTilt) > 15:
            tilt = tilt - errorTilt / 50
        if pan > 180:
            pan = 180
            print("Pan out of range")
        if pan < 0:
            pan = 0
            print("Pan out of range")
        if tilt > 180:
            tilt = 180
            print("Tilt out of range")
        if tilt < 0:
            tilt = 0
            print("Tilt out of range")
        kit.servo[0].angle = pan
        kit.servo[1].angle = tilt

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh))
    cv2.imshow('nanoCam',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()