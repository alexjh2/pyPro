import cv2
print(cv2.__version__)
dispW = 320
dispH = 240
flip = 2
camSet = camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
while True:
    ret, frame = cam.read()
    cv2.imshow('piCam', frame)
    cv2.moveWindow('piCam', 0 , 0)
    cv2.imshow('piCam2', frame)
    cv2.moveWindow('piCam2', 350 , 0)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayVideo', gray)
    cv2.moveWindow('grayVideo', 0, 270)
    cv2.imshow('grayVideo', gray)
    cv2.moveWindow('grayVideo', 350, 270)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()