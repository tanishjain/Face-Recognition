"""
ECE 196 Face Recognition Project
Author: Will Chen, Simon Fong

What this script should do:
1. Start running the camera.
2. Detect a face, display it, and get confirmation from user.
3. Send it for classification and fetch result.
4. Show result on face display.
"""

import time
import cv2
import base64
import requests
from picamera import PiCamera
from picamera.array import PiRGBArray

# Font that will be written on the image
FONT = cv2.FONT_HERSHEY_SIMPLEX

# TODO: Declare path to face cascade
CASCADE_PATH = "/home/pi/Desktop/Face-Recognition/project_2/P2/haarcascade_frontalface_default.xml"

def request_from_server(img):
    # URL or PUBLIC DNS to your server
    URL = "http://ec2-35-164-225-216.us-west-2.compute.amazonaws.com:8080/predict"
    print("i'm here - 0")
    # File name so that it can be temporarily stored.
    temp_image_name = 'temp.jpg'

    # TODO: Save image with name stored in 'temp_image_name'
    cv2.imwrite(temp_image_name, img)

    # Reopen image and encode in base64
    # Open binary file in read mode
    image = open(temp_image_name, 'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    print("i'm here - 1")
    # Defining a params dict for the parameters to be sent to the API
    payload = {'image': image_64_encode}
    print("i'm here - 2")
    # Sending post request and saving the response as response object
    response = requests.post(url=URL, json=payload)
    print("i'm here - 3")
    # Get prediction from response
    prediction = response.json()
    print("returning prediction")
    return prediction


def main():
    # 1. Start running the camera.
    # TODO: Initialize face detector
    face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

    # Initialize camera and update parameters
    camera = PiCamera()
    width = 640
    height = 480
    camera.rotation = 180
    camera.resolution = (width, height)
    rawCapture = PiRGBArray(camera, size=(width, height))

    # Warm up camera
    print ('Let me get ready ... 2 seconds ...')
    time.sleep(2)
    print ('Starting ...')

    # 2. Detect a face, display it, and get confirmation from user.
    for frame in camera.capture_continuous(
                    rawCapture,
                    format='bgr',
                    use_video_port=True):

        # Get image array from frame
        frame = frame.array
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # TODO: Use face detector to get faces.
        # Be sure to save the faces in a variable called 'faces'
        faces = face_cascade.detectMultiScale(img, 1.1,4)
        rawCapture.truncate(0)

        for (x, y, w, h) in faces:
            print('==================================')
            print('Face detected!')
            cv2.imshow('Face Image for Classification', frame)

            # Keep showing image until a key is pressed
            cv2.waitKey()
            answer = input('Confirm image (1-yes / 0-no): ')
            print(answer)
            print('==================================')
            
            if(answer):
                print('Let\'s see who you are...')

                # TODO: Get label and confidence using request_from_server
                pred = request_from_server(img)
                print('New result found!')

                # TODO: Display label on face image
                # Save what you want to write on image to 'result_to_display'
                # [OPTIONAL]: At this point you only have a number to display,
                # you could add some extra code to convert your number to a
                # name
                result_to_display = pred 
                cv2.putText(frame, str(result_to_display), (10, 30), FONT, 1, (0, 255, 0), 2)
                cv2.imshow('Face Image for Classification', frame)
                cv2.waitKey()
                break

        # Delete image in variable so we can get the next frame
        rawCapture.truncate(0)

        print('Waiting for image...')
        time.sleep(1)


# Runs main if this file is run directly
if(__name__ == '__main__'):
    main()
