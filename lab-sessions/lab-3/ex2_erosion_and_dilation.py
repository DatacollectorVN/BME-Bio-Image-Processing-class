import cv2
import numpy as np
import argparse

def main(image_file_path):
    img = cv2.imread(image_file_path)
    # get srtucture element (S)
    # read here https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    img_erosion = cv2.erode(img, kernel, cv2.BORDER_REFLECT, iterations = 10)
    img_dilation = cv2.dilate(img, kernel, iterations = 10)
    name_window_1 = "original"
    name_window_2 = "erosion"
    name_window_3 = "dilation"

    while True:
        cv2.imshow(name_window_1, img)
        cv2.imshow(name_window_2, img_erosion)
        cv2.imshow(name_window_3, img_dilation)
        key = cv2.waitKey(0)
        
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