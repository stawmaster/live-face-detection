import xmlrpc.client
import cv2
import sys


cap = cv2.VideoCapture()
cap.open('rtsp://192.168.108.32:8080/h264_ulaw.sdp')

i=0
fac=[]


proxy= xmlrpc.client.ServerProxy("http://192.168.108.105:8000/")

while(cap.isOpened()):
    ret, frame = cap.read()
    fac=[]
    if (i>25 and i<30):
        fac=proxy.getsquares()
        print(fac)

    elif(i==30):
        i=0
    i+=1
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
proxy.close()
