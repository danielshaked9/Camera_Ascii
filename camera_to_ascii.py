from turtle import clear
from matplotlib.cbook import print_cycles
import numpy as np
import cv2 as cv
from image_to_ascii import *
from text_to_image import *
from time import sleep
import os






cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #cv.imwrite("stream.png",gray)
    #im_pil = Image.fromarray(frame)
    aimg=covertImageToAscii(frame,cols=100,scale=1,moreLevels=1)
    # open file
    #f = open("out.txt", 'w')
	# write to file
    for row in aimg:
        #f.write(row + '\n')
        print(row)
    #aimg=covertImageToAscii("stream.png",cols=100,scale=1,moreLevels=1)
	# cleanup
    #f.close()
    #gray=textfile_to_image("out.txt")
    #cv.imwrite("imgout.png",gray)
    #sleep(0.5)

    # Display the resulting frame
    #cv.imshow('frame', gray)
    
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()