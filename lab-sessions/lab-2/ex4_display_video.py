import cv2
import argparse

def main(video_file_path):
    video_capture = cv2.VideoCapture(video_file_path)
    window_name = "video"
    if video_capture.isOpened() == False:
        print("Erorr when open video")
    else:
        while True:
            ret, frame = video_capture.read()
            if ret:
                # if video is not the end, then ret is True 
                cv2.imshow(window_name, frame)
                key = cv2.waitKey(1)
                
                # press ESC to close
                if key == 27: 
                    break
            else:
                # ret is False when running out of video
                break
        
        # release the video capture object
        video_capture.release()

        # destroy all windows
        cv2.destroyAllWindows()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--videopath", dest = "video_file_path", type = str,
                        default = None, help = "Video file path")
    args = parser.parse_args()
    video_file_path = args.video_file_path
    main(video_file_path)