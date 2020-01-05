#!/usr/bin/env python3

import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    BaWframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    imgYellow = cv2.inRange(imgHSV,np.array([25,80,100]), np.array([35,255,255]))




    # Display the resulting frame
    cv2.imshow('Frame',BaWframe)
    cv2.imshow('OG', frame)
    cv2.imshow('stick', imgYellow)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()