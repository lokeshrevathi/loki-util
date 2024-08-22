import cv2 as cv
import numpy as np

def readImage(iPath):
    img = cv.imread(iPath)
    cv.imshow("Display window", img)
    img = np.zeros((512,512,3), np.uint8)


if __name__ == '__main__':
    print(cv.__version__)
    readImage("gmic.png")