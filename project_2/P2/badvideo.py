import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
# Read the input image
#img = cv2.imread('test.png')
#cap = cv2.VideoCapture('test.mp4')
#cap = cv2.VideoCapture(0)

camera = PiCamera()
camera.resolution = (480, 640)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=camera.resolution)

time.sleep(0.1)

#while cap.isOpened():
i=0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    #_, img = cap.read()
    img = frame.array

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    rawCapture.truncate(0)
    
    for (x, y , w ,h) in faces:
        # Change image ratio to 1:1
        try:
            gray = gray[y:y+h, x:x+w]
            gray = cv2.resize(gray, (224, 224))
        except:
            continue
        
    i = i + 1
    cv2.imwrite("img" + str(i) +".jpg", gray)
    time.sleep(0.5)
        
    if i == 150:
        break
        

    # Display the output
    try:
        cv2.imshow('img', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        continue

cap.release()
      