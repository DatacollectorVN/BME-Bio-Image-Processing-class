import cv2
import argparse
from utils import controller

def brightnesscontrast(brightness=0):
    # getTrackbarPos returns the current position of the specified trackbar
    brightness = cv2.getTrackbarPos("Brightness",
                                    window_name)
     
    contrast = cv2.getTrackbarPos('Contrast',
                                  window_name)
 
    effect = controller(img, brightness,
                        contrast)
 
    # The function imshow displays an image in the specified window
    cv2.imshow('Effect', effect)

def main(image_file_path):
    img_ori = cv2.imread(image_file_path)
    global img
    img = img_ori.copy()
    global window_name
    window_name = "BME"
    cv2.namedWindow(window_name)
    while True:
        cv2.imshow("BME", img_ori)
        
        # Brightness range -255 to 25
        cv2.createTrackbar("Brightness", window_name, 255, 2 * 255, brightnesscontrast)
     
        # Contrast range -127 to 127
        cv2.createTrackbar("Contrast", window_name, 127, 2 * 127, brightnesscontrast) 
        
        brightnesscontrast(0)
        key = cv2.waitKey(0)
        
        # close all if press ESC
        if key == 27: 
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--imagepath", dest = "image_file_path", type = str,
                        default = None, help = "Image file path")
    args = parser.parse_args()
    image_file_path = args.image_file_path
    main(image_file_path)