import cv2
import argparse

def main(image_file_path, image_write_path):
    # flag = 0 mean, we read and covert to gray scale image.
    # cv2.imread return a array with 3D array if color image and 2D array if gray scale image.
    # read more: https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/
    img = cv2.imread(image_file_path, flags = 0)
    
    cv2.imwrite(image_write_path, img)
    print(f"Done writed image at {image_write_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--imagepath", dest = "image_file_path", type = str,
                        default = None, help = "Image file path")
    parser.add_argument("--imagewrite", dest = "image_write_path", type = str,
                        default = None, help = "Image write path")
    args = parser.parse_args()
    image_file_path = args.image_file_path
    image_write_path = args.image_write_path
    main(image_file_path, image_write_path)