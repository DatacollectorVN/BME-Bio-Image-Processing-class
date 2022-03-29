import cv2
import numpy as np

def main():
    canvas_size = (500, 500, 3)
    name_window = "window"
    canvas = np.zeros(canvas_size, dtype = "uint8")
    
    # creating a polygon
    pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(canvas, [pts], True, (0, 255, 255))
    while True:
        cv2.imshow(name_window, canvas)
        key = cv2.waitKey(0)
        
        # press ESC to close
        if key == 27: 
            break

    # destroy all windows
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()