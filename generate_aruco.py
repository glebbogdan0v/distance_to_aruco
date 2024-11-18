from cv2 import aruco
import cv2 as cv

#dictionary to specify type of the marker
marker_dict = aruco.getPredefinedDictionary(aruco.DICT_7X7_250)

#MARKER_ID = 0
MARKER_SIZE = 400 #pixels

# generating unique IDs using for loop
for id in range(20): #generating 20 markers
    # using function to draw a marker
    marker_image = aruco.generateImageMarker(marker_dict, id, MARKER_SIZE)
    cv.imshow("img", marker_image)
    cv.imwrite(f"./markers/marker_{id}.png", marker_image)


