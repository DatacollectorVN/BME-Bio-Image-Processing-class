import cv2
import numpy as np
import argparse

def empty(a):
    pass

def main(image_file_path):
    cv2.namedWindow("TrackBars") 
    cv2.resizeWindow("TrackBars", 640, 240) 
    cv2.createTrackbar("Hue Min", "TrackBars",0,179, empty) 
    cv2.createTrackbar("Hue Max", "TrackBars",179,179, empty) 
    cv2.createTrackbar("Sat Min", "TrackBars",0,255, empty) 
    cv2.createTrackbar("Sat Max", "TrackBars",255,255, empty) 
    cv2.createTrackbar("Val Min", "TrackBars",0,255, empty) 
    cv2.createTrackbar("Val Max", "TrackBars",255,255, empty)
    while True:
        img = cv2.imread(image_file_path)
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
        h_min=cv2.getTrackbarPos("Hue Min", "TrackBars") 
        h_max=cv2.getTrackbarPos("Hue Max", "TrackBars") 
        s_min=cv2.getTrackbarPos("Sat Min", "TrackBars") 
        s_max=cv2.getTrackbarPos("Sat Max", "TrackBars") 
        v_min=cv2.getTrackbarPos("Val Min", "TrackBars") 
        v_max=cv2.getTrackbarPos("Val Max", "TrackBars")
        upper = np.array([h_max, s_max,v_max])
        lower = np.array([h_min, s_min, v_min])
        mask = cv2.inRange(imgHSV, lower, upper)
        imgResult = cv2.bitwise_and(img, img, mask=mask) 
        imgHor = np.hstack((img,imgResult)) 
        
        cv2.imshow('HSV Image', imgHSV)
        cv2.imshow('Mask Image', mask)
        cv2.imshow('Result Image', imgResult) 
        cv2.imshow('Stack Image', imgHor)
        
        key = cv2.waitKey(1)
        # press ESC to close
        if key == 27: 
            break
        
    # destroy all windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--imagepath", dest = "image_file_path", type = str,
                        default = None, help = "Image file path")
    args = parser.parse_args()
    image_file_path = args.image_file_path
    main(image_file_path)