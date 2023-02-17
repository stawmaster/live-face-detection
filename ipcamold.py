import cv2
import sys
from xmlrpc.server import SimpleXMLRPCServer

i=0
detected=[]

cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

cap = cv2.VideoCapture()
cap.open('rtsp://192.168.248.10:8080/h264_ulaw.sdp')

font = cv2.FONT_HERSHEY_SIMPLEX

while(cap.isOpened()):
    ret, frame = cap.read()

    if (i>25 and i<30):
        detected=[]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            detected.append((x,y,w,h))
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    elif(i==30):
        i=0

    i+=1

    for (x, y, w, h) in detected:
        if(w>10):
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame,'Authorized',(x, y+h+20),font, 0.7,(0, 255, 0),1, cv2.LINE_4)
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame,'Unauthorized',(x, y+h+20),font, 0.7,(0, 0, 255),1, cv2.LINE_4)


    scale_percent = 100 # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    cv2.imshow('frame', resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
