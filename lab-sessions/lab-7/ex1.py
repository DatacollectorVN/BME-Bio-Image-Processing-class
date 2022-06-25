import numpy as np
import cv2 as cv
import argparse

def main(image_file_path):
    img = cv.imread(image_file_path)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations = 2)
    cv.imshow("Opening", opening)
    # sure background area
    sure_bg = cv.dilate(opening, kernel, iterations=3)
    cv.imshow("sure background", sure_bg)
    # Finding sure foreground area
    dist_transform = cv.distanceTransform(opening, cv.DIST_L2,5)
    cv.imshow("dist transform", dist_transform)
    _, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    cv.imshow("Sure fg", sure_fg)
    unknown = cv.subtract(sure_bg,sure_fg)
    cv.imshow("Unknown region", unknown)

    # Marker labelling
    _, markers = cv.connectedComponents(sure_fg)

    markers = markers+1
    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0
    # cv.imshow("Original", img)

    markers = cv.watershed(img,markers)
    img[markers == -1] = [255,0,0] #apply marker
    # cv.imshow("Final result", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--imagepath", dest = "image_file_path", type = str,
                        default = None, help = "Image file path")
    args = parser.parse_args()
    image_file_path = args.image_file_path
    main(image_file_path)