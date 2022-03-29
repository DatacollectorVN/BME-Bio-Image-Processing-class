import cv2
import argparse

def main(video_file_path, video_write_path):
    video_capture = cv2.VideoCapture(video_file_path)
    window_name = "video"

    # get all meta-information in source video
    # if we want to save with different properties, changes it.
    frame_width = int(video_capture.get(3))
    frame_height = int(video_capture.get(4))
    frame_size = (frame_width,frame_height)
    fps = int(video_capture.get(5))

    if video_write_path.split('.')[-1] == "avi":
        format_video = cv2.VideoWriter_fourcc(*'MJPG')
    elif video_write_path.split('.')[-1] == "mp4":
        # note might be this will get some wrong cause different opencv version
        # you can read more discuss here. https://stackoverflow.com/questions/30509573/writing-an-mp4-video-using-python-opencv
        format_video = cv2.VideoWriter_fourcc(*'mp4v')
    else:
        print("wrong format video output")
    
    result = cv2.VideoWriter(video_write_path, format_video, fps, frame_size)
    while(True):
        ret, frame = video_capture.read()
        if ret == True: 
            # if video is not the end, then ret is True

            # Write the frame into video_write_path
            result.write(frame)
    
            cv2.imshow(window_name, frame)
            key = cv2.waitKey(1)
            
            # press ESC to close
            if key == 27: 
                break

        else:
            # ret is False when running out of video
            break
  
    # When everything done, release all
    video_capture.release()
    result.release()
    print(f"Done write video in {video_write_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--videopath", dest = "video_file_path", type = str,
                        default = None, help = "Video file path")
    parser.add_argument("--videowrite", dest = "video_write_path", type = str,
                        default = None, help = "Video write path")
    args = parser.parse_args()
    video_file_path = args.video_file_path
    video_write_path = args.video_write_path
    main(video_file_path, video_write_path)