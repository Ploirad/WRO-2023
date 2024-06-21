#This code is a library for the camera to take the color centroid and area of a specific frame given

#Import the necessary libraries
import cv2
import numpy as np

#This function is used to take the green centroid respect to the X edge and the green area all about the frame gived and they are integer variables
def detect_green(frame):
    V_bajo = np.array([62, 147, 49])
    V_alto = np.array([65, 156, 255])
    return detect_color(frame, V_bajo, V_alto)

#This function is used to take the red centroid respect to the X edge and the red area all about the frame gived
def detect_red(frame):
    R_bajo = np.array([175, 126, 68])
    R_alto = np.array([176, 212, 255])
    return detect_color(frame, R_bajo, R_alto)

#This function is used to take the magenta centroid respect to the X edge and the magenta area all about the frame gived
def detect_magenta(frame):
    M_bajo = np.array([138, 87, 25])
    M_alto = np.array([167, 185, 255])
    return detect_color(frame, M_bajo, M_alto)

#This function is used to take the centroid and the area of the color gived (color_low, color_high) in the respective frame
def detect_color(frame, color_low, color_high):
    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the specified color range
    mask = cv2.inRange(hsv, color_low, color_high)

    # Find contours in the mask
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # If no contours are found, return None
    if not contours:
        return None, 0

    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # Compute the center and area of the largest contour
    M = cv2.moments(largest_contour)
    if M["m00"] == 0:
        return None, 0
    cX = int(M["m10"] / M["m00"])
    area = cv2.contourArea(largest_contour)

    return cX, area