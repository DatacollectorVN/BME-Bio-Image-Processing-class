import cv2
import numpy as np
import argparse

def main(image_file_path):
    # flag = 0 mean, we read and covert to gray scale image.
    # cv2.imread return a array with 3D array if color image and 2D array if gray scale image.
    # read more: https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/
    img = cv2.imread(image_file_path, flags = 0)
    print(f"img.shape = {img.shape}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--imagepath", dest = "image_file_path", type = str,
                        default = None, help = "Image file path")
    args = parser.parse_args()
    image_file_path = args.image_file_path
    main(image_file_path)