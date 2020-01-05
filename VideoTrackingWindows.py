#!/usr/bin/env python3

# Import video tracking library OPEN CV and python Advance array support with numpy 
import cv2
import numpy as np

# Import math for distance calculations
import math

print("Video Tracking Infinite Recharge:2606")

# initial video capture
cap = cv2.VideoCapture(0)

# Initial Exoisure for darkness
cap.set(cv2.CAP_PROP_EXPOSURE, -12)

# Set resolution and framerate
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

print('Camera has been configured')

# For exposure problem (see below)
exposureResetCounter = 0

while(cap.isOpened()):

    # Found exposure Problem last year auto adjust doesnt turn off here is a fix
    exposureResetCounter = exposureResetCounter + 1
    if exposureResetCounter == 29:
        exposureResetCounter = 0
        cap.set(cv2.CAP_PROP_EXPOSURE, -8) # -8 is around 6 ms expo
    
    # Capture frames 
    ret, frame = cap.read()
    if ret == True:

        # Convert BGR video to HSV for hue selection
        imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Make Black White image of just imgHSV bright green
        imgGreenBW = cv2.inRange(imgHSV, np.array([30, 150, 40]), np.array([100, 255, 255]))
        
        # BGR Version of imgGreenBW image for contour drawing
        imgGreenBGR = cv2.cvtColor(imgGreenBW, cv2.COLOR_GRAY2BGR)

        # Ffind contours and place them in an array
        img2, contours, hierarchy = cv2.findContours(imgGreenBW, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # Sort contour Array by size
        contoursSorted = sorted(contours, key=lambda x: cv2.contourArea(x), reverse = True)

        # Init point array and adjusted array of countours @@ NOTE @@ make change to a single largest item
        #adjContours = []
        points = (0,0)

        # Find Largest Contour
        if len(contoursSorted) >= 1:
            # Make variable of biggest contour
            bigCont = contoursSorted[0]
            
            # Draw that big contour
            cv2.drawContours(imgGreenBGR, bigCont, 0 (255, 0, 255), 3)

            # Point finding 
            moments = cv2.moments(bigCont)
            moment = moments['m00']
            if moment != 0: 
                centerX = int(moments['m10']/moment)
                centerY = int(moments['m01']/moment)

                # Store point
                pt = (centerX, centerY)
                
                # Draw point on window
                cv2.circle(imgGreenBGR, pt, 3, (255, 0, 0), 3)
                
                # Put point in pt array
                points.append(pt)
        
        # write to console point where the center is
        print('center of pixels = {}'.format(pt))

    # Show frame with contours and points
    cv2.imshow("Frame", imgGreenBGR)

    # Show Original image in HSV
    cv2.imshow("HSV", imgHSV)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
 
    # Break the loop
    else: 
        break
# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows() 
