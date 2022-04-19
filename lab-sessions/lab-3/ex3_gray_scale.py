import cv2
import numpy as np
import argparse

def main(image_file_path):
    img = cv2.imread(image_file_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    name_window_1 = "original"
    name_window_2 = "grayscale"

    while True:
        cv2.imshow(name_window_1, img)
        cv2.imshow(name_window_2, img_gray)
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