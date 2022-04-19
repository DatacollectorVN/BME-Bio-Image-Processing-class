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

def main(image_path, output_name, threshold1=100, threshold2=200):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    canny_img = canny_function(img, threshold1 = threshold1, threshold2 = threshold2)
    cv2.imshow("window", canny_img)
    cv2.waitKey(0) 
    if output_name is not None:
        os.makedirs('./outputs', exist_ok = True)
        cv2.imwrite(os.path.join('./outputs', output_name), canny_img)
        print('Done saved')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--imagepath', dest = 'image_path', 
                        default = 'Input-image.jpg', type = str)
    parser.add_argument('--output_name', dest = 'output_name', 
                         default=None, type = str)
    parser.add_argument('--threshold1', dest = 'threshold1', 
                        default = 100, type = int)
    parser.add_argument('--threshold2', dest = 'threshold2', 
                        default = 200, type = int)
    args = parser.parse_args()

    main(args.image_path, args.output_name, args.threshold1, args.threshold2)
