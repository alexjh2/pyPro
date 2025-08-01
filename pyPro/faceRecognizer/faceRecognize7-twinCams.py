import cv2
import np as numpy
import time
print(cv2.__version__)
dispW = 640
dispH = 480
flip = 2
font = cv2.FONT_HERSHEY_SIMPLEX
dtav = 0

camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam1 = cv2.VideoCapture(camSet)
cam2 = cv2.VideoCapture(1)
startTime = time.time()
while True:
    ret, frame1 = cam1.read()
    ret, frame2 = cam2.read()
    frame2 = cv2.resize(frame2, (frame1.shape[1], frame1.shape[0]))
    frameCombined = np.hstack((frame1, frame2))
    dt = time.time() - startTime
    startTime = time.time()
    dtav = .9 * dtav + .1 * dt
    fps = 1 / dtav
    cv2.rectangle(FrameCombined, (0,0), (130,40), (0,0,255), -1)
    cv2.putText(frameCombined, str(round(fps,1)) + ' FPS', (0,25))
    cv2.imshow('nanoCam',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()