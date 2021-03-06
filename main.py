'''
@author: luislortega
'''
import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision
import pyautogui

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize the WindowCapture class
#wincap = WindowCapture('LDPlayer')

# load the trained model
cascade_limestone = cv.CascadeClassifier('cascade/cascade.xml')
# load an empty Vision class
vision_limestone = Vision(None)

#loop_time = time()
while(True):
    # get an updated image of the game
    #screenshot = wincap.get_screenshot()
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = screenshot[:,:,::-1].copy()
    # do object detection
    rectangles = cascade_limestone.detectMultiScale(screenshot, 2)

    # draw the detection results onto the original image
    detection_image = vision_limestone.draw_rectangles(screenshot, rectangles)
    imS = cv.resize(detection_image, (400, 300))
    # display the images
    cv.imshow('Matches', imS)

    # debug the loop rate
    #print('FPS {}'.format(1 / (time() - loop_time)))
    #loop_time = time()

    # press 'q' with the output window focused to exit.
    # press 'f' to save screenshot as a positive image, press 'd' to 
    # save as a negative image.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    '''
    elif key == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)
    '''
print('Done.')
