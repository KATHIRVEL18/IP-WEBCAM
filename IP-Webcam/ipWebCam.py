import urllib.request
import cv2
import numpy as np
import imutils

url = 'http://192.168.247.143:8080/shot.jpg'


while True:
    try:
        imagePath = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print("Error opening URL:", e)
        continue
    imageNp = np.array(bytearray(imagePath.read()), dtype=np.uint8)
    image = cv2.imdecode(imageNp, -1)
    image = imutils.resize(image, width=400)
    cv2.imshow("CameraFeed",image)
    if ord("q") == cv2.waitKey(1):
        exit(0)
