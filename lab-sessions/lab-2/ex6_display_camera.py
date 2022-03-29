import cv2
import argparse

def main():
    video_capture = cv2.VideoCapture(0)
    window_name = "video"
    
    while(True):
        _, frame = video_capture.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(1)
        
        # press ESC to close
        if key == 27: 
            break
  
    # When everything done, release all
    video_capture.release()

if __name__ == "__main__":
    main()