import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse

def main(image_file_path, image_temp_file_path):
    img = cv.imread(image_file_path, 0)
    cv.imshow("Original image", img)
    img2 = img.copy()
    # take the reference object
    template = cv.imread(image_temp_file_path, 0)
    w, h = template.shape[:2]
    cv.imshow("Template", template)
    # All the 6 methods for comparison in a list
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
    'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        # Apply template Matching
        res = cv.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img, top_left, bottom_right, 255, 2)
        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--imagepath", dest = "image_file_path", type = str,
                        default = None, help = "Image file path")
    parser.add_argument("--imagetemppath", dest = "image_temp_file_path", type = str,
                        default = None, help = "Image file template path")
    args = parser.parse_args()
    image_file_path = args.image_file_path
    image_temp_file_path = args.image_temp_file_path
    main(image_file_path, image_temp_file_path)