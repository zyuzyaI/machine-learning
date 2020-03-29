# Importing all necessary libraries
from hashlib import md5
from cv2 import imread
import scipy.spatial
import numpy as np
import itertools
import hashlib
import time
import cv2 
import os 

# Read the video from specified path 
def create(video, file_name="file", cur_dir=""):
    cam = cv2.VideoCapture("C:/Users/Irka/github/machine-learning/OpenCV/template/"+video) 
    try:             
        # creating a folder named data 
        if not os.path.exists('data'): 
            os.makedirs('data') 
    
    # if not created then raise error 
    except OSError: 
        print ('Error: Creating directory of data') 
    
    # frame 
    currentframe = 0
    
    while(True): 
        os.chdir(cur_dir)
        # reading from frame 
        ret,frame = cam.read() 
    
        if ret: 
            # if video is still left continue creating images 
            name = "data/"+file_name + str(currentframe) + '.jpg'
               
            # writing the extracted images 
            cv2.imwrite(name, frame) 
            name = name.split("/")[-1]
            tmp = FindSimilar(name, cur_dir=cur_dir)
            if tmp.worker() == False:
                os.remove(name)
            else:
                print ('Creating...' + name)
            # increasing counter so that it will show how many frames are created 
            currentframe += 1
        else: 
            break

    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows() 

class FindSimilar:
    def __init__(self, image_name, cur_dir="", file_path="/data"):
        os.chdir(cur_dir+file_path)
        self.file_path = file_path
        self.image_name = image_name
        print(image_name)

    def worker(self):
        if len(os.listdir()) == 1:
            return True

        for img in os.listdir():
            if img == self.image_name:
                continue 
            img = self.filter_images(img)
            check_img = self.filter_images(self.image_name)
            if self.hamming_distance(self.difference_score(img), 
                    self.difference_score(check_img)) < 0.4:
                return False 
        return True
        
    def filter_images(self, image):
        try:
            assert imread(image).shape[2] == 3
            return image
        except  AssertionError as e:
            print(e)

    def img_gray(self, image):
        image = imread(image)
        return np.average(image, weights=[0.299, 0.587, 0.114], axis=2)

    #resize image and flatten
    def resize(self, image, height=30, width=30):
        row_res = cv2.resize(image,(height, width), interpolation = cv2.INTER_AREA).flatten()
        col_res = cv2.resize(image,(height, width), interpolation = cv2.INTER_AREA).flatten('F')
        return row_res, col_res

    #gradient direction based on intensity 
    def intensity_diff(self, row_res, col_res):
        difference_row = np.diff(row_res)
        difference_col = np.diff(col_res)
        difference_row = difference_row > 0
        difference_col = difference_col > 0
        return np.vstack((difference_row, difference_col)).flatten()
       
    def hamming_distance(self, image, image2):
        score = scipy.spatial.distance.hamming(image, image2)
        return score

    def difference_score(self, image, height = 30, width = 30):
        gray = self.img_gray(image)
        row_res, col_res = self.resize(gray, height, width)
        difference = self.intensity_diff(row_res, col_res)
        
        return difference

cur_dir = os.getcwd()
print(cur_dir)
for file_name, video in enumerate(os.listdir(os.getcwd()+"/template")):
    create(video, file_name=str(file_name), cur_dir=cur_dir)
    find_duplicates(cur_dir+"/data")

