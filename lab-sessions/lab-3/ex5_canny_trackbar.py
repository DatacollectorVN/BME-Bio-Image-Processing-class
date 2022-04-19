import cv2
import numpy as np 
import os
import argparse

def canny_function(img, blur_ksize=7, threshold1=100, threshold2=200):
    ''' Canny Edge Detection
    Args:
        img: (np.array) img_array with RGB
        blur_ksize: (int) Kernel size parameter for Gaussian Blurry
        threshold1: (int) min threshold
        threshold2: (int) max threshold
    Output:
        canny_img: (np.array)
    '''

    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blurred_img = cv2.GaussianBlur(gray_img, ksize = (blur_ksize, blur_ksize), sigmaX = 0)

    # canny edge
    canny_img = cv2.Canny(blurred_img, threshold1 = threshold1, threshold2 = threshold2)

    return canny_img

def null(x):
    pass

def main(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #canny_img = canny_function(img, threshold1 = threshold1, threshold2 = threshold2)
    cv2.namedWindow('Canny') 
    cv2.resizeWindow('Canny', (450,300))
    cv2.createTrackbar('MIN', 'Canny', 80,255, null) 
    cv2.createTrackbar('MAX', 'Canny', 120,255, null)
    
    while True:
        a = cv2.getTrackbarPos('MIN', 'Canny') 
        b = cv2.getTrackbarPos('MAX', 'Canny')
        canny_img = canny_function(img, threshold1 = a, threshold2 = b)
        cv2.imshow('Canny', canny_img)
        key = cv2.waitKey(1) & 0xFF
        # press ESC to close
        if key == 27: 
            break
    cv2.destroyAllWindows()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--imagepath', dest = 'image_path', 
                        default = 'Input-image.jpg', type = str)
    args = parser.parse_args()
    main(args.image_path)
