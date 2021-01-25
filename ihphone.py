# import the required library
import numpy as np
import cv2
from matplotlib import pyplot as plt

device = 1 # Front camera
# read the image
#img = cv2.imread('triangle.jpg')
cap = cv2.VideoCapture(device)


while cap.isOpened():
    # convert image to gray scale image
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is not empty
    if not ret:
      continue

    # Auto rotate camera
    frame = cv2.autorotate(frame, device)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect corners with the goodFeaturesToTrack function.
    corners = cv2.goodFeaturesToTrack(gray, 3, 0.01, 10)
    corners = np.int0(corners)

    # we iterate through each corner,
    # making a circle at each point that we think is a corner.
    for i in corners:
        x, y = i.ravel()
        cv2.circle(frame, (x, y), 3, 255, -1)

    cv2.imshow('frame', frame)
