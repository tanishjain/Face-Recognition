"""
ECE196 Face Recognition Project
Author: Will Chen

Prerequisite: You need to install OpenCV before running this code
The code here is an example of what you can write to print out 'Hello World!'
Now modify this code to process a local image and do the following:
1. Read geisel.jpg
2. Convert color to gray scale
3. Resize to half of its original dimensions
4. Draw a box at the center the image with size 100x100
5. Save image with the name, "geisel-bw-rectangle.jpg" to the local directory
All the above steps should be in one function called process_image()
"""

# TODO: Import OpenCV
import cv2


# TODO: Edit this function
def process_image():	
	img = cv2.imread("geisel.jpg")
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	height, width = img.shape
	img = cv2.resize(img, (int(width/2), int(height/2)))
	img = cv2.rectangle(img, (int(width/4) - 50, int(height/4) - 50), (int(width/4) + 50, int(height/4) + 50), (255, 255, 255), 2)
	cv2.imwrite("geisel_new.jpg", img)
	return

# Just prints 'Hello World! to screen.
def hello_world():
    print('Hello World!')
    return

# TODO: Call process_image function.
def main():
    hello_world()
    process_image()
    return


if(__name__ == '__main__'):
    main()
