import cv2
import glob
import os
import shutil


dir_list = os.listdir("images")

for directory in dir_list:

    sub_dir_list = os.listdir("images/" + directory + "/")
    training_list = sub_dir_list[0:int(0.7*len(sub_dir_list))]
    test_list = sub_dir_list[int(0.7*len(sub_dir_list)):int(0.9*len(sub_dir_list))]
    validation_list = sub_dir_list[int(0.9*len(sub_dir_list)):]
    
    for image in training_list:
        
        if not os.path.exists("/home/pi/Desktop/Face-Recognition/Training/" + directory + "/"):
            os.makedirs("/home/pi/Desktop/Face-Recognition/Training/" + directory + "/")
            
        shutil.move("images/" + directory + "/" + image , "/home/pi/Desktop/Face-Recognition/Training/" + directory + "/")
        
    for image in test_list:
        
        if not os.path.exists("/home/pi/Desktop/Face-Recognition/Test/" + directory + "/"):
            os.makedirs("/home/pi/Desktop/Face-Recognition/Test/" + directory + "/")
            
        shutil.move("images/" + directory + "/" + image , "/home/pi/Desktop/Face-Recognition/Test/" + directory + "/")
        
    for image in validation_list:
        
        if not os.path.exists("/home/pi/Desktop/Face-Recognition/Validation/" + directory + "/"):
            os.makedirs("/home/pi/Desktop/Face-Recognition/Validation/" + directory + "/")
            
        shutil.move("images/" + directory + "/" + image , "/home/pi/Desktop/Face-Recognition/Validation/" + directory + "/")
        
        