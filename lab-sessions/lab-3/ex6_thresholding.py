import cv2 as cv
from matplotlib import pyplot as plt
import argparse

def main(image_path):
    img = cv.imread(image_path, 0)
    _, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) 
    _, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) 
    _, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) 
    _, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
    _, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV'] 
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in range(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray', vmin = 0, vmax = 255) 
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--imagepath', dest = 'image_path', 
                        default = 'Input-image.jpg', type = str)
    args = parser.parse_args()
    main(args.image_path)
