import cv2
import sys
from xmlrpc.server import SimpleXMLRPCServer


# cascPath2 = 'haarcascade_profileface.xml'
# faceCascade2 = cv2.CascadeClassifier(cascPath2)


i=0
detected=[]

cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

cap = cv2.VideoCapture()
cap.open('rtsp://192.168.108.32:8080/h264_ulaw.sdp')


def getsquares():
    while(cap.isOpened()):
        ret, frame = cap.read()


        detected=[]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        # faces2 = faceCascade2.detectMultiScale(
        #     gray,
        #     scaleFactor=1.1,
        #     minNeighbors=5,
        #     minSize=(30, 30)
        # )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            detected.append((x,y,w,h))
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # for (x, y, w, h) in faces2:
        #     detected.append((x,y,w,h))
        #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        return detected
        # for (x, y, w, h) in detected:
        #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #
        # scale_percent = 100 # percent of original size
        # width = int(frame.shape[1] * scale_percent / 100)
        # height = int(frame.shape[0] * scale_percent / 100)
        # dim = (width, height)
        #
        # resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        #
        # cv2.imshow('frame', resized)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

# cap.release()
# cv2.destroyAllWindows()



server = SimpleXMLRPCServer(("192.168.108.105", 8000))
print("Listening on port 8000...")
server.register_function(getsquares, "getsquares")
server.serve_forever()
