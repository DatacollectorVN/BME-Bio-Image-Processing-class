import cv2
import numpy as np

def main():
    canvas_size = (500, 500, 3)
    name_window = "window"
    canvas = np.zeros(canvas_size, dtype = "uint8")
    
    # creating a circle
    cv2.circle(canvas, (200, 200), 80, (0, 20, 200), 10)
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