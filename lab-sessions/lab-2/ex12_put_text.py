import cv2
import numpy as np

def main():
    canvas_size = (500, 500, 3)
    name_window = "window"
    text = "Nathan Ngo"
    canvas = np.zeros(canvas_size, dtype = "uint8")
    
    # write text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(canvas, text, (50, 50), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
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