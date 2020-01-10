#!/usr/bin/env python3

import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0)
 
cap.set(cv2.CAP_PROP_EXPOSURE, 16)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 35)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
cap.set(cv2.CAP_PROP_AUTO_WB, 1)
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  cap.set(cv2.CAP_PROP_EXPOSURE, 12)
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    BaWframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #circleFrame = cv2.HoughCircles(BaWframe, cv2.HOUGH_GRADIENT, 20, 100, circles=10, param1=None, param2=None, minRadius=None, maxRadius=None)

    # detect circles in the image
    circles = cv2.HoughCircles(BaWframe, cv2.HOUGH_GRADIENT, 1.2, 100)
    
    # ensure at least some circles were found
    if circles is not None:
      # convert the (x, y) coordinates and radius of the circles to integers
      circles = np.round(circles[0, :]).astype("int")
    
      # loop over the (x, y) coordinates and radius of the circles
      for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)



    # Display the resulting frame
    cv2.imshow('Frame',BaWframe)
    cv2.imshow('OG', frame)
    #cv2.imshow('stick', circleFrame)

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