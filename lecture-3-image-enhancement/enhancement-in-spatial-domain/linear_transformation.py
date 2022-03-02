import cv2
import numpy as np
import argparse

def main(image_file_path, a, b):
    img_ori = cv2.imread(image_file_path)
    img_clone = img_ori.copy()
    img_clone = img_clone * a + b
    img_clone = np.array(img_clone, dtype = np.uint8)
    
    while True:
        cv2.imshow("image before", img_ori)
        cv2.imshow("image after", img_clone)
        key = cv2.waitKey(0)
        
        # close all if press ESC
        if key == 27: 
            break

    cv2.destroyallwindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--imagepath", dest = "image_file_path", type = str,
                        default = None, help = "Image file path")
    parser.add_argument("--a", dest = "a", type = float, 
                        default = 1, help= "a parameter")
    parser.add_argument("--b", dest = "b", type = float, 
                        default = 0, help= "b parameter")
    
    args = parser.parse_args()
    image_file_path = args.image_file_path
    a = args.a
    b = args.b
    main(image_file_path, a , b)